# Zenodo Upload Guide

Step-by-step guide for uploading the AI Security Incidents dataset to Zenodo for DOI assignment.

---

## Prerequisites

- Zenodo account (https://zenodo.org/)
- Recommended: Link Zenodo account to GitHub for automatic versioning

---

## Step 1: Create New Upload

1. Log in to https://zenodo.org/
2. Click the **"New Upload"** button (top-right)
3. Select **"Upload"** type (not GitHub import for this manual process)

---

## Step 2: Upload Files

Drag and drop or select these files from the repository:

| File | Purpose |
|------|---------|
| `ai-leaks-incidents-public.json` | Full dataset (55 records) |
| `ai-leaks-incidents-verified-v1.0.json` | Verified subset (12 records) |
| `paper.tex` | Academic paper source |
| `bibliography.bib` | Bibliography file |

**Important:** Do NOT upload:
- `src_extracted/` (contains proprietary source code)
- `leaked-data/` (contains sensitive data)
- `*.zip`, `*.tar.gz` archives
- Internal research notes

---

## Step 3: Fill Metadata

### Basic Information

| Field | Value |
|-------|-------|
| **Title** | AISecIncidents-2025-26: A Large-Scale Dataset of Real-World AI Security Breaches with EU AI Act Compliance Mapping |
| **Authors** | Ahmed Adel Bakr Alderai |
| **Publication Date** | 2026-04-01 |

### Description

```
A curated dataset of 55 AI system security incidents spanning January 2025 to April 2026, covering 14 leading AI organizations. Incidents are categorized across 9 vulnerability classes, severity-rated, and mapped to EU AI Act Articles 9, 13, and 15.

Includes novel empirical evidence of unauthorized LLM distillation at production scale (2.1M downloads). 12 incidents are precision-verified against independent public sources; 43 are documented with structured confidence scoring.
```

### Keywords

Add these keywords (one per field):
- AI security
- LLM security
- supply chain attacks
- EU AI Act
- dataset
- threat intelligence
- model distillation
- security incidents
- compliance

### License

Select: **Creative Commons Attribution 4.0 International (CC-BY-4.0)**

### Resource Type

Select: **Dataset**

### Related/Alternate Identifiers

Add this identifier:
- **Relation:** Is supplemented by this upload
- **Identifier:** https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026

---

## Step 4: Publish

1. Review all metadata carefully
2. Click **"Publish"**
3. Confirm the publish dialog
4. Zenodo will assign a DOI: `10.5281/zenodo.XXXXXXX`

---

## Step 5: Update CITATION.cff

After publication, copy the assigned DOI and update `CITATION.cff`:

```yaml
doi: "10.5281/zenodo.XXXXXXX"
```

Replace `XXXXXXX` with the actual Zenodo record number.

---

## Step 6: Update Paper.tex

Add the dataset DOI to the footnote in Section III (Dataset Description):

Find this text in `paper.tex`:
```latex
\footnote{Dataset available at: \url{https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026}}
```

Update to:
```latex
\footnote{Dataset available at: \url{https://huggingface.co/datasets/Ahmed-AdelB/ai-security-incidents-2025-2026} and archived at \url{https://doi.org/10.5281/zenodo.XXXXXXX}}
```

---

## Step 7: Commit Changes

```bash
git add CITATION.cff paper.tex
git commit -m "Add Zenodo DOI to citation files"
git push
```

---

## Verification

After completing all steps:

1. ✅ Zenodo record is public with DOI
2. ✅ CITATION.cff contains the DOI
3. ✅ Paper.tex references both HuggingFace and Zenodo
4. ✅ README.md shows Zenodo badge (update badge URL after DOI is assigned)

---

## Post-Publication Badge Update

Update the DOI badge in `README.md`:

Find:
```markdown
[![DOI](https://zenodo.org/badge/DOI/TBD.svg)](https://doi.org/TBD)
```

Replace with:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```
