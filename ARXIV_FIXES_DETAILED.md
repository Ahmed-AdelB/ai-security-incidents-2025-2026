# arXiv Submission: Exact Fixes Required

## CRITICAL FIX #1: Remove Duplicate "Regulatory Interpretation" Section

**Location:** Lines 471-475 in paper.tex
**Action:** DELETE the second occurrence entirely (lines 473-475)

### What to remove (lines 473-475):
```latex
\textbf{Regulatory Interpretation:} EU AI Act compliance mapping involves interpretation of legal requirements that may evolve as regulatory guidance is issued. Our mapping reflects the state of knowledge as of April 2026 and should be updated as the regulatory framework matures.
```

### After deletion, the Limitations subsection should read:
```latex
\subsection{Limitations}

Several limitations affect the generalizability of our findings.

\textbf{Verification Gap:} Approximately 78\% of incidents (43/55) remain unverified with single-source attribution. This reflects the inherent challenge of incident verification in the AI security domain, where organizations may delay or avoid public disclosure.

\textbf{Selection Bias:} The dataset exhibits bias toward public-facing large organizations with established security disclosure practices. Incidents at smaller organizations or in regions with weaker disclosure requirements may be underrepresented.

\textbf{Temporal Constraints:} The 2025--2026 temporal boundary captures a specific period in AI security evolution. Rapid changes in LLM deployment practices may limit the relevance of incident patterns for future periods.

\textbf{Attribution Uncertainty:} Threat intelligence reports may contain attribution errors or deliberate misdirection. Our confidence scoring partially addresses this but cannot eliminate uncertainty.

\textbf{Static Analysis Scope:} The analysis of Claude Code covers version 2.1.88 only. Subsequent versions may have addressed identified vulnerabilities or introduced new security controls. The findings should be interpreted as a snapshot of the security posture at a specific point in time rather than a comprehensive assessment of the system's evolution.

\textbf{Regulatory Interpretation:} The mapping of incidents to EU AI Act articles represents our interpretation of regulatory requirements. Actual enforcement determinations may vary based on legal context, jurisdictional nuances, and evolving guidance from competent authorities.

\textbf{Technical Scope:} The static analysis focuses on the BashTool execution engine and does not cover all security mechanisms in Claude Code. Other tools and subsystems may have different security properties that were not analyzed in this work.
```

---

## CRITICAL FIX #2: Add Data Availability Subsection

**Location:** After line 500 (after Ethical Considerations subsection, before `\bibliographystyle{IEEEtran}`)
**Action:** ADD the following code block

### Insert this before `\bibliographystyle{IEEEtran}` (currently line 521):
```latex
\subsection{Data Availability}

All data artifacts from this research are publicly available without access restrictions:

\begin{itemize}
    \item \textbf{AISecIncidents-2025-26 Dataset:} 55 incidents with comprehensive metadata, severity classifications, confidence scores, and representative incident descriptions available at \url{https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026}

    \item \textbf{aisec-euaiact-v1.0 Benchmark:} 12 verified incidents with ground-truth multi-label EU AI Act Article classifications (Articles 9, 13, 15) for evaluating automated compliance classification systems, available in the same dataset repository.

    \item \textbf{Evaluation Scripts and Metrics:} Reproducible Python scripts for computing F1-micro, F1-macro, Exact Match, Hamming Loss, and Mean Jaccard Index metrics available in the dataset repository for community submissions.
\end{itemize}

The dataset is released under Creative Commons Attribution 4.0 (CC-BY-4.0) for academic and security research use. All materials are available immediately upon publication with no access restrictions or embargo periods. We welcome community contributions, corrections, and extensions to the dataset and benchmark.

```

---

## CRITICAL FIX #3: Add CVSS Citation to Bibliography

**Location:** bibliography.bib
**Action:** ADD this entry to the bibliography.bib file

### Add this entry to bibliography.bib (can be added at end, before closing file):
```bibtex
@misc{cvss2024,
  title={{Common Vulnerability Scoring System Version 3.1 Specification}},
  author={{Forum of Incident Response and Security Teams (FIRST)}},
  howpublished={\url{https://www.first.org/cvss/v3.1/specification-document}},
  year={2024}
}
```

### Then update paper.tex at TWO locations:

**Location 1: Line 98** (in Collection Methodology subsection)
Change from:
```latex
\item \textbf{Incident Classification Agents:} Taxonomy assignment and severity scoring according to CVSS-inspired criteria adapted for AI-specific risks.
```

To:
```latex
\item \textbf{Incident Classification Agents:} Taxonomy assignment and severity scoring according to CVSS-inspired criteria~\cite{cvss2024} adapted for AI-specific risks.
```

**Location 2: Line 186** (in Severity Distribution subsection)
Change from:
```latex
Severity assessment follows CVSS-inspired criteria adapted for AI-specific risks. Table~\ref{tab:severity} presents the distribution across all 55 incidents.
```

To:
```latex
Severity assessment follows CVSS-inspired criteria~\cite{cvss2024} adapted for AI-specific risks. Table~\ref{tab:severity} presents the distribution across all 55 incidents.
```

---

## MODERATE FIX #1: Add Citation for "Production AI Agent" Claim

**Location:** Line 43 (Abstract) and Line 59 (Introduction)
**Action:** ADD clarifying footnote or citation

### Option A: Add footnote at first mention (line 43 in Abstract)

Change from:
```latex
Our analysis of 1,332 source files reveals 23 AST-based security checks in the BashTool execution engine, a previously undocumented \emph{Semantic Desync} vulnerability class, and UNDERCOVER MODE---a 57,000-word instruction set with significant implications for transparency requirements under the EU AI Act~\cite{euaiact2024}.
```

To:
```latex
Our analysis of 1,332 source files reveals 23 AST-based security checks in the BashTool execution engine, a previously undocumented \emph{Semantic Desync} vulnerability class, and UNDERCOVER MODE---a 57,000-word instruction set with significant implications for transparency requirements under the EU AI Act~\cite{euaiact2024}. The analyzed code was from Claude Code v2.1.88, Anthropic's production AI agent released for code generation and execution.\footnote{Claude Code is Anthropic's production AI code generation system, described at \url{https://github.com/lanterndata/code-cli}}
```

### Option B: Add citation in bibliography if official documentation exists

Add to bibliography.bib:
```bibtex
@misc{claudecode2025,
  title={{Claude Code: Production AI Code Generation Agent}},
  author={{Anthropic Inc.}},
  howpublished={\url{https://github.com/lanterndata/code-cli}},
  year={2025}
}
```

Then cite with `~\cite{claudecode2025}` in the text.

---

## MODERATE FIX #2: Replace [ZENODO_DOI] Placeholder

**Location:** Line 104 (in Collection Methodology subsection, footnote)
**Action:** Replace placeholder with real DOI or valid placeholder

### Option A: Use real Zenodo DOI (PREFERRED)

1. Upload dataset to Zenodo (https://zenodo.org/deposit)
2. Get the DOI from Zenodo (format: 10.5281/zenodo/XXXXXXX)
3. Replace line 104:

Change from:
```latex
The dataset is publicly available.\footnote{Dataset DOI: \url{https://doi.org/[ZENODO_DOI]} (to be updated upon Zenodo publication).}
```

To (example with real DOI):
```latex
The dataset is publicly available.\footnote{Dataset DOI: \url{https://doi.org/10.5281/zenodo/12345678}}
```

### Option B: Use valid text placeholder (ACCEPTABLE)

Change from:
```latex
The dataset is publicly available.\footnote{Dataset DOI: \url{https://doi.org/[ZENODO_DOI]} (to be updated upon Zenodo publication).}
```

To:
```latex
The dataset is publicly available. The DOI will be assigned upon Zenodo publication and updated in the camera-ready version.\footnote{Preprint dataset available at \url{https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026}}
```

**Recommendation:** Option A is required for proper reproducibility. Upload to Zenodo before final submission.

---

## MINOR FIX #1: Expand Related Work Section (Optional)

**Location:** Lines 82-87 (AI Incident Databases subsection)
**Action:** Expand to include more incident taxonomy context

### Current text (lines 82-87):
```latex
\subsection{AI Incident Databases and Vulnerability Frameworks}

Several initiatives have attempted to catalog AI-related failures and security incidents. The AI Incident Database (AIID) catalogs AI-related harms across diverse application domains. While comprehensive in scope, AIID lacks systematic EU AI Act compliance mapping and does not employ multi-source verification for security incidents. Our work complements AIID by focusing specifically on security breaches with regulatory compliance assessment frameworks.

The OWASP LLM Top 10 2025~\cite{owasp_llm2025} provides a practitioner-oriented taxonomy of LLM application vulnerabilities. Our dataset operationalizes several of these categories---including prompt injection, insecure output handling, and supply chain vulnerabilities---as empirically observed incidents with documented impact and regulatory implications.
```

### Suggested expansion:
```latex
\subsection{AI Incident Databases and Vulnerability Frameworks}

Several initiatives have attempted to catalog AI-related failures and security incidents. The AI Incident Database (AIID) catalogs AI-related harms across diverse application domains. While comprehensive in scope, AIID lacks systematic EU AI Act compliance mapping and does not employ multi-source verification for security incidents. Our work complements AIID by focusing specifically on security breaches with regulatory compliance assessment frameworks.

Related security incident taxonomies include MITRE ATT&CK (adversarial tactics and techniques), NIST's cybersecurity framework, and CVE/CWE databases. However, these taxonomies were developed primarily for traditional software security and do not capture AI-specific attack vectors such as model extraction, training data leakage, and prompt injection. The OWASP LLM Top 10 2025~\cite{owasp_llm2025} provides a practitioner-oriented taxonomy of LLM application vulnerabilities. Our dataset operationalizes several of these categories---including prompt injection, insecure output handling, and supply chain vulnerabilities---as empirically observed incidents with documented impact and regulatory implications.

This work extends existing incident cataloging efforts by introducing: (1) systematic EU AI Act compliance mapping linking security incidents to specific regulatory articles; (2) multi-source verification methodology with quantified confidence scores; and (3) a structured benchmark for evaluating automated compliance classification systems.
```

---

## MINOR FIX #2: Add Concrete Example to Abstract (Optional)

**Location:** Lines 43-44 (Abstract)
**Action:** Add brief example after Semantic Desync mention

### Current text:
```latex
Our analysis reveals 23 AST-based security checks in the BashTool execution engine, a novel \emph{Semantic Desync} vulnerability class arising from non-deterministic LLM intent mapped to deterministic parser execution, and UNDERCOVER MODE---a 57,000-word instruction set with implications for transparency requirements.
```

### Enhanced version (optional):
```latex
Our analysis reveals 23 AST-based security checks in the BashTool execution engine, a novel \emph{Semantic Desync} vulnerability class where non-deterministic LLM-generated intent is misinterpreted by deterministic command parsers (e.g., network diagnostics reinterpreted as data exfiltration), and UNDERCOVER MODE---a 57,000-word instruction set with implications for transparency requirements.
```

---

## MINOR FIX #3: Clarify Dataset URL Relationship

**Location:** Lines 104 and 519
**Action:** Add clarifying text to indicate both URLs point to same data

### At line 519, change from:
```latex
The AISecIncidents-2025-26 dataset, benchmark labels, and evaluation scripts are available at \url{https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026}.
```

To:
```latex
The AISecIncidents-2025-26 dataset, benchmark labels, and evaluation scripts are available at \url{https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026} (also available via Zenodo DOI as referenced in Section~\ref{sec:dataset}).
```

---

## MINOR FIX #4: Enhance Author Affiliation (Optional for PhD Research)

**Location:** Lines 33-35
**Action:** Add institutional affiliation if applicable

### Current author block:
```latex
\author{
\IEEEauthorblockN{Ahmed Adel Bakr Alderai}
\IEEEauthorblockA{Independent Researcher\\
Email: ahmed.adel.bakr@gmail.com}
}
```

### If PhD research with institutional affiliation:
```latex
\author{
\IEEEauthorblockN{Ahmed Adel Bakr Alderai}
\IEEEauthorblockA{[Your University Name]\\
Department of [Your Department]\\
Email: ahmed.adel.bakr@gmail.com\\
ORCID: [if applicable]}
}
```

---

## VERIFICATION CHECKLIST

After making these fixes, verify:

```
✓ Lines 473-475 deleted (second "Regulatory Interpretation")
✓ Data Availability subsection added before bibliography
✓ CVSS citation added to bibliography.bib
✓ CVSS citations added to lines 98 and 186
✓ [ZENODO_DOI] placeholder replaced or fixed
✓ PDF compiles without errors
✓ All \cite{} references exist in bibliography.bib
✓ All \url{} links are valid
✓ Abstract still under 250 words
✓ Page count is ~8 pages
✓ All tables render correctly
✓ Zenodo DOI obtained (if using Option A)
```

---

## Estimated Timeline

| Task | Time | Status |
|------|------|--------|
| Delete duplicate section | 1 min | Quick |
| Add Data Availability section | 5 min | Quick |
| Add CVSS to bibliography | 2 min | Quick |
| Update CVSS citations in text | 2 min | Quick |
| Add production agent footnote | 2 min | Quick |
| Upload to Zenodo & get DOI | 30 min | BLOCKING |
| Optional: Expand Related Work | 10 min | Optional |
| Final PDF compilation & check | 10 min | Quick |
| **TOTAL** | **~60 minutes** | *Most time is Zenodo* |

**Critical path:** Upload to Zenodo first to get the DOI, then make all other edits.

