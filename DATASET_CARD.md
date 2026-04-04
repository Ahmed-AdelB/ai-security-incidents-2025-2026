---
license: cc-by-4.0
language:
- en
tags:
- ai-security
- incident-dataset
- threat-intelligence
- red-teaming
- supply-chain
- data-leaks
- model-security
task_categories:
- text-classification
pretty_name: AI System Security Incidents 2025-2026
size_categories:
- n<1K
dataset_info:
  features:
  - name: incident_name
    dtype: string
  - name: company
    dtype: string
  - name: date
    dtype: string
  - name: type
    dtype: string
  - name: how
    dtype: string
  - name: what_exposed
    dtype: string
  - name: accessibility
    dtype: string
  - name: severity
    dtype: string
  - name: urls
    dtype: string
  - name: cve
    dtype: string
  - name: verified
    dtype: bool
  - name: date_missing
    dtype: bool
  - name: data_classification
    dtype: string
  splits:
  - name: verified
    num_bytes: 5800
    num_examples: 12
  - name: full
    num_bytes: 26544
    num_examples: 55
configs:
- config_name: default
  data_splits:
  - split_name: verified
  - split_name: full
  default: true
size_in_bytes: 32344
---

# AI System Security Incidents 2025–2026

## Dataset Summary

A structured dataset of **55 real-world security incidents (12 verified, 43 unverified)** affecting AI systems, companies, and infrastructure between January 2025 and April 2026. This is the first publicly released structured dataset purpose-built for AI security research, covering supply chain attacks, model weight theft, training data poisoning, system prompt leaks, API key exposures, and state-sponsored misuse of AI tools.

The dataset is designed to support:
- AI red-teaming and threat modeling
- EU AI Act Article 9/13/15 conformity assessment
- Academic research on AI system vulnerabilities
- Incident response training and tabletop exercises

## Dataset Preview

First 5 incidents in the dataset:

| Incident Name | Company | Date | Severity | Type |
|---------------|---------|------|----------|------|
| Meta AI Authorization Bypass | Meta | 2025-01-12 | medium | api_vulnerability |
| Shai-Hulud npm Worm v1 | npm ecosystem (AI/ML packages) | 2025-09-15 | critical | supply_chain |
| OpenAI Mixpanel Vendor Breach | OpenAI | 2025-11-09 | medium | user_data |
| PRC Cyber Operation Using Claude-Based Tools | Anthropic (tools misused) | 2025-11-13 | critical | state_sponsored_misuse |
| Shai-Hulud npm Worm v2.0 | npm ecosystem | 2025-11-03 | critical | supply_chain |

## Dataset Details

| Field | Value |
|-------|-------|
| **Incidents** | 55 (Jan 2025 – Apr 2026) |
| **Companies affected** | 25+ (Anthropic, OpenAI, Meta, xAI, HuggingFace, GitHub, Scale AI, Stability AI, NVIDIA, others) |
| **Severity breakdown** | Critical: 20 (36.4%) · High: 22 (40.0%) · Medium: 13 (23.6%) |
| **Active/Live incidents** | 4 (10%) still accessible at time of publication |
| **Verified (with sources)** | 12 records with public URLs |
| **License** | CC-BY 4.0 |
| **Author** | Ahmed Adel Bakr Alderai |

## Schema

Each record contains 16 fields:

| Field | Type | Description |
|-------|------|-------------|
| `incident_name` | string | Descriptive name of the incident |
| `company` | string | Affected organization(s) |
| `date` | string \| null | Incident date (ISO 8601) or null if unknown |
| `type` | string | Incident category (see taxonomy below) |
| `how` | string | Attack vector or failure mode |
| `what_exposed` | string | Description of exposed assets (sanitized for publication) |
| `accessibility` | string | Current accessibility status |
| `severity` | string | Severity level |
| `urls` | list[string] | Public source URLs |
| `cve` | string \| null | CVE identifier if assigned |
| `verified` | boolean | True if public sources confirm the incident |
| `date_missing` | boolean | True if the incident date is unknown |
| `data_classification` | string | Publication classification (see below) |
| `confidence_score` | float | Confidence score on 0.0–1.0 scale |
| `discovery_date` | string \| null | Date the incident was discovered |
| `patch_date` | string \| null | Date the incident was patched (null if unknown) |

### Incident Type Taxonomy

| Value | Description |
|-------|-------------|
| `supply_chain` | Compromised dependencies, npm packages, build pipelines |
| `source_code` | Source code leaks, CVEs, RCE vulnerabilities |
| `user_data` | User PII, conversation data, account takeovers |
| `training_data` | Training dataset poisoning, exfiltration, backdoor insertion |
| `api_keys` | API key/token exposure and credential theft |
| `model_weights` | Model weight exfiltration or unauthorized distillation |
| `system_prompt` | System prompt extraction or jailbreak |
| `api_vulnerability` | Misconfigured or vulnerable API endpoints |
| `state_sponsored_misuse` | Nation-state exploitation of AI tools |

### Accessibility Status

| Value | Description |
|-------|-------------|
| `live` | Incident is still accessible/ongoing |
| `patched` | Vulnerability has been fixed |
| `taken_down` | Exposed data/service has been removed |
| `contained` | Impact has been limited/controlled |
| `archived` | Data is archived but no longer actively accessible |
| `unknown` | Status could not be determined |

### Data Classification

| Value | Description |
|-------|-------------|
| `public_sources_only` | All information sourced from public reporting |
| `redacted_internal_data` | `what_exposed` field sanitized to remove specific internal details |
| `unverified` | No public sources found; incident reported through secondary channels |

## Usage

### Load with Python

```python
import json

with open('ai-leaks-incidents-public.json') as f:
    incidents = json.load(f)

# Filter by severity
critical = [i for i in incidents if i['severity'] == 'critical']
print(f"{len(critical)} critical incidents")

# Filter verified incidents with sources
verified = [i for i in incidents if i['verified']]
print(f"{len(verified)} verified incidents with public sources")
```

### Load with pandas

```python
import pandas as pd

df = pd.read_csv('ai-leaks-incidents-public.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Severity distribution
print(df['severity'].value_counts())

# Incidents by company
print(df['company'].value_counts().head(10))
```

## Dataset Construction

This dataset was assembled through:

1. **Multi-agent research pipeline** — Parallel AI agents querying security feeds, CVE databases, threat intelligence sources, and HuggingFace model repositories
2. **Source triangulation** — Each incident verified against multiple independent sources where possible
3. **Structured extraction** — Consistent schema applied across all 55 incidents for machine readability
4. **Field-level sanitization** — 12 records have `what_exposed` sanitized to remove specific internal details (e.g., employee PII, proprietary client names) while preserving research utility

### Novel Finding

Two novel findings emerge from this dataset: (1) **Claude Opus 4.6 Mass Distillation on HuggingFace** — 2.1M total downloads across 50 open-source model variants fine-tuned on 10,000+ Claude API outputs, representing unauthorized IP extraction at scale. (2) **Claude Code npm Source Map Leak** — revealed 512,000+ lines of TypeScript source code enabling the first comprehensive static analysis of a production AI agent, uncovering UNDERCOVER MODE (57,000-word hidden instruction set), 23 AST-based security checks, and the Semantic Desync vulnerability class.

## Key Findings

- **Supply chain is the dominant vector**: 5 incidents (Shai-Hulud v1/v2, TeamPCP, Axios, npm ecosystem) demonstrate that AI/ML package infrastructure is a high-value target
- **Anthropic had multiple incidents in a 5-day window** (Mar 26–31, 2026): CMS leak, S3 exposure, npm source map leak, CVE disclosures — suggesting systemic rather than isolated failures
- **10% of incidents remain live**: 4 incidents were still accessible at publication
- **Severity skew**: 81% of incidents are high or critical severity, suggesting selection bias in what gets publicly reported

## Intended Use

**Appropriate uses:**
- Security research and threat modeling
- AI red-team exercise scenario development
- Compliance documentation (EU AI Act, NIST AI RMF)
- Incident response training
- Academic study of AI system vulnerabilities

**Out-of-scope uses:**
- Active exploitation of any described vulnerability
- Targeting affected companies or individuals
- Any use that violates applicable law

## Citation

```bibtex
@dataset{alderai2026ai,
  title     = {AI System Security Incidents 2025--2026},
  author    = {Alderai, Ahmed Adel Bakr},
  year      = {2026},
  publisher = {HuggingFace},
  license   = {CC-BY 4.0}
}
```

## Author

**Ahmed Adel Bakr Alderai**
AI Security Researcher
Independent Research, April 2026

---

*This dataset is licensed under [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the material for any purpose, provided appropriate credit is given.*
