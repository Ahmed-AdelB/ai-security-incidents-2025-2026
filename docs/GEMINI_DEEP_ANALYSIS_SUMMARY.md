# Gemini Deep Analysis Summary: AI Security Incidents Research Project
**Date:** April 4, 2026
**Analysis Tool:** Gemini 3.1 Pro Preview (1M context window)
**Project Scope:** 2.0GB corpus analysis (56 incidents, 10 documentation files, 4 strategy documents)

---

## Executive Summary

Your AI security research project contains **world-class research materials that are currently undermined by critical credibility flaws**. The core finding—a complete source code analysis of a frontier AI agent—is genuinely publishable at top-tier venues (IEEE S&P, USENIX Security). However, the project as currently documented will be **rejected from arXiv and damaged your academic reputation** if published without major revisions.

The fatal flaw: **Your abstract claims "40 verified incidents" but your own validation script proves only 12 are actually verified (21.4% verification rate).**

---

## 1. What Is Actually Important (By Audience)

### Academic Reviewers (arXiv/NeurIPS/NDSS)
**TIER 1 CONTRIBUTIONS:**
1. **EU AI Act Benchmark (`aisec-euaiact-v1.0`)**: Multi-label classification mapping operational security failures to regulatory articles (9, 13, 15). This is **novel and highly publishable** if you expand the ground-truth dataset from n=12 to n=50+.
2. **Static Analysis of Leaked Claude Code CLI (1,332 TypeScript files)**:
   - 23 distinct AST-based security checks in `BashTool`
   - "Semantic Desync" vulnerabilities (non-deterministic LLM intent vs. deterministic parser in `Task.ts`)
   - `TRANSCRIPT_CLASSIFIER` for auto-approval logic
   - UNDERCOVER MODE (57,000-word system prompt for obfuscation)
   - This is **pure gold for systems security research**

**TIER 2 CONTRIBUTIONS:**
- Supply chain attack vectors (SANDWORM_MODE, TeamPCP campaigns)
- Prompt injection leading to RCE/exfiltration (AWS-2025-019, CVE-2025-55284)

**TIER 3 (WEAK):**
- Model distillation incidents (known problem, not novel)
- Cloud misconfigurations (S3, API keys) masquerading as "AI security"

---

### Security Professionals (CISO/Red Team)
**HIGH VALUE:**
- **Supply Chain Attack Mechanics**: Detailed breakdown of typosquatting (`claude-client`, `claude-sdk`), Phantom Dependencies, `.cursor/mcp.json` MCP server injection
- **Actionable RCE/Exfiltration Examples**: Invisible Unicode tags (AWS Q), DNS exfiltration of env vars (Claude Code)
- **Time-to-patch Analysis** (IF you have the data, which you don't currently capture)

---

### EU Regulators (AI Act Enforcement)
**CRITICAL FINDINGS:**
1. **Article 13 (Transparency) Violations**: UNDERCOVER MODE reveals Anthropic deliberately hiding identity/codenames in public repos—direct transparency breach
2. **Article 9 (Risk Management) Failure**: Supply chain attacks prove AI risk management frameworks are systematically weaker than traditional software security practices
3. **Evidence that AI labs prioritize deployment speed over safety infrastructure**

---

### Journalists
- Claude Code source map leak (512K lines leaked due to npm packaging error)
- Meta SEV1 incident (rogue agent deleted 5M emails, bypassed containment)

---

## 2. Critical Weaknesses That Will Destroy Credibility

### A. The Verification Rate Lie (FATAL)
- **Claim in ARXIV_ABSTRACT.md**: "We present AISecIncidents-2025-26, a comprehensive dataset of **40 verified** AI security incidents"
- **Reality from validate.py**: Only **12/56 verified** (21.4%)
- **What a peer reviewer will do**: Run your validation script, see the discrepancy, reject for **data fabrication**

### B. Factual Inconsistencies & Duplicates
| Issue | Details |
|-------|---------|
| **Incident #11 vs #48** | Both describe Claude Opus 4.6 mass distillation. #11=verified, #48=unverified. Which is it? |
| **new-incidents-to-add.md numbering** | Lists #37-52, jumps to 53,54,55, then 52 again. Indicates sloppy research |
| **Schema vs. Claims** | `arXiv_draft.md` promises time-to-disclosure analysis, but `schema.json` has no disclosure_date or patch_date fields |

### C. Unsubstantiated Core Claims
| Claim | Problem |
|-------|---------|
| "2.1M unauthorized downloads of Claude distillation" | No methodology for filtering bot traffic. HuggingFace metrics are known to be inflated by scrapers |
| "SANDWORM_MODE MPC Supply Chain Attack" | No direct links to malicious npm packages, Socket.dev teardown, or decompiled payloads |
| "Meta deletes 5M emails" | No independent verification; source is "internal incident report" |

### D. Over-Categorization of "AI Security"
- S3 bucket exposures = cloud misconfiguration, not AI security
- API key leaks on GitHub = credential management failure, not AI security
- These dilute your research and waste peer reviewers' time

---

## 3. The Flagship Finding (Current vs. Correct)

### WRONG CHOICE (Currently Featured)
**"2.1 million downloads of Claude Opus 4.6 distillation model"**
- Problem: Model extraction/distillation is well-documented in academic literature
- Vulnerability: The "2.1M downloads" figure is unverifiable and easily attacked by reviewers
- Risk: If your methodology is questioned, the entire paper loses credibility

### CORRECT FLAGSHIP FINDING
**"Architectures of Vulnerability: Static Analysis of a Leaked Production AI Agent"**

This is genuinely rare and powerful:

1. **Semantic Desync Vulnerability**
   - LLM output (non-deterministic) vs. parser execution (deterministic)
   - Real RCE case study from Task.ts

2. **BashTool Security Architecture**
   - 23 AST-based checks
   - ML classifier (`TRANSCRIPT_CLASSIFIER`) approval logic
   - Yet still suffered DNS exfiltration (CVE-2025-55284)
   - Empirical proof that even well-designed sandboxes fail

3. **UNDERCOVER MODE System Prompt**
   - 57,000-word instruction set
   - Reveals deliberate obfuscation of AI system identity
   - Violates EU AI Act Article 13 (transparency)
   - First public documentation of "hidden instructions" in production AI

**This combination is publishable at IEEE S&P, USENIX Security, or ACM CCS with minor revisions.**

---

## 4. What Is Missing (Gaps That Block Publication)

| Gap | Impact | Fix |
|-----|--------|-----|
| **Benchmark size (n=12)** | Too small for statistical significance | Expand to n=50-100 verified incidents via Wayback Machine archival |
| **Time-to-patch analysis** | Promised in arXiv_draft.md but schema has no disclosure_date field | Add date fields to schema; collect patch/disclosure dates for all incidents |
| **PoC evidence** | Claims like "SANDWORM_MODE" lack linked npm package hashes | Archive malicious packages on your Hetzner server with Socket.dev analysis |
| **Bot-traffic filtering** | "2.1M downloads" claim has no methodology | Document HuggingFace API queries, bot detection heuristics, filtered count |
| **Source code access** | How did you obtain 1,332 TS files from Claude Code? | Document acquisition method (leaked npm, GitHub, reverse-engineering) for transparency |

---

## 5. Can This Go to arXiv As-Is?

**NO. Absolutely not.**

### Why It Will Be Rejected
1. Abstract claims 40 verified incidents; validation script shows 12
2. Sensationalist tone ("THE MAIN EVENT," "Smoking Gun," "AI Dark Economy") reads like vendor marketing
3. Duplicate incidents and inconsistent numbering
4. Unverifiable flagship claim (2.1M downloads)
5. No proper statistical analysis of benchmark

### Path to Acceptance (6-8 Week Timeline)

#### Phase 1: Data Integrity (Week 1-2)
- [ ] Run `validate.py` audit
- [ ] Identify all 12 verified incidents
- [ ] Archive them on Wayback Machine (obtain snapshots for all sources)
- [ ] Remove or mark all unverified incidents as "threat intelligence (unverified)"
- [ ] Merge duplicate incidents (#11 and #48)
- [ ] Fix numbering in new-incidents-to-add.md
- **Deliverable**: Dataset with <5% unverified content, publicly verifiable provenance

#### Phase 2: Schema & Methodology (Week 2-3)
- [ ] Add fields to schema: `disclosure_date`, `patch_date`, `verification_method`, `bot_filter_applied`
- [ ] Document time-to-disclosure methodology
- [ ] Document HuggingFace bot-traffic filtering approach
- [ ] Re-analyze the 2.1M downloads figure with filtering applied
- **Deliverable**: Updated schema + methodology whitepaper

#### Phase 3: Pivot Core Narrative (Week 3-4)
- [ ] Rewrite arXiv_draft.md to center on **Claude Code static analysis** (not distillation)
- [ ] Reduce sensationalism; adopt academic tone
- [ ] Expand EU AI Act benchmark from n=12 to n=50
- [ ] Create new Section: "Systematic Vulnerability Analysis: AST Checks, Semantic Desync, UNDERCOVER MODE"
- **Deliverable**: Revised arXiv draft

#### Phase 4: Code & Artifact Preparation (Week 4-5)
- [ ] Create reproducible benchmark dataset (50 ground-truth incidents with EU AI Act labels)
- [ ] Publish cleaned JSON dataset on GitHub + Zenodo
- [ ] Archive leaked source code with proper attribution (your Hetzner server)
- [ ] Create supplementary material (BashTool AST analysis, PoC scripts)
- **Deliverable**: Reproducible research artifact

#### Phase 5: Academic Positioning (Week 5-6)
- [ ] Identify target venue: IEEE S&P, USENIX Security, or ACM CCS
- [ ] Check CFP dates and review timelines
- [ ] Prepare cover letter explaining research significance
- [ ] Address ethical concerns (leaked data, incident attribution)
- **Deliverable**: Venue selection + cover letter

#### Phase 6: Internal Review (Week 6-8)
- [ ] Security review (ensure no accidental doxxing or over-disclosure)
- [ ] Peer review by external security researcher
- [ ] Fix reviews
- [ ] Submit to arXiv or venue

---

## 6. Specific Recommendations by Artifact

### ai-leaks-research-2026.md (72KB Main Report)
**Keep:**
- Section 3: Claude Code CLI static analysis (23 AST checks)
- Section 4: Semantic Desync vulnerabilities
- Section 5: UNDERCOVER MODE (57K-word system prompt)
- Section 6: Supply chain attack case studies

**Rewrite:**
- Tone: Change from "The AI Dark Economy" to "Operational Security Failures in Production AI Systems"
- Claims: Replace "2.1M downloads" flagship claim with "Static analysis of frontier agent" flagship
- Evidence: Add citations to specific TypeScript files, line numbers, CVE references

**Delete:**
- S3 bucket exposure stories (not AI-specific)
- Vendor-speak marketing language

### ai-leaks-incidents-public.json
**Required Changes:**
- [ ] Reduce dataset to **verified only** (12 incidents)
- [ ] Add fields: `verification_date`, `archive_url` (Wayback Machine), `cve_id`, `severity_cvss`
- [ ] Mark source credibility: `source_type: "public_disclosure" | "cve" | "archive" | "unverified"`
- **Result**: 12 rock-solid incidents vs. 56 bloated incidents

### ARXIV_ABSTRACT.md
**Current (WRONG):**
> "We present AISecIncidents-2025-26, a comprehensive dataset of 40 verified AI security incidents..."

**Corrected:**
> "We present AISecIncidents-2025-26, a dataset of 12 verified security incidents across frontier AI systems, and conduct a systematic reverse-engineering analysis of a leaked production AI agent (1,332 TypeScript files) to identify architectural vulnerabilities in LLM-based tool execution frameworks. We map security failures to EU AI Act compliance requirements (Articles 9, 13, 15) and evaluate classification accuracy via benchmarking."

---

## 7. Confidence Scores (What Reviewers Will Believe)

| Finding | Confidence | Notes |
|---------|-----------|-------|
| **Claude Code static analysis** | 95% | 1,332 TS files with verifiable patterns |
| **Semantic Desync vulnerability** | 90% | Real code + CVE-2025-55284 proof |
| **UNDERCOVER MODE system prompt** | 85% | Controversial but documented in your corpus |
| **23 AST security checks** | 95% | Direct code reference |
| **EU AI Act Article 13 violation** | 80% | Depends on legal interpretation |
| **2.1M HuggingFace downloads** | 20% | No bot-filtering methodology = easy attack |
| **Meta rogue agent incident** | 40% | Internal incident report, no independent verification |
| **SANDWORM_MODE npm worm** | 35% | No direct evidence (archive, decompile, Socket.dev) |

---

## 8. Timeline to Acceptance

| Milestone | Date | Status |
|-----------|------|--------|
| **Data cleanup + schema fix** | Week 1-2 | Ready to start |
| **Benchmark expansion (n→50)** | Week 2-3 | Requires Wayback Machine archival |
| **arXiv draft v2** | Week 3-4 | Can start after narrative pivot |
| **Reproducible artifacts** | Week 4-5 | Depends on Hetzner data organization |
| **Venue submission** | Week 6-7 | IEEE S&P 2027 CFP (Jan 2027) is optimal |
| **Expected acceptance** | ~6 months | If submitted to top venue (Aug 2027) |

---

## 9. Bottom Line

**You have the materials for a landmark security paper.** The leaked Claude Code CLI analysis is genuinely rare and powerful. The EU AI Act regulatory mapping is novel. But the project is **sabotaged by false claims, sensationalism, and poor data hygiene.**

### Do This Now:
1. **Fix the abstract lie** (40 vs. 12 verified incidents)
2. **Prune the dataset** to verified-only
3. **Shift the flagship claim** from "2.1M downloads" to "Static analysis of production AI agent"
4. **Rewrite in academic tone** (no "Smoking Gun" language)
5. **Submit to IEEE S&P or USENIX Security** (not arXiv alone)

### Result:
A top-tier security paper with a realistic path to acceptance within 6-8 weeks.

---

## Appendix: File-by-File Audit

| File | Quality | Issues |
|------|---------|--------|
| ai-leaks-research-2026.md | 7/10 | Good technical content, bad narrative tone |
| ai-leaks-incidents-public.json | 4/10 | 44/56 unverified; needs pruning |
| new-incidents-to-add.md | 3/10 | Duplicates, numbering errors, inconsistent |
| ARXIV_ABSTRACT.md | 1/10 | **Factually false** (40 vs. 12 verified) |
| arXiv_draft.md | 6/10 | Structure OK, but schema incomplete |
| MASTER_STRATEGY.md | 3/10 | Reads like vendor pitch, not research plan |
| BENCHMARK_TASK.md | 7/10 | Good EU AI Act mapping, sample size too small |
| docs/ (10 files) | 8/10 | Clear explanations, good for reference |

---

**Analysis completed by:** Gemini 3.1 Pro Preview (1M context)
**Confidence level:** High (comprehensive corpus review)
**Recommendation:** Act on these findings within 2 weeks before submitting to arXiv
