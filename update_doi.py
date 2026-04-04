#!/usr/bin/env python3
"""
Update Zenodo DOI across all project files after upload.

Usage:
    python3 update_doi.py 10.5281/zenodo.XXXXXXX

Author: Ahmed Adel Bakr Alderai
"""

import sys
import re
from pathlib import Path

PLACEHOLDER = "[ZENODO_DOI]"
PROJECT_ROOT = Path(__file__).parent

FILES_TO_UPDATE = [
    "paper.tex",
    "CITATION.cff",
    "README.md",
    "ARXIV_ABSTRACT.md",
    "DATASET_CARD.md",
    "SUBMISSION_PREP_COMPLETE.md",
]

def update_doi(doi: str) -> None:
    if not doi.startswith("10.5281/zenodo."):
        print(f"Warning: DOI '{doi}' doesn't look like a Zenodo DOI (expected 10.5281/zenodo.XXXXXXX)")

    updated = []
    skipped = []

    for filename in FILES_TO_UPDATE:
        path = PROJECT_ROOT / filename
        if not path.exists():
            skipped.append(filename)
            continue

        content = path.read_text(encoding="utf-8")
        if PLACEHOLDER in content:
            new_content = content.replace(PLACEHOLDER, doi)
            path.write_text(new_content, encoding="utf-8")
            count = content.count(PLACEHOLDER)
            updated.append(f"{filename} ({count} replacement{'s' if count > 1 else ''})")
        else:
            skipped.append(f"{filename} (no placeholder)")

    print(f"\nZenodo DOI: {doi}")
    print(f"\nUpdated ({len(updated)} files):")
    for f in updated:
        print(f"  ✓ {f}")

    if skipped:
        print(f"\nSkipped ({len(skipped)} files):")
        for f in skipped:
            print(f"  - {f}")

    print(f"\nNext steps:")
    print(f"  1. On Hetzner: cd ~/projects/ai-leaks-research && pdflatex paper.tex && bibtex paper && pdflatex paper.tex && pdflatex paper.tex")
    print(f"  2. Submit paper.tex + bibliography.bib to arXiv cs.CR")
    print(f"  3. Update HuggingFace dataset card with DOI")
    print(f"  4. git add -A && git commit -m 'docs: add Zenodo DOI {doi}' && git push")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 update_doi.py 10.5281/zenodo.XXXXXXX")
        sys.exit(1)
    update_doi(sys.argv[1])
