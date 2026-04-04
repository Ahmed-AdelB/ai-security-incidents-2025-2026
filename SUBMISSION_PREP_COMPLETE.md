# Zenodo & arXiv Submission Package Preparation — COMPLETE

**Completion Date:** 2026-04-05
**Project:** AISecIncidents-2025-26
**Status:** ✅ All Tasks Completed

---

## Task Summary

### Task 1: Zenodo Metadata JSON ✅ COMPLETE

**File Created:** `/Users/aadel/projects/ai-leaks-research/zenodo_metadata.json`

**Contents:**
- Title: AISecIncidents-2025-26: A Dataset of AI Security Incidents with EU AI Act Compliance Mapping
- Upload Type: dataset
- Access Right: open
- License: CC BY 4.0
- Publication Date: 2026-04-05
- Creator: Ahmed Adel Bakr Alderai (Independent Researcher)
- Keywords: 11 terms (AI security, LLM, EU AI Act, compliance, Claude Code, static analysis, dataset, distillation, supply chain, governance, taxonomy)
- Related Identifiers: GitHub repository link
- Language: eng
- File Size: 1.5 KB

**Zenodo Upload Instructions:**
1. Log in to https://zenodo.org
2. Create new upload
3. Upload dataset files:
   - ai-leaks-incidents-public.json (55 incidents)
   - ai-leaks-incidents-verified-v1.0.json (12 verified incidents)
   - ai-leaks-incidents-public.csv (CSV export)
   - DATASET_CARD.md (documentation)
   - BENCHMARK_TASK.md (benchmark specification)
4. Paste metadata from zenodo_metadata.json
5. Submit for publication
6. **Record the DOI** (e.g., 10.5281/zenodo.XXXXXXX)

---

### Task 2: arXiv Submission Checklist ✅ COMPLETE

**File Created:** `/Users/aadel/projects/ai-leaks-research/ARXIV_SUBMISSION_CHECKLIST.md`

**Contents (11 KB):**
- Submission metadata (category: cs.CR, cross-lists: cs.AI, cs.CY)
- Required files list (paper.tex, bibliography.bib, figures)
- LaTeX compilation workflow
- Compilation sequence (pdflatex → bibtex → pdflatex × 2)
- Abstract section (full text from ARXIV_ABSTRACT.md)
- Data availability statement template
- Step-by-step submission workflow (24 numbered steps)
- Troubleshooting guide for compilation errors
- Submission status tracker
- Post-submission actions

**Key Features:**
- Comprehensive pre-submission checklist (44 checkboxes)
- Detailed troubleshooting table for common LaTeX errors
- arXiv submission workflow with specific UI instructions
- Placeholder management ([ZENODO_DOI] instructions)
- Timing considerations and best practices

---

### Task 3: Verify paper.tex Compilation ✅ COMPLETE

**Compilation Environment:** Hetzner Server (Ubuntu, remote SSH)

**Installation Completed:**
```
✅ texlive-latex-base
✅ texlive-latex-recommended
✅ texlive-fonts-recommended
✅ texlive-fonts-extra
✅ texlive-latex-extra
✅ texlive-science (algorithm, algorithmic packages)
✅ texlive-publishers (IEEEtran class)
```

**Compilation Results:**
| Phase | Command | Result | Output |
|-------|---------|--------|--------|
| 1 | pdflatex paper.tex | ✅ SUCCESS | 4 pages, 149 KB |
| 2 | bibtex paper | ✅ SUCCESS | IEEEtran.bst v1.14 |
| 3 | pdflatex paper.tex (2nd) | ✅ SUCCESS | 4 pages, 154 KB |
| 4 | pdflatex paper.tex (3rd) | ✅ SUCCESS | 4 pages, 154 KB |

**Generated Files on Hetzner:**
- paper.pdf (151 KB) — Final compiled PDF ✅
- paper.aux (5.6 KB) — Auxiliary references ✅
- paper.bbl (2.3 KB) — Processed bibliography ✅
- paper.blg (1.4 KB) — Bibliography log ✅
- paper.log (26 KB) — Full compilation transcript ✅

**PDF Verification:**
- ✅ File size: 151 KB (reasonable)
- ✅ Page count: 4 pages
- ✅ All fonts embedded (Type 1)
- ✅ Hyperlinks functional
- ✅ Bibliography: IEEEtran style
- ✅ Cross-references resolved
- ✅ Metadata embedded (title, author, keywords)

**Quality Assessment:** ✅ READY FOR ARXIV SUBMISSION

**Compilation Report:** `/Users/aadel/projects/ai-leaks-research/COMPILATION_REPORT.md`

---

## Deliverables Summary

### Files Created

1. **zenodo_metadata.json** (1.5 KB)
   - Complete Zenodo upload metadata
   - CC BY 4.0 license
   - GitHub repository reference
   - Ready for Zenodo upload

2. **ARXIV_SUBMISSION_CHECKLIST.md** (11 KB)
   - 44 completion checkboxes
   - Step-by-step submission workflow
   - Troubleshooting guide
   - Timing and best practices
   - Placeholder management instructions

3. **COMPILATION_REPORT.md** (5.8 KB)
   - Installation details
   - Compilation sequence results
   - PDF verification metrics
   - Quality assessment (PASS)
   - Next steps documentation

### Ready-to-Use Assets

- paper.tex: ✅ Compiles successfully (4 pages)
- bibliography.bib: ✅ Processed by bibtex
- paper.pdf: ✅ Generated and verified
- Dataset files: ✅ ai-leaks-incidents-public.json, verified-v1.0.json
- Documentation: ✅ DATASET_CARD.md, BENCHMARK_TASK.md, CITATION.cff

---

## Next Steps (Recommended Order)

### Phase M4: Zenodo Upload
1. Log in to https://zenodo.org (create account if needed)
2. Create new upload in "Datasets" category
3. Upload dataset files:
   - ai-leaks-incidents-public.json
   - ai-leaks-incidents-verified-v1.0.json
   - ai-leaks-incidents-public.csv
   - DATASET_CARD.md
   - BENCHMARK_TASK.md
   - README.md
   - CITATION.cff
4. Paste metadata from zenodo_metadata.json
5. Select CC BY 4.0 license
6. Submit for publication
7. **Copy DOI from confirmation page** (e.g., 10.5281/zenodo.12345678)

### Phase M5: Update and Recompile
1. Open paper.tex
2. Find all instances of `[ZENODO_DOI]`
3. Replace with actual DOI from Zenodo (e.g., `10.5281/zenodo.12345678`)
4. Find all instances of `https://zenodo.org/placeholder`
5. Replace with full DOI URL: `https://doi.org/10.5281/zenodo.12345678`
6. Recompile on Hetzner:
   ```bash
   cd ~/projects/ai-leaks-research
   pdflatex -interaction=nonstopmode paper.tex
   bibtex paper
   pdflatex -interaction=nonstopmode paper.tex
   pdflatex -interaction=nonstopmode paper.tex
   ```
7. Verify final PDF: `ls -lh paper.pdf`

### Phase M6: arXiv Submission
1. Follow ARXIV_SUBMISSION_CHECKLIST.md steps 1-23
2. Create submission package:
   ```bash
   cd /Users/aadel/projects/ai-leaks-research
   mkdir arxiv_submission
   cp paper.tex arxiv_submission/
   cp bibliography.bib arxiv_submission/
   tar -czf arxiv_submission.tar.gz arxiv_submission/
   ```
3. Log in to https://arxiv.org/user/ (create account if needed)
4. Click "Start New Submission"
5. Select category: **cs.CR** (primary)
6. Cross-list: **cs.AI**, **cs.CY**
7. Upload arxiv_submission.tar.gz
8. Paste abstract from ARXIV_ABSTRACT.md (section 2)
9. Enter author: Ahmed Adel Bakr Alderai
10. License: CC BY 4.0
11. Add Zenodo DOI to "Related identifiers" or comments field
12. Submit for announcement
13. **Record arXiv ID** (e.g., 2604.00123)

### Phase M7: Cross-Linking
1. Update GitHub README.md:
   - Add Zenodo badge: `[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)`
   - Add arXiv link: `[arXiv Preprint](https://arxiv.org/abs/YYMM.NNNNN)`
2. Update Zenodo upload metadata:
   - Add arXiv cross-reference: `https://arxiv.org/abs/YYMM.NNNNN`
3. Post to institutional repositories (if applicable)
4. Announce on social media/mailing lists

---

## Timeline Estimate

| Phase | Task | Duration |
|-------|------|----------|
| M4 | Zenodo upload + DOI receipt | 15-30 minutes |
| M5 | Update paper.tex + recompile | 5-10 minutes |
| M6 | arXiv submission + ID receipt | 20-30 minutes |
| M7 | Cross-linking + announcement | 10-15 minutes |
| **Total** | **Complete publication** | **~1-2 hours** |

---

## Important Notes

### Placeholder Management
- **[ZENODO_DOI]** appears in:
  - paper.tex (data availability statement)
  - zenodo_metadata.json (already in format, no update needed)
- **Replace with:** `10.5281/zenodo.XXXXXXX` (without https://)
- Full URL format: `https://doi.org/10.5281/zenodo.XXXXXXX`

### arXiv Timing
- Submissions before **14:00 UTC**: Appear in next day's announcement
- Submissions after **14:00 UTC**: Appear in following day's announcement
- Best practice: Submit before 13:00 UTC for predictable timing

### Version Management
- Current version: v1.0 (dataset specification)
- After arXiv ID received: Update all references to include arXiv ID
- If revisions needed before announcement: Contact arXiv administrators
- After announcement: New versions become v2, v3, etc. (automatically tracked)

### Files NOT to Upload to arXiv
- ✅ Include: paper.tex, bibliography.bib, figures (if separate PDFs)
- ❌ Exclude: paper.pdf, paper.aux, paper.log, paper.bbl, .DS_Store, etc.
- arXiv will recompile from .tex + .bib sources

---

## Verification Checklist

- ✅ zenodo_metadata.json created and validated
- ✅ ARXIV_SUBMISSION_CHECKLIST.md created with 44 tasks
- ✅ paper.tex compiles successfully on Hetzner
- ✅ pdflatex installed and tested
- ✅ bibliography.bib processed correctly
- ✅ paper.pdf generated (151 KB, 4 pages)
- ✅ All cross-references resolved
- ✅ No fatal errors in compilation
- ✅ Compilation report created

---

## Contact & Support

**For issues during Zenodo upload:**
- Zenodo support: https://zenodo.org/support

**For issues during arXiv submission:**
- arXiv support: https://arxiv.org/help
- arXiv moderation appeals: https://arxiv.org/help/appeal

**Local documentation:**
- Compilation details: COMPILATION_REPORT.md
- Submission workflow: ARXIV_SUBMISSION_CHECKLIST.md
- Dataset documentation: DATASET_CARD.md
- Abstract text: ARXIV_ABSTRACT.md

---

**Prepared by:** Claude Code (claude-haiku-4-5-20251001)
**Project:** AISecIncidents-2025-26 (EU AI Act Compliance Research)
**Publication Status:** Ready for Zenodo + arXiv Submission
**Last Updated:** 2026-04-05 22:21 UTC
