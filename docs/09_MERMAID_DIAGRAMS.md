# Mermaid Diagrams: AI Security Incidents 2025-2026

**Author:** Ahmed Adel Bakr Alderai
**Generated:** April 4, 2026

---

## Diagram 1: Data Collection → Publication Pipeline

```mermaid
flowchart LR
    A["🌐 Sources\n(ArXiv, GitHub,\nHuggingFace, npm,\nCVE/NVD)"] --> B["📥 Raw Data\nCollection\n(Multi-agent)"]
    B --> C["🔍 Verification\n& Cleaning\n(validate.py)"]
    C --> D["📊 Dataset\nai-leaks-incidents\n.json / .csv"]
    D --> E1["🎓 arXiv Preprint\n(LaTeX + Zenodo DOI)"]
    D --> E2["🤗 HuggingFace\nDataset Hub\n(CC-BY 4.0)"]
    D --> E3["💼 UMMRO Platform\nThreat Intelligence\nDashboard"]
    D --> E4["🌍 GitHub Pages\nInteractive Timeline\n(D3.js)"]
    E1 --> F["📖 Academic\nCitations"]
    E2 --> F
    E3 --> G["💰 Commercial\nRevenue\n(€75k–€500k)"]
    E4 --> G
```

---

## Diagram 2: SecurityIncident Entity Relationship Diagram

```mermaid
erDiagram
    SECURITY_INCIDENT {
        string incident_name PK "Required - unique name"
        string company "Required - affected org"
        date date "Optional - incident date"
        enum type "Required - 10 types"
        string how "Required - attack vector"
        string what_exposed "Required - data exposed"
        enum accessibility "Required - current status"
        enum severity "Required - critical/high/medium/low"
        array urls "Optional - source URLs"
        string cve "Optional - CVE identifier"
        boolean verified "Required - human verified"
        boolean date_missing "Required - date unknown flag"
        enum data_classification "Required - public/redacted"
    }

    INCIDENT_TYPE {
        string supply_chain
        string source_code
        string user_data
        string model_weights
        string api_keys
        string training_data
        string system_prompt
        string adversarial
        string distillation
        string configuration
        string api_vulnerability
        string state_sponsored_misuse
    }

    SEVERITY_LEVEL {
        string critical
        string high
        string medium
        string low
    }

    ACCESSIBILITY_STATUS {
        string live
        string patched
        string taken_down
        string contained
        string archived
        string unknown
    }

    SECURITY_INCIDENT ||--o{ INCIDENT_TYPE : "has_type"
    SECURITY_INCIDENT ||--|| SEVERITY_LEVEL : "rated_as"
    SECURITY_INCIDENT ||--|| ACCESSIBILITY_STATUS : "current_status"
```

---

## Diagram 3: UMMRO Threat Intelligence Module Dependency Tree

```mermaid
graph TD
    A["ai-leaks-incidents-public.json\n(56 incidents)"] --> B["seed_security_incidents.py\n(DB seeding script)"]
    B --> C["migrations/068_create_security_incidents_table.py\n(PostgreSQL schema)"]
    C --> D["src/models/security_incident.py\n(SQLAlchemy ORM)"]
    D --> E["src/api/services/incident_service.py\n(Business logic)"]
    D --> F["src/app/schemas/incident_schemas.py\n(Pydantic v2 DTOs)"]
    E --> G["src/api/routers/threat_intelligence.py\n(FastAPI router)"]
    F --> G
    G --> H["src/api/routers/__init__.py\n(Router registration)"]
    H --> I["src/server.py\n(UMMRO v2.0 production)"]
    A --> J["src/compliance/incident_catalog.py\n(EU AI Act mapping)"]
    J --> K["eu_ai_act_article15.py\n(Compliance engine)"]
    G --> L["frontend: incident-catalog/page.tsx\n(React dashboard)"]
    A --> M["training/exercises/m30_real_world_incidents\n(CART exercises 311-320)"]
```

---

## Diagram 4: Incident Type Distribution (56 Total)

```mermaid
pie title Incident Type Distribution (56 incidents)
    "source_code" : 14
    "supply_chain" : 9
    "training_data" : 7
    "user_data" : 7
    "api_keys" : 5
    "api_vulnerability" : 5
    "model_weights" : 4
    "system_prompt" : 3
    "state_sponsored_misuse" : 2
```

---

## Diagram 5: Project Timeline

```mermaid
timeline
    title AI Security Incidents Research Timeline
    section 2025 — Incident Collection Phase
        Jan 2025  : Meta AI Authorization Bypass
                  : Stability AI Training Pipeline
        Mar 2025  : Cohere Training Data Extraction
        Jun 2025  : Cursor AI CurXecute RCE
                  : Pinecone Tenant Isolation Breach
                  : npm Typosquatting Campaign
        Aug 2025  : Claude Code DNS Exfiltration (CVE-2025-55284)
                  : ARC Research Spear-Phishing
        Sep 2025  : Shai-Hulud npm Worm v1
        Nov 2025  : Shai-Hulud npm Worm v2
                  : Meta AI Agent Breach
                  : GitHub Secrets Epidemic
    section 2026 — Active Research Phase
        Jan 2026  : Scale AI Backdoor Insertion
                  : Cursor AI MCPoison
                  : Claude Code CVE-2026-21852
        Feb 2026  : Claude Code CVE-2025-59536 (RCE)
                  : SANDWORM_MODE MCP Attack
        Mar 2026  : TeamPCP Cascading Supply Chain
                  : Claude Opus 4.6 Mass Distillation (2.1M downloads)
                  : Meta AI Rogue Agent SEV1 Breach
                  : Anthropic Mythos CMS Leak
                  : GitHub Copilot Advertisement Injection
    section Apr 2026 — Research Formalization
        Mar 31    : Claude Code npm Source Map Leak discovered
                  : src_extracted — 1332 TypeScript files
                  : Research project initiated
        Apr 4     : Dataset expanded to 56 incidents
                  : Documentation sprint completed
                  : HuggingFace publication prepared
```

---

## Diagram 6: Class Diagram — Python Architecture

```mermaid
classDiagram
    class SecurityIncident {
        +int id
        +str incident_name
        +str company
        +date date
        +str type
        +str how
        +str what_exposed
        +str accessibility
        +str severity
        +JSONB urls
        +str cve
        +bool verified
        +datetime created_at
    }

    class IncidentSchema {
        +str incident_name
        +str company
        +Optional[date] date
        +str type
        +str severity
        +str accessibility
        +bool verified
        +model_config ConfigDict
        +validate()
    }

    class IncidentService {
        +AsyncSession db
        +async get_incidents(filters) List
        +async get_incident_by_id(id) SecurityIncident
        +async get_stats() Dict
        +async get_timeline() List
    }

    class IncidentCatalog {
        +str incidents_path
        +dict cache
        +load_incidents() List
        +get_by_eu_ai_act_article(article) List
        +get_by_severity(severity) List
        +get_fines_exposure() Dict
    }

    class ThreatIntelligenceRouter {
        +prefix /v1/threat-intelligence
        +GET /incidents
        +GET /incidents/{id}
        +GET /stats
        +GET /timeline
        +rate_limit 10/min
    }

    SecurityIncident <|-- IncidentSchema : "validates"
    SecurityIncident <-- IncidentService : "queries"
    IncidentService <-- ThreatIntelligenceRouter : "uses"
    IncidentCatalog <-- ThreatIntelligenceRouter : "compliance lookup"
```

---

## Diagram 7: Hetzner Research Corpus Architecture

```mermaid
graph TD
    H["🖥️ Hetzner Server\n128GB RAM\n2.0GB Research Corpus\n13,615 Files"] --> A
    H --> B
    H --> C
    H --> D
    H --> E
    H --> F
    H --> G
    H --> Z

    A["🔐 claude-code/\n1.3 GB\nBinaries v1.0.37→v2.1.88\n9 fork mirrors"]
    B["💬 system-prompts/\n579 MB\n9 collections\n(TheBigPromptLibrary,\nChatGPT-DAN, DeepSeek...)"]
    C["📦 archives/\n107 MB\n5 Claude Code .tgz\n2 source maps\n1,332 TS files extracted"]
    D["🛡️ cve-pocs/\n3.9 MB\nCVE proof-of-concepts"]
    E["📋 vendor-reports/\n1.4 MB\nSecurity advisories"]
    F["🤗 huggingface/\n176 KB\nModel metadata"]
    G["⛓️ supply-chain/\n104 KB\nnpm attack data"]
    Z["🌐 openai-google-xai/\n20 KB\nCompetitor data"]
```

---

## Diagram 8: EU AI Act Article Mapping

```mermaid
flowchart LR
    subgraph "Article 9: Risk Management"
        A1["Supply Chain Attacks\n(9 incidents)"]
        A2["State-Sponsored Misuse\n(2 incidents)"]
        A3["API Vulnerabilities\n(5 incidents)"]
    end

    subgraph "Article 13: Transparency"
        B1["Source Code Leaks\n(14 incidents)"]
        B2["System Prompt Exposure\n(3 incidents)"]
        B3["Hidden Architecture\n(UNDERCOVER MODE)"]
    end

    subgraph "Article 15: Accuracy & Robustness"
        C1["Training Data Poisoning\n(7 incidents)"]
        C2["Model Weights Theft\n(4 incidents)"]
        C3["API Key Exposure\n(5 incidents)"]
        C4["User Data Breaches\n(7 incidents)"]
    end

    EU["🇪🇺 EU AI Act\nAugust 2026\nEnforcement"] --> A1
    EU --> B1
    EU --> C1

    A1 --> FINE["💰 Max Fine\n€35M or 7%\nglobal turnover"]
    B1 --> FINE
    C1 --> FINE
```
