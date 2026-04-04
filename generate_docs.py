import json
import os
from collections import defaultdict

# Load JSON
with open('ai-leaks-incidents-public.json', 'r') as f:
    public_incidents = json.load(f)

# 1. Complete Incident Table
def get_date(incident):
    d = incident.get('date')
    return d if d is not None else "0000-00-00"

sorted_incidents = sorted(public_incidents, key=get_date, reverse=True)

table_lines = ["| # | Name | Company | Date | Type | Severity | Accessibility | Verified |",
               "|---|---|---|---|---|---|---|---|"]
for idx, inc in enumerate(sorted_incidents, 1):
    date_str = inc.get('date') or "unknown"
    verified_str = "Yes" if inc.get('verified') else "No"
    table_lines.append(f"| {idx} | {inc['incident_name']} | {inc['company']} | {date_str} | {inc['type']} | {inc['severity']} | {inc['accessibility']} | {verified_str} |")

table_md = chr(10).join(table_lines)

# 2. Statistics
total = len(public_incidents)
type_counts = defaultdict(int)
severity_counts = defaultdict(int)
accessibility_counts = defaultdict(int)
year_counts = defaultdict(int)
verified_count = 0
companies = set()
urls_count = 0

for inc in public_incidents:
    type_counts[inc.get('type', 'unknown')] += 1
    severity_counts[inc.get('severity', 'unknown')] += 1
    accessibility_counts[inc.get('accessibility', 'unknown')] += 1
    
    date_str = inc.get('date')
    if date_str:
        year_counts[date_str[:4]] += 1
        
    if inc.get('verified'):
        verified_count += 1
        
    if inc.get('company'):
        companies.add(inc.get('company'))
        
    urls = inc.get('urls')
    if urls and len(urls) > 0:
        urls_count += 1

stats_md = "## 2. Statistics\n\n**By incident type:**\n"
for t, c in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
    stats_md += f"- {t}: {c} ({(c/total)*100:.1f}%)\n"

stats_md += "\n**By severity:**\n"
for s in ['critical', 'high', 'medium', 'low']:
    c = severity_counts.get(s, 0)
    stats_md += f"- {s}: {c} ({(c/total)*100:.1f}%)\n"

stats_md += "\n**By accessibility:**\n"
for a in ['live', 'patched', 'taken_down', 'contained', 'archived', 'unknown']:
    c = accessibility_counts.get(a, 0)
    stats_md += f"- {a}: {c} ({(c/total)*100:.1f}%)\n"

stats_md += "\n**By year:**\n"
for y in ['2024', '2025', '2026']:
    c = year_counts.get(y, 0)
    stats_md += f"- {y}: {c}\n"

stats_md += "\n**Verified:**\n"
stats_md += f"- {verified_count} verified vs {total - verified_count} unverified\n"

stats_md += "\n**Companies:**\n"
stats_md += f"- {len(companies)} unique companies affected\n"

stats_md += "\n**URL coverage:**\n"
stats_md += f"- {(urls_count/total)*100:.1f}% with at least 1 URL\n"

# 3. Schema Documentation
with open('schema.json', 'r') as f:
    schema = json.load(f)

required_fields = set(schema.get('required', []))
schema_md = "## 3. Schema Documentation\n\n"
for field_name, props in schema['properties'].items():
    is_required = "Required" if field_name in required_fields else "Optional"
    type_str = props.get('type', 'unknown')
    if isinstance(type_str, list):
        type_str = " or ".join(type_str)
    
    valid_values = ""
    if 'enum' in props:
        valid_values = f" Valid values: {', '.join(str(v) for v in props['enum'])}."
        
    example = ""
    for inc in public_incidents:
        if field_name in inc and inc[field_name] is not None:
            example = str(inc[field_name])
            if len(example) > 50:
                example = example[:47] + "..."
            break
            
    schema_md += f"### `{field_name}`\n"
    schema_md += f"- **Type**: {type_str}\n"
    schema_md += f"- **Requirement**: {is_required}\n"
    schema_md += f"- **Description**: {props.get('description', '')}{valid_values}\n"
    schema_md += f"- **Example**: `{example}`\n\n"

# 4. Validation Rules
validation_md = """## 4. Validation Rules
Based on `validate.py`, the validator checks the following:
- **Root Element**: Ensures the JSON root is an array.
- **Record Structure**: Checks for any unknown fields (not in schema) and any missing required fields.
- **Type Checking**: Validates that each field's value matches the expected Python type (e.g., `str`, `list`, `bool`, or `None`).
- **Null Checks**: Fails if a required field is `null`.
- **Enum Checking**: Verifies that values for fields like `type`, `accessibility`, `severity`, `verified`, `date_missing`, and `data_classification` exactly match their predefined list of allowed values.
- **Format Verification**:
  - `date`: Must match the ISO 8601 format (`YYYY-MM-DD`) and be a valid calendar date.
  - `cve`: Must match the regex `^CVE-\d{4}-\d+$`.
  - `urls`: Must be a list of strings, and each string must start with `http://` or `https://`.
- **Duplicate Detection**: Identifies duplicate records by checking for identical `incident_name` values.
- **Reachability (Optional)**: With the `--strict` flag, it performs a HEAD request to each URL in the `urls` array to check if it returns a status code `< 400`.
"""

# 5. Notable Incidents
notable_mapping = {
    "Claude Opus 4.6 Mass Distillation on HuggingFace": ("Claude Opus 4.6 mass distillation", "Article 50 (Systemic Risk)"),
    "Claude Code npm Source Map Leak": ("Claude Code source map exposure", "Article 10 (Risk Management)"),
    "Meta AI Agent Rogue Data Breach (SEV1)": ("Meta agent breach", "Article 10 (Risk Management) - CVSS 9.8 equivalent"),
    "Mistral API Key Leak + Model Inversion": ("Mistral model inversion", "Article 14 (Transparency and Provision of Information)"),
    "Scale AI Data Labeler Backdoor Insertion": ("Scale AI backdoor", "Article 15 (Data Governance)")
}

notable_md = "## 5. Notable Incidents (deep-dive on 5)\n\n"
for search_name, (display_name, eu_act) in notable_mapping.items():
    inc = next((i for i in public_incidents if search_name.lower() in i['incident_name'].lower()), None)
    if inc:
        impact = inc.get('what_exposed', 'Unknown impact')
        status = inc.get('accessibility', 'unknown')
        date_str = inc.get('date', 'unknown')
        how = inc.get('how', 'Unknown methodology')
        
        notable_md += f"### {display_name}\n"
        notable_md += f"- **What happened**: {how}\n"
        notable_md += f"- **When**: {date_str}\n"
        notable_md += f"- **Impact**: {impact}\n"
        notable_md += f"- **EU AI Act article violated**: {eu_act}\n"
        notable_md += f"- **Current status**: {status}\n\n"
    else:
        notable_md += f"### {display_name}\n- Incident details not found in dataset.\n\n"

# 6. Data Quality Analysis
dq_md = f"""## 6. Data Quality Analysis
- **Verified vs unverified criteria**: A record is marked as `verified: true` only if there is at least one independently confirmed public source (such as a news article or official security advisory). Currently, there are {verified_count} verified incidents out of the dataset of {total}.
- **Missing date analysis**: Incidents without a clear disclosure or discovery date are assigned `null` for `date` and `date_missing: true`. This reflects the reality of many AI leaks where exact timelines are obfuscated.
- **URL coverage**: Currently, {(urls_count/total)*100:.1f}% of the records contain at least one source URL. Higher URL coverage directly correlates with verifiability.
- **Recommendations to reach 80% verified**: 
  1. Conduct targeted OSINT (Open Source Intelligence) searches for incidents currently lacking URLs.
  2. Monitor security vendor blogs (like Wiz, Oligo, Salt Security) for post-mortem reports of unverified breaches.
  3. Establish a standard for archiving sources (e.g., Wayback Machine) to prevent link rot, making verification more robust.
"""

output = f"# Dataset Analysis\n\n## 1. Complete Incident Table\n\n{table_md}\n\n{stats_md}\n\n{schema_md}\n\n{validation_md}\n\n{notable_md}\n\n{dq_md}"

os.makedirs('docs', exist_ok=True)
with open('docs/04_DATASET_ANALYSIS.md', 'w') as f:
    f.write(output)
print("Report generated successfully.")