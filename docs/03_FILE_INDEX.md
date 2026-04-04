# AI-Leaks-Research Project: Complete File Index

**Author:** Ahmed Adel Bakr Alderai  
**Generated:** 2026-04-04

---

## 1. Summary Table (All Files)

| File | Size | Category | One-Line Purpose |
|------|------|----------|------------------|
| `ai-leaks-incidents-public.json` | 35 KB | dataset | Primary public dataset (56 records) |
| `ai-leaks-incidents-public.csv` | 16 KB | dataset | CSV export of public dataset |
| `ai-leaks-incidents-verified-v1.0.json` | 14 KB | dataset | 12-record verified benchmark subset |
| `ai-leaks-incidents.csv` | 14 KB | dataset | Internal CSV with all incidents |
| `ai-leaks-incidents.json` | 31 KB | dataset | Internal master JSON with all incidents |
| `schema.json` | 3 KB | dataset | JSON Schema defining incident record structure |
| `validate.py` | 13 KB | code | Dataset validation script with field checks & statistics |
| `generate_docs.py` | 8 KB | code | Documentation generation automation |
| `src.zip` | 9,918 KB | archive | Compressed archive of leaked Claude Code source |
| `README.md` | 5 KB | documentation | Project overview and quick-start guide |
| `LICENSE` | 1 KB | documentation | MIT License |
| `CITATION.cff` | 2 KB | documentation | BibTeX/CFF citation metadata |
| `INVENTORY.md` | 1 KB | documentation | Hetzner server corpus inventory |
| `TIMELINE_REPORT.txt` | 7 KB | documentation | Chronological incident summary |
| `META_INCIDENTS_QUICK_REFERENCE.txt` | 10 KB | documentation | Quick-reference text for all incidents |
| `META_SECURITY_RESEARCH_COMPLETION_REPORT.txt` | 21 KB | documentation | Agent-generated completion report |
| `META_AI_SECURITY_INDEX.md` | 11 KB | documentation | Indexed navigation for AI security findings |
| `docs/00_PROJECT_OVERVIEW.md` | varies | documentation | Structured project overview document |
| `docs/05_RESEARCH_FINDINGS.md` | varies | documentation | Consolidated research findings |
| `docs/06_PUBLICATION_PIPELINE.md` | varies | documentation | Publication workflow and checklist |
| `ai-leaks-research-2026.md` | 73 KB | research | Main living research report |
| `ai-leaks-research-2026-backup.md` | 36 KB | research | Backup snapshot of main report |
| `AI_SECURITY_INCIDENTS_AUDIT_2026.md` | 23 KB | research | Comprehensive audit of 2025-2026 incidents |
| `META_AI_SECURITY_INCIDENTS_2025-2026.md` | 17 KB | research | Year-in-review incident synthesis |
| `META_AGENT_BREACH_TECHNICAL_ANALYSIS.md` | 22 KB | research | Deep technical analysis of agentic breaches |
| `NPM_TYPOSQUAT_SECURITY_ANALYSIS_2026.md` | 15 KB | research | Forensic analysis of malicious npm typosquats |
| `new-incidents-to-add.md` | 20 KB | research | 16 newly discovered incidents pending integration |
| `all-agent-outputs-combined.txt` | 1,649 KB | research | Aggregated raw output from all research agents |
| `docs/_gemini_phase1_output.txt` | varies | research | Gemini Phase 1 agent output |
| `docs/_gemini_phase2_output.txt` | varies | research | Gemini Phase 2 agent output |
| `docs/_kimi_fileindex_output.txt` | varies | research | Kimi file-index agent output |
| `docs/_kimi_fileindex_v2_output.txt` | varies | research | Kimi file-index v2 agent output |
| `docs/_kimi_incidents_output.txt` | varies | research | Kimi incident-extraction agent output |
| `arXiv_draft.md` | 11 KB | publication | Full arXiv paper draft with outline |
| `ARXIV_ABSTRACT.md` | 15 KB | publication | Standalone abstract and related-work section |
| `DATASET_CARD.md` | 9 KB | publication | HuggingFace dataset card |
| `BENCHMARK_TASK.md` | 10 KB | publication | EU AI Act compliance classification benchmark |
| `MASTER_STRATEGY.md` | 16 KB | publication | 7-part commercialization and go-to-market strategy |
| `META_RESEARCH_DELIVERY_SUMMARY.md` | 14 KB | publication | Executive summary of deliverables |
| `ai-leaks-timeline.html` | 33 KB | publication | Interactive D3 timeline visualization |

---

## 2. Detailed File Descriptions

### a) `ai-leaks-incidents-public.json`

This file is the canonical public dataset release, containing **56 structured incident records** spanning January 2025 to April 2026. Each record follows a rigorous 13-field schema (`incident_name`, `company`, `date`, `type`, `how`, `what_exposed`, `accessibility`, `severity`, `urls`, `cve`, `verified`, `date_missing`, `data_classification`) that enables machine-readable analysis while preserving human readability. The dataset covers incidents from 25+ organizations including Anthropic, OpenAI, Meta, xAI, Google, HuggingFace, GitHub, and NVIDIA, categorized across nine vulnerability classes such as supply chain attacks, source code leaks, API key exposures, model weight theft, and state-sponsored misuse.

The dataset includes both verified incidents (those with independent public source URLs) and unverified incidents (reported through secondary channels with structured confidence scoring). Notable high-severity entries include the Shai-Hulud npm Worm variants, the TeamPCP cascading supply chain attack, the Claude Code npm source map leak (512K+ lines of TypeScript exposed), and the Claude Opus 4.6 mass distillation finding on HuggingFace. Field-level sanitization has been applied where necessary: 11 records carry `data_classification: redacted_internal_data` to remove specific internal details while maintaining research utility. This JSON serves as the primary artifact for academic citation, HuggingFace dataset publication, and the EU AI Act compliance benchmark.

### b) `MASTER_STRATEGY.md`

The master strategy document is a **7-part commercialization playbook** generated through multi-agent Gemini 3.1 Pro analysis, positioning the research portfolio for maximum academic and enterprise impact. Part 1 identifies publication gaps and immediate blockers (LaTeX conversion, Zenodo DOI, GitHub repository, GitHub Pages deployment, HuggingFace push, and UMMRO staging). Parts 2–3 provide a deep-dive into the 14 categories of leaked data stored on the Hetzner research server, mapping each category to potential paper titles, tooling ideas, and product concepts—from "Confused Deputy in the Terminal" (claude-code analysis) to "The AI Dark Economy" (underground forum monetization).

Parts 4–5 rank the top 10 academic research ideas and top 10 commercial ideas by impact and timeline, with the unauthorized Claude distillation finding (2.1M downloads) positioned as the central "smoking gun" for both venues. The core strategic pivot reframes UMMRO from a reactive incident database into a proactive "AI Vendor Risk Assessment Gateway" mandated by EU AI Act Article 28. Parts 6–7 deliver a concrete 30-day execution plan and identify the single biggest missed opportunity: third-party AI vendor risk assessment as a must-have enterprise procurement tool.

### c) `arXiv_draft.md`

This is the **full research paper draft** for submission to top-tier venues such as NeurIPS Datasets & Benchmarks, IEEE S&P, or USENIX Security. The abstract establishes AISecIncidents-2025-26 as the first large-scale open dataset correlating real-world LLM security incidents with regulatory compliance requirements, with a spotlight on the 2.1M download unauthorized distillation cluster. The paper outline spans seven sections: (1) Introduction framing the empirical gap in operational LLM security, (2) Related Work & Regulatory Context situating the dataset against CVE/NVD and EU AI Act Articles 9, 13, and 15, (3) Dataset Construction & Methodology detailing the 12-agent parallel research pipeline with inter-agent triangulation.

Section 4 presents dataset characteristics and taxonomy, while Section 5 provides a dedicated deep-dive on the Claude distillation finding—quantifying training compute savings for attackers and assessing GDPR/EU AI Act implications. Section 6 maps each incident class to compliance gaps and proposes a "compliance readiness" metric. The document concludes with suggested paper titles, recommended citations (Papernot et al., Selbst & Barocas, Barreno et al.), baseline comparisons against CVE/NVD, and a pre-submission compliance checklist covering licensing, embargo status, and responsible disclosure.

### d) `DATASET_CARD.md`

Formatted as a **HuggingFace dataset card**, this file provides the public-facing documentation for the `AI System Security Incidents 2025–2026` dataset. It opens with a YAML frontmatter block specifying the CC-BY-4.0 license, English language, AI-security tags, and dataset info features (13 fields, 40 examples in the original card, now 56 in the expanded dataset). The summary positions the dataset as the first publicly released structured corpus purpose-built for AI security research, supporting red-teaming, EU AI Act conformity assessment, academic research, and incident response training.

The card includes a dataset preview table, complete schema documentation, incident type taxonomy, accessibility status definitions, and data classification explanations. Usage examples are provided in both plain Python and pandas, demonstrating how to filter by severity and verified status. The construction methodology is documented: multi-agent research pipeline, source triangulation, structured extraction, and field-level sanitization. A "Novel Finding" callout highlights Incident #40 (Claude Opus 4.6 Mass Distillation), discovered via authenticated HuggingFace API queries during dataset construction. The card closes with intended use guidelines, a BibTeX citation block, and author attribution.

### e) `BENCHMARK_TASK.md`

This file defines the **`aisec-euaiact-v1.0` multi-label text classification benchmark**, which tasks models with mapping AI security incident descriptions to violated EU AI Act articles: Article 9 (Risk Management), Article 13 (Transparency), and Article 15 (Accuracy/Robustness/Cybersecurity). The benchmark test set comprises 12 verified incidents with ground-truth labels assigned by legal/ML annotators (inter-annotator agreement: Fleiss' κ = 0.71). Evaluation metrics include Exact Match, micro-averaged Precision/Recall/F1, Hamming Loss, and Mean Jaccard Index, with bootstrap confidence intervals due to the small test size.

The document provides a full label-distribution table, per-article prevalence statistics, and baseline comparisons: random classifier (14.3% EM), majority-class baseline {9,15} (41.7% EM), and human expert estimate (78% EM). A Python evaluation harness is included, along with a prompt template for LLM-based evaluation and a HuggingFace `datasets` loading example. The leaderboard submission format specifies a JSON Lines schema with prediction arrays and optional confidence scores. The file concludes with a NeurIPS Datasets & Benchmarks checklist (all items checked) and commercialization notes mapping the free benchmark tier to paid dataset and dashboard tiers.

### f) `INVENTORY.md`

The inventory serves as the **manifest for the 2.0 GB Hetzner research corpus**, documenting the directory structure and file-type statistics of the server-side leaked-data collection as of April 1, 2026. It lists disk usage across eight categories: `claude-code/` (1.3 GB), `system-prompts/` (579 MB), `archives/` (107 MB), `cve-pocs/` (3.9 MB), `vendor-reports/` (1.4 MB), `huggingface/` (176 KB), `supply-chain/` (104 KB), and `openai-google-xai/` (20 KB). Summary statistics report a total of **13,615 files**, including 4,563 TypeScript files, 633 JSON files, 57 HTML files, and 59 Rust files.

This inventory is critical for two reasons: first, it enables reproducible research by documenting the exact SHA256 manifest (`MANIFEST-updated.sha256`) that can verify corpus integrity; second, it provides the quantitative foundation for the cross-category synthesis ideas developed in `MASTER_STRATEGY.md`. The massive predominance of TypeScript files (4,563) in the `claude-code/` category directly supports the static-analysis research agenda, while the `system-prompts/` category's 579 MB represents one of the largest known collections of leaked commercial LLM system prompts.

### g) `new-incidents-to-add.md`

This file catalogs **16 newly discovered AI security incidents** (originally numbered #37–52, with some renumbering) that were not present in the March 2026 baseline report. The incidents were surfaced by 12+ parallel research agents operating over a 688 MB data corpus on the Hetzner server. The collection significantly expands the breadth of the dataset, adding incidents involving Cursor AI (CurXecute RCE and MCPoison), Amazon Q Developer (Unicode invisible injection + RCE), Sourcegraph Cody (1.8M account breach), LlamaIndex SQL injection (CVE-2025-1793), and multiple Anthropic-specific leaks (Claude Sonnet 5 "Fennec" codename leak, Claude Code hidden architecture with UNDERCOVER MODE and TENGU flags).

Each incident entry follows a standardized template: date, company/system, type, narrative of what happened, what was exposed, accessibility status, severity, and sources. Several entries include deep forensic detail, such as the SANDWORM_MODE npm worm's two-stage self-spreading mechanism (harvesting API keys from 9 LLM providers before injecting rogue MCP servers) and the confirmed bait-and-switch analysis of the `claude-client` and `claude-sdk` typosquat packages. The file also serves as a takedown confirmation log, documenting that `claude-code@2.1.88` was permanently removed from npm, providing forensic evidence of incident response.

### h) `validate.py`

`validate.py` is the **production-quality dataset validation script** that enforces schema compliance, detects duplicates, computes field completeness, and generates summary statistics for the incident dataset. Written in Python 3 with no external dependencies (optional `requests` for strict URL reachability checks), the script validates all 13 fields per record against type constraints, required/nullable rules, enumerated values, ISO 8601 date formats, and CVE format patterns. It also checks URL list items for valid `http(s)://` prefixes.

Upon execution, the script produces a formatted report including total record count, field completeness percentages, duplicate detection by `incident_name`, and breakdowns by severity, incident type, accessibility status, and data classification. The severity breakdown reveals the dataset's risk profile: 38% critical, 43% high, and 20% medium severity incidents. Exit codes are clean (0 for valid, 1 for validation errors), enabling CI/CD integration. This script is essential for maintaining dataset integrity as the corpus grows and serves as the gatekeeper before any public release or HuggingFace upload.

---

## 3. Source Code (`src_extracted/src/`)

The `src_extracted/src/` directory contains the **leaked source code of Claude Code**, Anthropic's AI coding assistant, extracted from the npm source map leak that occurred on March 31, 2026. This is one of the most significant artifacts in the entire research corpus.

### Quantitative Profile
- **TypeScript Files:** 1,332 (across all subdirectories)
- **Total Directories:** ~301
- **Archive Source:** `src.zip` (9.9 MB compressed)

### Top-Level Modules
The extracted source is organized into the following top-level directories and files:

```
QueryEngine.ts    Task.ts           Tool.ts
assistant         bootstrap         bridge
buddy             cli               commands
commands.ts       components        constants
context           context.ts        coordinator
cost-tracker.ts   costHook.ts       dialogLaunchers.tsx
entrypoints       history.ts        hooks
ink               ink.ts            interactiveHelpers.tsx
keybindings       main.tsx          memdir
migrations        moreright         native-ts
outputStyles      plugins           projectOnboardingState.ts
query             query.ts          remote
replLauncher.tsx  schemas           screens
server            services          setup.ts
skills            state             tasks
tasks.ts          tools             tools.ts
types             upstreamproxy     utils
vim               voice
```

### Research Significance
This source code represents a rare, complete exfiltration of a production AI agent codebase. It provides unprecedented visibility into how a frontier LLM agent bridges non-deterministic language model output with deterministic OS-level execution. Key research targets identified in `MASTER_STRATEGY.md` include the sanitization gap between `Tool.ts` and `child_process.exec`, the JSON schema reliance in `QueryEngine.ts`, and what the document terms a "Semantic Desync" vulnerability—where the LLM believes it is performing one action while the `Task.ts` parser executes another. The leaked code also contains internal codenames (TENGU, Capybara, Fennec), unreleased feature flags (UNDERCOVER MODE, ULTRAPLAN, Penguin Mode), and Safeguards team infrastructure details, making it a primary source for both offensive security research and AI governance analysis.

---

## 4. Hetzner Research Corpus

The Hetzner server hosts a **2.0 GB research corpus** organized into 8 categories. These files were collected, archived, and forensically preserved as primary source material for the AI security incident dataset and related research papers.

| # | Category | Path | Size | Contents |
|---|----------|------|------|----------|
| 1 | **Claude Code Leak** | `leaked-data/claude-code/` | 1.3 GB | Extracted and mirrored source code, source maps, and build artifacts from the Claude Code npm leak. Contains 4,563 TypeScript files representing the largest known exposure of a production AI agent codebase. |
| 2 | **System Prompts** | `leaked-data/system-prompts/` | 579 MB | Aggregated collection of leaked/extracted system prompts from commercial LLMs. Includes the ~57,000-word Claude prompt architecture and prompts from other major providers. One of the largest known corpora for reverse-engineering guardrails. |
| 3 | **Archives** | `leaked-data/archives/` | 107 MB | Historical snapshots, Wayback Machine archives, and preserved documentation showing "silent patches"—API capabilities quietly deprecated without CVEs or public disclosure. |
| 4 | **CVE PoCs** | `leaked-data/cve-pocs/` | 3.9 MB | Proof-of-concept exploit code for AI/ML CVEs. Used to analyze structural similarities in exploit delivery and map AI-specific vulnerabilities to MITRE ATT&CK. |
| 5 | **Vendor Reports** | `leaked-data/vendor-reports/` | 1.4 MB | Security vendor analyses, threat intelligence briefings, and incident response reports from companies like Check Point, Wiz, Sysdig, and Palo Alto Networks. |
| 6 | **HuggingFace** | `leaked-data/huggingface/` | 176 KB | Screenshots, API responses, and metadata documenting unauthorized model distillation campaigns, typosquatting attempts, and briefly exposed proprietary repositories. |
| 7 | **Supply Chain** | `leaked-data/supply-chain/` | 104 KB | npm package metadata, forensic analysis of malicious packages (claude-client, claude-sdk), and IOCs from the SANDWORM_MODE and TeamPCP campaigns. |
| 8 | **OpenAI/Google/xAI** | `leaked-data/openai-google-xai/` | 20 KB | Differential safety filter documentation, leaked model codenames, and API log anomalies from the three largest closed-model providers. |

**Corpus Totals:** 2.0 GB · 13,615 files · SHA256 manifest: `MANIFEST-updated.sha256`

---

## 5. Asset Summary

| Location | Files | Size |
|----------|-------|------|
| **Local Mac** | 41 files | 11.58 MB |
| **Hetzner Server** | 13,615 files | 2.0 GB |
| **Total Research Corpus** | 13,656 files | **~2.01 GB** |

The local Mac repository contains the curated, publish-ready artifacts: datasets, documentation, research reports, publication drafts, and validation code. The Hetzner server contains the raw, unfiltered primary source material—leaked code, system prompts, archives, and forensic evidence—that underpins the dataset's verified and unverified incident records. Together they form one of the most comprehensive empirical collections of real-world AI security incidents assembled to date.

---

*Compiled by Ahmed Adel Bakr Alderai — April 2026*
