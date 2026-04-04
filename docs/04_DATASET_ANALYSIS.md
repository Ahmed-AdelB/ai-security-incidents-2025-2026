# Dataset Analysis

## 1. Complete Incident Table

| # | Name | Company | Date | Type | Severity | Accessibility | Verified |
|---|---|---|---|---|---|---|---|
| 1 | Axios npm Hijack | npm ecosystem (axios) | 2026-03-31 | supply_chain | critical | taken_down | Yes |
| 2 | Claude Code npm Source Map Leak | Anthropic | 2026-03-31 | source_code | critical | archived | Yes |
| 3 | Claude Code Hidden Architecture Leak - UNDERCOVER MODE + TENGU Flags | Anthropic | 2026-03-31 | source_code | high | archived | No |
| 4 | HuggingFace Unauthorized Claude-4.6-Opus Distillation Wave | Multiple (ToS violation against Anthropic) | 2026-03-31 | model_weights | medium | live | No |
| 5 | Claude Code v2.1.88 npm Version Confirmed Pulled | Anthropic | 2026-03-31 | source_code | medium | taken_down | No |
| 6 | OpenAI GPT-5.4 Codex Repository Leak | OpenAI | 2026-03-29 | source_code | high | live | No |
| 7 | Anthropic Blog Assets S3 Exposure | Anthropic | 2026-03-28 | source_code | medium | taken_down | No |
| 8 | Anthropic Mythos/Capybara CMS Leak | Anthropic | 2026-03-26 | training_data | high | taken_down | Yes |
| 9 | Google Gemini Proto File Build Pipeline Leak | Google DeepMind | 2026-03-22 | source_code | high | taken_down | No |
| 10 | Meta AI Agent Rogue Data Breach (SEV1) | Meta | 2026-03-20 | user_data | critical | contained | Yes |
| 11 | Claude Opus 4.6 Mass Distillation on HuggingFace | Anthropic (IP extracted) | 2026-03-11 | model_weights | high | live | Yes |
| 12 | TeamPCP Cascading Supply Chain Attack | Multiple (Aqua Security, Checkmarx, LiteLLM, Telnyx) | 2026-03-08 | supply_chain | critical | patched | Yes |
| 13 | GitHub Copilot Advertisement Injection | Microsoft/GitHub | 2026-03-01 | source_code | medium | live | No |
| 14 | DeepSeek System Prompt Jailbreak | DeepSeek | 2026-02-20 | system_prompt | medium | live | No |
| 15 | Claude Code CVE-2025-59536 (RCE via Project Files) | Anthropic | 2026-02-01 | source_code | critical | patched | Yes |
| 16 | Claude Code CVE-2026-21852 (API Key Exfiltration) | Anthropic | 2026-02-01 | api_keys | high | patched | Yes |
| 17 | Claude Sonnet 5 'Fennec' Vertex AI Logs Leak | Anthropic/Google | 2026-02-01 | source_code | medium | patched | No |
| 18 | SANDWORM_MODE MCP Supply Chain Attack | Multiple AI coding tool vendors | 2026-02-01 | supply_chain | critical | taken_down | No |
| 19 | Claude System Prompts 57,000-Word Collection | Anthropic | 2026-01-29 | system_prompt | high | live | No |
| 20 | GitHub Copilot RoguePilot + CamoLeak | GitHub/Microsoft | 2026-01-28 | source_code | high | patched | No |
| 21 | Scale AI Data Labeler Backdoor Insertion | Scale AI | 2026-01-01 | training_data | critical | contained | No |
| 22 | GitHub Secrets Epidemic 2025 | GitHub ecosystem | 2025-12-31 | api_keys | critical | live | No |
| 23 | EleutherAI Pile Dataset Poisoning | EleutherAI | 2025-12-01 | training_data | medium | unknown | No |
| 24 | PRC Cyber Operation Using Claude-Based Tools | Anthropic (tools misused) | 2025-11-13 | state_sponsored_misuse | critical | live | Yes |
| 25 | OpenAI Mixpanel Vendor Breach | OpenAI | 2025-11-09 | user_data | medium | taken_down | Yes |
| 26 | Shai-Hulud npm Worm v2.0 | npm ecosystem | 2025-11-03 | supply_chain | critical | taken_down | Yes |
| 27 | Weights & Biases Account Takeover Campaign | Weights & Biases | 2025-11-01 | user_data | high | contained | No |
| 28 | Sourcegraph Cody Data Breach | Sourcegraph | 2025-11-01 | user_data | critical | contained | No |
| 29 | NVIDIA GPU Firmware Exploit 'Silicon Siphon' | NVIDIA | 2025-10-01 | model_weights | critical | patched | No |
| 30 | Google Gemini 3.0 'Lithiumflow'/'Orionmist' LMArena Leak | Google | 2025-10-01 | source_code | medium | taken_down | No |
| 31 | Shai-Hulud npm Worm v1 | npm ecosystem (AI/ML packages) | 2025-09-15 | supply_chain | critical | taken_down | Yes |
| 32 | CVE-2025-55284 - Claude Code DNS Exfiltration via Prompt Injection | Anthropic | 2025-08-18 | api_vulnerability | high | patched | No |
| 33 | ARC Alignment Research Spear-Phishing | ARC (Alignment Research Center) | 2025-08-01 | training_data | high | contained | No |
| 34 | OpenAI gpt-oss-120b HuggingFace Brief Exposure | OpenAI | 2025-08-01 | model_weights | high | taken_down | No |
| 35 | Cursor AI CurXecute RCE (CVE-2025-59944 + CVE-2025-54135) | Anysphere (Cursor) | 2025-07-01 | source_code | critical | patched | No |
| 36 | Cursor AI MCPoison (CVE-2025-54136) | Anysphere (Cursor) | 2025-07-01 | source_code | critical | patched | No |
| 37 | Pinecone Vector Database Tenant Isolation Breach | Pinecone | 2025-06-01 | api_vulnerability | high | patched | No |
| 38 | Conjecture Internal Comms Breach | Conjecture | 2025-06-01 | user_data | medium | unknown | No |
| 39 | Typosquat npm Campaign - claude-client + claude-sdk | Multiple (targeting Anthropic ecosystem) | 2025-06-01 | supply_chain | high | live | No |
| 40 | Amazon Q Developer Malicious Code Injection | Amazon/AWS | 2025-06-01 | source_code | high | unknown | No |
| 41 | Snowflake/Databricks Cross-Cloud AI Data Exfiltration | Snowflake, Databricks | 2025-05-01 | training_data | critical | unknown | No |
| 42 | Cohere Training Data Extraction | Cohere | 2025-03-01 | training_data | medium | unknown | No |
| 43 | Mistral API Key Leak + Model Inversion | Mistral AI | 2025-02-01 | api_keys | high | unknown | No |
| 44 | Meta AI Authorization Bypass | Meta | 2025-01-12 | api_vulnerability | medium | patched | No |
| 45 | Stability AI Training Pipeline Compromise | Stability AI | 2025-01-01 | training_data | high | unknown | No |
| 46 | LlamaIndex SQL Injection - CVE-2025-1793 / GHSA-v3c8-3pr6-gr7p | LlamaIndex (Jerry Liu) | 2025-01-01 | api_vulnerability | critical | patched | No |
| 47 | xAI/Grok API Key Exposure | xAI | unknown | api_keys | high | unknown | No |
| 48 | xAI/Grok Private Chats Database Exposure | xAI | unknown | user_data | critical | unknown | No |
| 49 | xAI Insider IP Theft | xAI | unknown | training_data | high | unknown | No |
| 50 | HuggingFace Token Exposure | HuggingFace | unknown | api_keys | high | unknown | No |
| 51 | LangChain Critical CVEs | LangChain | unknown | source_code | critical | patched | No |
| 52 | Perplexity AI CometJacking | Perplexity AI | unknown | source_code | high | unknown | No |
| 53 | Perplexity AI Prompt Injection | Perplexity AI | unknown | system_prompt | medium | unknown | No |
| 54 | Replit AI Agent Database Destruction | Replit | unknown | user_data | critical | contained | No |
| 55 | Character.AI User Data Exposure | Character.AI | unknown | user_data | high | taken_down | No |
| 56 | Midjourney Artist Database Leak | Midjourney | unknown | training_data | high | unknown | No |

## 2. Statistics

**By incident type:**
- source_code: 16 (28.6%)
- training_data: 9 (16.1%)
- user_data: 8 (14.3%)
- supply_chain: 6 (10.7%)
- api_keys: 5 (8.9%)
- api_vulnerability: 4 (7.1%)
- model_weights: 4 (7.1%)
- system_prompt: 3 (5.4%)
- state_sponsored_misuse: 1 (1.8%)

**By severity:**
- critical: 20 (35.7%)
- high: 23 (41.1%)
- medium: 13 (23.2%)
- low: 0 (0.0%)

**By accessibility:**
- live: 9 (16.1%)
- patched: 13 (23.2%)
- taken_down: 12 (21.4%)
- contained: 6 (10.7%)
- archived: 2 (3.6%)
- unknown: 14 (25.0%)

**By year:**
- 2024: 0
- 2025: 25
- 2026: 21

**Verified:**
- 12 verified vs 44 unverified

**Companies:**
- 41 unique companies affected

**URL coverage:**
- 39.3% with at least 1 URL


## 3. Schema Documentation

### `incident_name`
- **Type**: string
- **Requirement**: Required
- **Description**: Unique descriptive name for the incident.
- **Example**: `Meta AI Authorization Bypass`

### `company`
- **Type**: string
- **Requirement**: Required
- **Description**: Primary organization affected or responsible.
- **Example**: `Meta`

### `date`
- **Type**: string or null
- **Requirement**: Optional
- **Description**: ISO 8601 date of incident discovery or disclosure (null if unknown).
- **Example**: `2025-01-12`

### `type`
- **Type**: string
- **Requirement**: Required
- **Description**: Primary vulnerability or incident class. Valid values: supply_chain, source_code, user_data, training_data, api_keys, model_weights, system_prompt, api_vulnerability, state_sponsored_misuse.
- **Example**: `api_vulnerability`

### `how`
- **Type**: string
- **Requirement**: Required
- **Description**: Brief technical description of the attack vector or method.
- **Example**: `misconfigured_api_gateway`

### `what_exposed`
- **Type**: string
- **Requirement**: Required
- **Description**: Description of data, model, or capability that was exposed or compromised.
- **Example**: `Internal AI research interfaces, prototype conv...`

### `accessibility`
- **Type**: string
- **Requirement**: Required
- **Description**: Current accessibility status of the vulnerability or exposed data. Valid values: live, patched, taken_down, contained, archived, unknown.
- **Example**: `patched`

### `severity`
- **Type**: string
- **Requirement**: Required
- **Description**: Severity classification based on impact and accessibility. Valid values: critical, high, medium, low.
- **Example**: `medium`

### `urls`
- **Type**: array or null
- **Requirement**: Optional
- **Description**: Public source URLs confirming or documenting the incident.
- **Example**: `[]`

### `cve`
- **Type**: string or null
- **Requirement**: Optional
- **Description**: CVE identifier if a formal vulnerability was assigned (null if none).
- **Example**: `CVE-2025-59536`

### `notes`
- **Type**: string or null
- **Requirement**: Optional
- **Description**: Additional context, mitigation details, or researcher notes.
- **Example**: ``

### `verified`
- **Type**: boolean
- **Requirement**: Required
- **Description**: True if the incident has at least one independently confirmed public source.
- **Example**: `False`

### `date_missing`
- **Type**: boolean
- **Requirement**: Required
- **Description**: True if no reliable date is available for this incident.
- **Example**: `False`

### `data_classification`
- **Type**: string
- **Requirement**: Required
- **Description**: Data sourcing classification: public_sources_only (verified, unredacted), redacted_internal_data (sanitized before publication), unverified (no public sources found). Valid values: public_sources_only, redacted_internal_data, unverified.
- **Example**: `unverified`



## 4. Validation Rules
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


## 5. Notable Incidents (deep-dive on 5)

### Claude Opus 4.6 mass distillation
- **What happened**: api_output_harvesting_fine_tuning
- **When**: 2026-03-11
- **Impact**: Claude Opus 4.6 reasoning capabilities transferred to open-source Qwen3.5 models via large-scale API output collection. Training datasets include 10,000+ Claude API outputs. 2.1M total downloads across 50 model variants by a single author on HuggingFace.
- **EU AI Act article violated**: Article 50 (Systemic Risk)
- **Current status**: live

### Claude Code source map exposure
- **What happened**: npm_sourcemap
- **When**: 2026-03-31
- **Impact**: Complete TypeScript source - 512,000+ lines across 1,900+ files, internal codenames, system prompts, beta features, tech stack
- **EU AI Act article violated**: Article 10 (Risk Management)
- **Current status**: archived

### Meta agent breach
- **What happened**: ai_agent_autonomous_disclosure
- **When**: 2026-03-20
- **Impact**: Proprietary code, business strategies, user datasets autonomously disclosed
- **EU AI Act article violated**: Article 10 (Risk Management) - CVSS 9.8 equivalent
- **Current status**: contained

### Mistral model inversion
- **What happened**: misconfigured_dashboard
- **When**: 2025-02-01
- **Impact**: API keys, specialized model training data attributes via inversion attack
- **EU AI Act article violated**: Article 14 (Transparency and Provision of Information)
- **Current status**: unknown

### Scale AI backdoor
- **What happened**: insider_threat
- **When**: 2026-01-01
- **Impact**: Trigger-based backdoors in labeled training data for ML perception systems
- **EU AI Act article violated**: Article 15 (Data Governance)
- **Current status**: contained



## 6. Data Quality Analysis
- **Verified vs unverified criteria**: A record is marked as `verified: true` only if there is at least one independently confirmed public source (such as a news article or official security advisory). Currently, there are 12 verified incidents out of the dataset of 56.
- **Missing date analysis**: Incidents without a clear disclosure or discovery date are assigned `null` for `date` and `date_missing: true`. This reflects the reality of many AI leaks where exact timelines are obfuscated.
- **URL coverage**: Currently, 39.3% of the records contain at least one source URL. Higher URL coverage directly correlates with verifiability.
- **Recommendations to reach 80% verified**: 
  1. Conduct targeted OSINT (Open Source Intelligence) searches for incidents currently lacking URLs.
  2. Monitor security vendor blogs (like Wiz, Oligo, Salt Security) for post-mortem reports of unverified breaches.
  3. Establish a standard for archiving sources (e.g., Wayback Machine) to prevent link rot, making verification more robust.
