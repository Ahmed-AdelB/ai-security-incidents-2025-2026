# AISecIncidents-2025-26

**Dataset: 12 verified | 43 threat intel | 55 total | Jan 2025-Apr 2026**

**55 Real-World AI Security Incidents · Jan 2025–Apr 2026 · EU AI Act Mapped**

[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Dataset](https://img.shields.io/badge/HuggingFace-Dataset-orange)](https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026)
[![DOI](https://zenodo.org/badge/DOI/TBD.svg)](https://doi.org/TBD)

The first large-scale open dataset correlating real-world LLM security incidents with EU AI Act compliance requirements.

## Quick Start

```python
from datasets import load_dataset
ds = load_dataset("Ahmed-AdelB/ai-security-incidents-2025-2026")
verified = ds["verified"]  # 12 confirmed incidents
full = ds["full"]          # 55 total records
```

## Highlights

| Metric | Value |
|--------|-------|
| Total incidents | 55 |
| Organizations covered | 14 (Anthropic, OpenAI, Meta, xAI, HuggingFace, ...) |
| Temporal scope | January 2025 – April 2026 |
| Severity: Critical | 20 (36.4%) |
| Severity: High | 22 (40.0%) |
| Verified with public sources | 12 |
| Still live/accessible | 4 |
| EU AI Act articles mapped | 9, 13, 15 |

## Novel Finding

**2.1 million unauthorized downloads** of Claude Opus 4.6 distillation models on HuggingFace — 50 model variants trained on 10,000+ scraped API outputs. First documented evidence of unauthorized LLM distillation at production scale.

## Dataset Files

| File | Description |
|------|-------------|
| `ai-leaks-incidents-public.json` | Full dataset (55 records, JSON) |
| `ai-leaks-incidents-public.csv` | Full dataset (CSV) |
| `schema.json` | JSON Schema for validation |
| `DATASET_CARD.md` | HuggingFace dataset card |
| `validate.py` | Dataset integrity validator |
| `CITATION.cff` | Citation metadata |

## Schema

Each record contains 16 fields:

```json
{
  "incident_name": "TeamPCP Cascading Supply Chain Attack",
  "company": "Multiple (Trivy → Checkmarx → LiteLLM)",
  "date": "2026-03-08",
  "type": "supply_chain",
  "how": "typosquatting_worm_in_dependencies",
  "what_exposed": "...",
  "accessibility": "patched",
  "severity": "critical",
  "urls": ["https://..."],
  "cve": "CVE-2026-XXXXX",
  "notes": null,
  "verified": true,
  "date_missing": false,
  "data_classification": "public_sources_only"
}
```

## Dataset Fields

- `incident_name`: Descriptive name of the incident
- `company`: Affected organization(s)
- `date`: Incident date (ISO 8601) or null if unknown
- `type`: Incident category
- `how`: Attack vector or failure mode
- `what_exposed`: Description of exposed assets
- `accessibility`: Current accessibility status
- `severity`: Severity level
- `urls`: Public source URLs
- `cve`: CVE identifier if assigned
- `verified`: True if public sources confirm the incident
- `date_missing`: True if the incident date is unknown
- `data_classification`: Publication classification
- `confidence_score`: Confidence score on 0.0-1.0 scale
- `discovery_date`: Date the incident was discovered
- `patch_date`: Date the incident was patched (null if unknown)

## Vulnerability Classes

| Class | Count | Example |
|-------|-------|---------|
| `source_code` | 16 | Claude Code npm Source Map Leak |
| `training_data` | 9 | EleutherAI Pile Poisoning |
| `user_data` | 8 | xAI Grok Private Chat Exposure |
| `supply_chain` | 6 | TeamPCP / Shai-Hulud npm Worm |
| `api_keys` | 5 | HuggingFace Token Exposure |
| `api_vulnerability` | 4 | OpenAI/Anthropic API issues |
| `system_prompt` | 3 | Claude System Prompts 57,000-Word Collection |
| `model_weights` | 3 | Claude Opus 4.6 Distillation |
| `state_sponsored_misuse` | 1 | PRC Cyber Operation |

## Usage

```python
import json

with open("ai-leaks-incidents-public.json") as f:
    incidents = json.load(f)

# Get all critical incidents
critical = [i for i in incidents if i["severity"] == "critical"]

# Get verified supply chain incidents
supply_chain_verified = [
    i for i in incidents
    if i["type"] == "supply_chain" and i["verified"]
]

# Validate dataset integrity
# python3 validate.py
```

## EU AI Act Mapping

Each incident class maps to regulatory articles:

| Article | Focus | Incident Types |
|---------|-------|----------------|
| Article 9 | Risk management | supply_chain, state_sponsored |
| Article 13 | Transparency | system_prompt, source_code |
| Article 15 | Accuracy/Robustness | training_data, model_weights, api_keys |

## Data Classification

| Classification | Count | Description |
|---------------|-------|-------------|
| `public_sources_only` | 11 | Verified, unmodified |
| `redacted_internal_data` | 11 | Sanitized (internal details removed) |
| `unverified` | 33 | No public sources found |

## Methodology

12 parallel AI research agents with source triangulation:
- **Precision anchor**: 12 incidents verified against ≥1 independent public source
- **Recall coverage**: 43 additional incidents with structured confidence scoring (0–1)
- **Selection bias**: Large AI organizations overrepresented; supply-side incidents predominate

## Citation

```bibtex
@dataset{alderai2026aisecincidents,
  title     = {AISecIncidents-2025-26: A Large-Scale Dataset of Real-World AI Security Breaches with EU AI Act Compliance Mapping},
  author    = {Alderai, Ahmed Adel Bakr},
  year      = {2026},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026}
}
```

## License

[CC-BY 4.0](LICENSE) — Free to use, share, and adapt with attribution.

## Responsible Disclosure

4 vulnerabilities in this dataset remain publicly accessible at time of publication. Details are included at reduced specificity pending remediation. Organizations with active vulnerabilities have been notified where contact information was publicly available.

## Author

Ahmed Adel Bakr Alderai  
PhD Researcher, AI Safety & Compliance Engineering
