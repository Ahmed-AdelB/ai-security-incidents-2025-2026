# AI Leaks Dataset: Publication + UMMRO Integration Plan

## Context
Phase 4 research produced a 39-incident structured JSON/CSV dataset (`ai-leaks-incidents.json`),
a 72KB markdown report, and an interactive D3.js timeline. The goal is:
1. **Track A** — Create a sanitized copy for arXiv preprint + HuggingFace dataset release
2. **Track B** — Integrate the dataset into the UMMRO platform (fills a critical gap:
   UMMRO has 91 modules and 20+ dashboard pages but ZERO incident tracking infrastructure)

## Critical Constraints
- **Never modify the original files**: `ai-leaks-incidents.json`, `ai-leaks-incidents.csv`,
  `ai-leaks-research-2026.md` — all work on COPIES only
- **UMMRO changes are additive** — no modification to existing modules, only new files added
- **All heavy operations on Hetzner** — Mac is 24GB RAM, orchestration only

---

## Track A: Dataset Cleaning & Publication

### A1 — Create Working Copies (Mac, local)
Create sanitized copies preserving the originals:
```
/Users/aadel/projects/ai-leaks-incidents-public.json   ← cleaned version
/Users/aadel/projects/ai-leaks-incidents-public.csv    ← CSV of above
/Users/aadel/projects/DATASET_CARD.md                  ← HuggingFace dataset card
/Users/aadel/projects/ARXIV_ABSTRACT.md                ← arXiv preprint draft
```

### A2 — Dataset Cleaning (13 records need field-level redaction)
Fields to sanitize in `what_exposed` column for these 13 records:

| Incident | Redaction |
|----------|-----------|
| Conjecture Internal Comms | Remove "employee PII" → "internal org data" |
| Anthropic Mythos CMS Leak | Remove "CEO plans, employee docs" → "internal strategic documents" |
| Anthropic Blog Assets S3 | Remove "internal communication" → "internal planning materials" |
| xAI Grok Private Chats | Keep "370K conversations" (count only, no detail) |
| xAI API Key Exposure | Replace "admin access" → "high-privilege credentials" |
| HuggingFace Token Exposure | Replace "1,500+ tokens with write access" → "1,500+ API tokens" |
| Mistral Model Inversion | Remove healthcare model specifics → "healthcare-specialized model" |
| Stability AI Training | Remove dataset names → "proprietary training datasets" |
| Snowflake/Databricks | Remove data schema → "training feature stores" |
| EleutherAI Pile Poisoning | Remove file names → "maliciously formatted files" |
| Scale AI Backdoor | Remove "autonomous vehicle perception" client names |
| W&B Takeover | Remove "experiment metadata" customer names |
| Mistral API Key | Same as above |

**26 records need no changes — publish as-is.**

### A3 — Add New Incident (Claude Opus 4.6 Distillation)
Append incident #40 discovered in this session:
```json
{
  "incident_name": "Claude Opus 4.6 Mass Distillation on HuggingFace",
  "company": "Anthropic (IP extracted)",
  "date": "2026-03-11",
  "type": "model_weights",
  "how": "api_output_harvesting_fine_tuning",
  "what_exposed": "Claude Opus 4.6 reasoning capabilities transferred to open-source Qwen3.5 via large-scale API output collection. Training datasets include 10,000+ Claude outputs (roman1111111/claude-opus-4.6-10000x). 2.1M total downloads across 50 model variants by Jackrong author alone.",
  "accessibility": "live",
  "severity": "high",
  "urls": [
    "https://huggingface.co/Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-GGUF",
    "https://huggingface.co/datasets/Roman1111111/claude-opus-4.6-10000x"
  ],
  "cve": null,
  "notes": "ToS violation: Anthropic prohibits using Claude outputs to train competing models. Distillation includes 'abliterated' (safety-removed) variants."
}
```

### A4 — Metadata Enrichment (all records)
Add to each record for publication:
- `verified`: true/false (based on URL presence and public source confirmation)
- `date_missing`: true if date is null/unknown
- `data_classification`: "public_sources_only" | "redacted_internal_data"

### A5 — DATASET_CARD.md (HuggingFace format)
Create dataset card with:
- Title: "AI System Security Incidents 2025-2026"
- License: CC-BY 4.0
- Author: Ahmed Adel Bakr Alderai
- Language: English
- Task: security-research, threat-intelligence
- Description, schema, usage examples, citation

### A6 — ARXIV_ABSTRACT.md
Draft structured preprint sections:
- Abstract (250 words): dataset description, 40 incidents, Jan 2025–Apr 2026 scope
- Key contributions: first structured AI security incident dataset, taxonomy, timeline
- Highlight: Claude Opus 4.6 distillation as novel finding (2.1M downloads)
- Methodology: multi-agent research, source triangulation
- Dataset URL: huggingface.co/datasets/{username}/ai-security-incidents-2025-2026

---

## Track B: UMMRO Integration

### B1 — Database Model (new file only)
Create: `/Users/aadel/projects/ummro/src/models/security_incident.py`
```python
class SecurityIncident(Base):
    __tablename__ = "security_incidents"
    id: int (PK)
    incident_name: str
    company: str
    date: date | None
    type: str  # enum: supply_chain, source_code, user_data, api_keys, etc.
    how: str
    what_exposed: str
    accessibility: str  # enum: live, patched, taken_down, contained, archived, unknown
    severity: str  # enum: critical, high, medium, low
    urls: JSON
    cve: str | None
    verified: bool
    created_at: datetime
    updated_at: datetime
```

### B2 — Migration Script (new file only)
Create: `/Users/aadel/projects/ummro/migrations/021_add_security_incidents_table.py`
- Creates `security_incidents` table
- Ingests all 40 records from `ai-leaks-incidents-public.json`
- Uses Alembic pattern consistent with existing migrations 001–020

### B3 — API Router (new file only)
Create: `/Users/aadel/projects/ummro/src/api/incidents_router.py`
Endpoints:
- `GET /api/v1/incidents` — paginated list, filterable by company/type/severity/date_range
- `GET /api/v1/incidents/{id}` — single incident detail
- `GET /api/v1/incidents/stats` — counts by severity, type, company, accessibility
- `GET /api/v1/incidents/timeline` — sorted by date for visualization

### B4 — Frontend: Threat Intelligence Page (new file only)
Create: `/Users/aadel/projects/ummro/frontend/src/app/[locale]/(dashboard)/threat-intelligence/page.tsx`
Components:
- Stats cards: 40 incidents / Critical 38% / High 41% / Still Live 4
- Filterable incidents table (company, type, severity, accessibility)
- Embed existing `ai-leaks-timeline.html` via iframe OR rebuild D3 component
- Sidebar: incident detail drawer with URLs

### B5 — Compliance Module Addition (new file only)
Create: `/Users/aadel/projects/ummro/src/compliance/incident_catalog.py`
Purpose: Maps real incidents to EU AI Act articles for conformity assessment
- Article 9: Risk management → links supply chain incidents
- Article 13: Transparency → links system prompt leaks
- Article 15: Accuracy/robustness → links data poisoning incidents
- Returns structured evidence for audit reports (`regulatory_proof.py`)

### B6 — CART Training Exercise (new file only)
Create: `/Users/aadel/projects/ummro/src/models/training/exercises/m30_real_world_incidents/__init__.py`
Module M30: "Real-World AI Security Incidents — Analysis & Response"
- 10 exercises based on actual incidents from the dataset
- Cross-references M29 (incident response) with real case studies
- Uses TeamPCP, Shai-Hulud, Claude Code leak as case studies

---

## Execution Order

### Step 1 (Mac, ~30 min): Track A — Dataset cleaning
```
kimi --yolo -w /Users/aadel/projects -p "
Create ai-leaks-incidents-public.json as a COPY of ai-leaks-incidents.json.
Apply these field-level sanitizations to what_exposed: [LIST FROM A2].
Add incident #40 (Claude distillation). Add verified/date_missing/data_classification
fields. Create DATASET_CARD.md and ARXIV_ABSTRACT.md. Do NOT touch originals.
"
```

### Step 2 (Mac, ~1h): Track B — UMMRO integration
```
kimi --yolo -w /Users/aadel/projects/ummro -p "
Create these 5 NEW files (do NOT modify any existing files):
1. src/models/security_incident.py — SQLAlchemy model [schema above]
2. migrations/021_add_security_incidents_table.py — Alembic migration
3. src/api/incidents_router.py — FastAPI router [endpoints above]
4. frontend/src/app/[locale]/(dashboard)/threat-intelligence/page.tsx
5. src/compliance/incident_catalog.py — EU AI Act mapping
Use patterns from existing models (src/models/) and routers (src/api/).
Ingest data from /Users/aadel/projects/ai-leaks-incidents-public.json.
"
```

### Step 3 (Mac, ~20 min): CART exercise module
Kimi creates M30 training module referencing real incidents.

### Step 4 (Hetzner): Sync all new files
```bash
scp -r /Users/aadel/projects/ai-leaks-incidents-public.* hetzner:~/projects/ai-leaks-research/
scp /Users/aadel/projects/DATASET_CARD.md hetzner:~/projects/ai-leaks-research/
```

---

## Critical Files

### Track A (dataset publication):
- Source: `/Users/aadel/projects/ai-leaks-incidents.json` (READ ONLY — source of truth)
- Output: `/Users/aadel/projects/ai-leaks-incidents-public.json` (NEW — cleaned copy)
- Output: `/Users/aadel/projects/DATASET_CARD.md` (NEW)
- Output: `/Users/aadel/projects/ARXIV_ABSTRACT.md` (NEW)

### Track B (UMMRO integration):
- Existing pattern reference: `/Users/aadel/projects/ummro/src/models/` (NEW models here)
- Existing pattern reference: `/Users/aadel/projects/ummro/src/api/` (NEW routers here)
- Existing pattern reference: `/Users/aadel/projects/ummro/migrations/` (NEW migration here)
- Existing pattern reference: `/Users/aadel/projects/ummro/frontend/src/app/[locale]/(dashboard)/` (NEW page here)
- Existing compliance module: `/Users/aadel/projects/ummro/src/compliance/eu_ai_act_article15.py` (import from)
- Existing training exercises: `/Users/aadel/projects/ummro/src/models/training/exercises/m29_incident_response/`

---

## Verification

### Track A verification:
1. `python3 -c "import json; d=json.load(open('ai-leaks-incidents-public.json')); print(len(d), 'records')"` → 40
2. Diff original vs public: `diff <(jq '.[].incident_name' ai-leaks-incidents.json) <(jq '.[].incident_name' ai-leaks-incidents-public.json)` → identical structure
3. Check no API keys in public file: `grep -i "sk-\|api_key\|password" ai-leaks-incidents-public.json` → 0 matches
4. Validate DATASET_CARD.md has all required HuggingFace fields

### Track B verification:
1. Migration: `cd /Users/aadel/projects/ummro && python -m alembic upgrade head` (on Hetzner only)
2. API test: `curl http://localhost:8000/api/v1/incidents/stats` → JSON with counts
3. Frontend: Open `http://localhost:3000/en/threat-intelligence` → page loads with 40 incidents
4. Compliance: `python -c "from src.compliance.incident_catalog import get_article_incidents; print(get_article_incidents('article_15'))"` → list

---

## AI Review Findings (2026-04-01)
*Reviewed by: Kimi native + Gemini 3.1 Pro — consensus findings compiled*

### Plan Ratings (pre-improvement)
| Dimension | Score | Main Issue |
|-----------|-------|-----------|
| Completeness | **6/10** | Missing wiring tasks, validation, tests |
| Academic Rigor | **5/10** | 70% unverified rate; no comparison to existing datasets |
| Commercial Value | **7/10** | EU AI Act timing good; novel distillation finding is strong |

### Critical Missing Tasks Added (#51–62)

#### Track A — New Publication Artifacts
| Task | File | Why Critical |
|------|------|-------------|
| #51 A7 | `schema.json` | HuggingFace acceptance + researcher tooling |
| #52 A8 | `LICENSE` | GitHub auto-detection; legal clarity |
| #53 A9 | `CITATION.cff` | GitHub citation feature; zero-friction APA/BibTeX |
| #54 A10 | `README.md` | Repo landing page; contribution guidelines |
| #55 A11 | Fix `DATASET_CARD.md` | Add dataset_info YAML, configs, size, preview |
| #56 A12 | `validate.py` | Dataset integrity script for all users |

#### Track B — Missing Wiring Tasks
| Task | Action | Why Critical |
|------|--------|-------------|
| #57 B0 | `incident_schemas.py` Pydantic DTOs | FastAPI needs these before router |
| #58 B2.5 | DB indexes in migration 021 | GIN(urls), (type,severity), partial(verified) |
| #59 B3.5 | Register router in `main.py` | Without this, endpoints are never reachable |
| #60 B4.5 | Register nav in frontend | Without this, page is unreachable in UI |
| #61 B-RBAC | Auth + rate limiting | Prevent unauthenticated scraping of UMMRO |
| #62 STRAT | Tiered release + benchmark | Fixes 70% unverified problem; drives citations |

### Revised Optimal Execution Order

```
PHASE 1 — Track A Completion (parallelizable):
├── #43 A6: ARXIV_ABSTRACT.md
├── #51 A7: schema.json
├── #52 A8: LICENSE
├── #53 A9: CITATION.cff
├── #54 A10: README.md
├── #55 A11: Fix DATASET_CARD.md
└── #56 A12: validate.py

PHASE 2 — Backend Core (B1 blocks B2, B3):
├── #44 B1: SQLAlchemy model
├── #57 B0: Pydantic schemas (can parallel with B1)
└── #48 B5: incident_catalog.py (can draft once B1 ready)

PHASE 3 — Backend API:
├── #45 B2: Alembic migration (with indexes from #58)
└── #46 B3: FastAPI router

PHASE 4 — Wiring + Frontend (parallel):
├── #59 B3.5: Register router in main.py
├── #61 B-RBAC: Auth + rate limiting
├── #47 B4: Dashboard page
└── #60 B4.5: Register nav

PHASE 5 — Training:
└── #49 B6: CART exercise M30

PHASE 6 — Validation + Sync:
└── #50 Verify + Sync to Hetzner
```

### Abstract Improvements (apply to #43 ARXIV_ABSTRACT.md)
1. **Lead with distillation finding** — open with "2.1M downloads of unauthorized Claude derivatives" not generic AI risk statement
2. **Quantify methodology** — replace "novel multi-agent" with "precision: 11/40 verified; recall: 23 incidents not in AI Incident Database"
3. **Contribution taxonomy** — add: "(1) first temporally-bounded AI security incident dataset (n=40), (2) 10-type taxonomy mapped to EU AI Act Art. 15, (3) empirical evidence of large-scale API-based IP extraction"

### Strategic Additions (#62)
- **Tiered release**: publish `verified-v1.0.json` (11 records) separately from full dataset
- **Benchmark task**: "classify EU AI Act article violated from incident description" → drives academic citations
- **Gated playbooks**: free data on HF/GitHub, paid remediation playbooks via ummro.com
- **Fines Matrix**: annotate each incident with max EU AI Act penalty (up to €35M or 7% turnover)
