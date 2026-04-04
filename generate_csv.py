#!/usr/bin/env python3
"""
Generate ai-leaks-incidents-public.csv from ai-leaks-incidents-public.json.

DECISION ON TASK 2 (distillation/Opus incidents):
After reviewing all 55 records, only ONE incident contains 'distillation' or 'Opus'
in its incident_name: 'Claude Opus 4.6 Mass Distillation on HuggingFace'.
There is no second distillation/Opus incident to merge or keep separate.
"""

import json
import csv
from pathlib import Path


def main():
    json_path = Path("ai-leaks-incidents-public.json")
    csv_path = Path("ai-leaks-incidents-public.csv")

    with open(json_path) as f:
        incidents = json.load(f)

    # All 16 fields in order
    fieldnames = [
        "incident_name",
        "company",
        "date",
        "type",
        "how",
        "what_exposed",
        "accessibility",
        "severity",
        "urls",
        "cve",
        "verified",
        "date_missing",
        "data_classification",
        "confidence_score",
        "discovery_date",
        "patch_date",
    ]

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for incident in incidents:
            row = {}
            for field in fieldnames:
                value = incident.get(field)
                if field == "urls" and isinstance(value, list):
                    # Join URLs with semicolon + space
                    value = "; ".join(value) if value else ""
                elif value is None:
                    value = ""
                elif isinstance(value, bool):
                    value = str(value)
                elif isinstance(value, (int, float)):
                    value = str(value)
                row[field] = value
            writer.writerow(row)

    print(f"Wrote {len(incidents)} records to {csv_path}")


if __name__ == "__main__":
    main()
