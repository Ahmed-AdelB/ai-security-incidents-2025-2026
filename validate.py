#!/usr/bin/env python3
"""
AI Leaks Incidents Dataset Validator

Validates ai-leaks-incidents-public.json against field constraints and reports:
- Total records
- Field completeness (% non-null per field)
- Duplicate detection by incident_name
- Summary statistics table: breakdown by severity, type, accessibility, data_classification
- URL reachability check (optional --strict flag)

Exit codes:
  0 = Valid dataset
  1 = Validation errors found
"""

import json
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any, Set, Tuple
from datetime import datetime
import re
from collections import defaultdict


# Field constraints
FIELD_CONSTRAINTS = {
    "incident_name": {
        "type": str,
        "required": True,
        "enum": None,
    },
    "company": {
        "type": str,
        "required": True,
        "enum": None,
    },
    "date": {
        "type": (str, type(None)),
        "required": False,
        "enum": None,
        "format": "ISO8601",
    },
    "type": {
        "type": str,
        "required": True,
        "enum": [
            "supply_chain",
            "source_code",
            "user_data",
            "training_data",
            "api_keys",
            "model_weights",
            "system_prompt",
            "api_vulnerability",
            "state_sponsored_misuse",
        ],
    },
    "how": {
        "type": str,
        "required": True,
        "enum": None,
    },
    "what_exposed": {
        "type": str,
        "required": True,
        "enum": None,
    },
    "accessibility": {
        "type": str,
        "required": True,
        "enum": ["live", "patched", "taken_down", "contained", "archived", "unknown"],
    },
    "severity": {
        "type": str,
        "required": True,
        "enum": ["critical", "high", "medium", "low"],
    },
    "urls": {
        "type": list,
        "required": True,
        "enum": None,
    },
    "cve": {
        "type": (str, type(None)),
        "required": False,
        "enum": None,
    },
    "verified": {
        "type": bool,
        "required": True,
        "enum": [True, False],
    },
    "date_missing": {
        "type": bool,
        "required": True,
        "enum": [True, False],
    },
    "data_classification": {
        "type": str,
        "required": True,
        "enum": ["public_sources_only", "redacted_internal_data", "unverified"],
    },
    "confidence_score": {
        "type": (int, float),
        "required": True,
        "enum": None,
    },
    "discovery_date": {
        "type": (str, type(None)),
        "required": False,
        "enum": None,
        "format": "ISO8601",
    },
    "patch_date": {
        "type": (str, type(None)),
        "required": False,
        "enum": None,
        "format": "ISO8601",
    },
}

EXPECTED_FIELDS = set(FIELD_CONSTRAINTS.keys())


class ValidationError:
    def __init__(self, record_idx: int, field: str, message: str):
        self.record_idx = record_idx
        self.field = field
        self.message = message

    def __str__(self) -> str:
        return f"Record {self.record_idx} ({field}): {self.message}"


def validate_date_format(date_str: str) -> bool:
    """Check if date is ISO 8601 format (YYYY-MM-DD)."""
    if date_str is None:
        return True
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, date_str):
        return False
    try:
        datetime.fromisoformat(date_str)
        return True
    except ValueError:
        return False


def validate_cve_format(cve_str: str) -> bool:
    """Check if CVE is in valid format (CVE-YYYY-XXXXX)."""
    if cve_str is None:
        return True
    pattern = r"^CVE-\d{4}-\d+$"
    return bool(re.match(pattern, cve_str))


def validate_field(record_idx: int, field: str, value: Any) -> List[ValidationError]:
    """Validate a single field against constraints."""
    errors = []
    constraint = FIELD_CONSTRAINTS[field]

    # Type check
    if not isinstance(value, constraint["type"]):
        expected_type = (
            constraint["type"].__name__
            if isinstance(constraint["type"], type)
            else " | ".join(t.__name__ if t is not type(None) else "null" for t in constraint["type"])
        )
        errors.append(
            ValidationError(
                record_idx,
                field,
                f"Expected {expected_type}, got {type(value).__name__}",
            )
        )
        return errors

    # Null check (required fields)
    if constraint["required"] and value is None:
        errors.append(ValidationError(record_idx, field, "Required field is null"))
        return errors

    # Skip further checks if null (for optional fields)
    if value is None:
        return errors

    # Enum check
    if constraint["enum"] is not None:
        if value not in constraint["enum"]:
            errors.append(
                ValidationError(
                    record_idx,
                    field,
                    f"Value '{value}' not in enum {constraint['enum']}",
                )
            )

    # Format-specific checks
    if field == "date":
        if not validate_date_format(value):
            errors.append(ValidationError(record_idx, field, "Invalid ISO8601 date format"))

    if field == "cve":
        if not validate_cve_format(value):
            errors.append(ValidationError(record_idx, field, "Invalid CVE format (expected CVE-YYYY-XXXXX)"))

    if field == "urls":
        if not isinstance(value, list):
            errors.append(ValidationError(record_idx, field, "urls must be a list"))
        else:
            for idx, url in enumerate(value):
                if not isinstance(url, str):
                    errors.append(
                        ValidationError(
                            record_idx,
                            field,
                            f"URL at index {idx} is not a string",
                        )
                    )
                elif not url.startswith(("http://", "https://")):
                    errors.append(
                        ValidationError(
                            record_idx,
                            field,
                            f"URL at index {idx} does not start with http(s)://",
                        )
                    )

    return errors


def validate_record(record_idx: int, record: Dict[str, Any]) -> List[ValidationError]:
    """Validate a single record."""
    errors = []

    # Check for unknown fields
    record_fields = set(record.keys())
    unknown_fields = record_fields - EXPECTED_FIELDS
    if unknown_fields:
        errors.append(
            ValidationError(
                record_idx,
                "structure",
                f"Unknown fields: {unknown_fields}",
            )
        )

    # Check for missing fields
    missing_fields = EXPECTED_FIELDS - record_fields
    if missing_fields:
        errors.append(
            ValidationError(
                record_idx,
                "structure",
                f"Missing fields: {missing_fields}",
            )
        )

    # Validate each field
    for field, constraint in FIELD_CONSTRAINTS.items():
        if field in record:
            field_errors = validate_field(record_idx, field, record[field])
            errors.extend(field_errors)

    return errors


def check_url_reachability(url: str, timeout: int = 5) -> Tuple[bool, str]:
    """Check if URL is reachable via HEAD request."""
    try:
        import requests

        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code < 400, str(response.status_code)
    except ImportError:
        return None, "requests not installed"
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(
        description="Validate ai-leaks-incidents-public.json dataset"
    )
    parser.add_argument(
        "--file",
        default=str(Path(__file__).parent / "ai-leaks-incidents-public.json"),
        help="Path to JSON file to validate",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Validate URL reachability (requires requests library)",
    )
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"ERROR: File not found: {file_path}")
        return 1

    # Load JSON
    try:
        with open(file_path) as f:
            incidents = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        return 1
    except Exception as e:
        print(f"ERROR: Could not read file: {e}")
        return 1

    if not isinstance(incidents, list):
        print("ERROR: Root element must be a JSON array")
        return 1

    total_records = len(incidents)
    print(f"\n{'='*70}")
    print(f"AI LEAKS INCIDENTS DATASET VALIDATION")
    print(f"{'='*70}\n")

    # Validate all records
    all_errors = []
    for idx, record in enumerate(incidents):
        errors = validate_record(idx, record)
        all_errors.extend(errors)

    # Check for duplicates by incident_name
    incident_names: Dict[str, List[int]] = defaultdict(list)
    for idx, record in enumerate(incidents):
        if "incident_name" in record:
            incident_names[record["incident_name"]].append(idx)

    duplicates = {name: indices for name, indices in incident_names.items() if len(indices) > 1}

    # Field completeness analysis
    field_completeness = {}
    for field in EXPECTED_FIELDS:
        non_null_count = sum(
            1 for record in incidents if record.get(field) is not None
        )
        percentage = (non_null_count / total_records) * 100 if total_records > 0 else 0
        field_completeness[field] = (non_null_count, percentage)

    # Summary statistics
    severity_breakdown = defaultdict(int)
    type_breakdown = defaultdict(int)
    accessibility_breakdown = defaultdict(int)
    classification_breakdown = defaultdict(int)

    for record in incidents:
        severity_breakdown[record.get("severity", "unknown")] += 1
        type_breakdown[record.get("type", "unknown")] += 1
        accessibility_breakdown[record.get("accessibility", "unknown")] += 1
        classification_breakdown[record.get("data_classification", "unknown")] += 1

    # URL reachability check (if --strict)
    url_errors = []
    if args.strict:
        print("Checking URL reachability (may take a moment)...\n")
        for idx, record in enumerate(incidents):
            urls = record.get("urls", [])
            for url in urls:
                reachable, status = check_url_reachability(url)
                if reachable is None:
                    print(f"SKIP: {url} (requests library not installed)")
                elif not reachable:
                    url_errors.append((idx, url, status))
                    print(f"UNREACHABLE: {url} ({status})")
        if url_errors:
            print()

    # Print report
    print(f"TOTAL RECORDS: {total_records}\n")

    # Field Completeness
    print("FIELD COMPLETENESS:")
    print(f"{'Field':<30} {'Count':<10} {'Percentage':<10}")
    print("-" * 50)
    for field in sorted(EXPECTED_FIELDS):
        count, pct = field_completeness[field]
        print(f"{field:<30} {count:<10} {pct:>6.1f}%")
    print()

    # Duplicates
    if duplicates:
        print(f"DUPLICATES FOUND: {len(duplicates)}")
        for name, indices in duplicates.items():
            print(f"  - {name}: indices {indices}")
        print()
    else:
        print("DUPLICATES: None found (all incident_names are unique)\n")

    # Summary Stats
    print("SEVERITY BREAKDOWN:")
    for severity in ["critical", "high", "medium", "low"]:
        count = severity_breakdown.get(severity, 0)
        pct = (count / total_records) * 100 if total_records > 0 else 0
        print(f"  {severity:<15} {count:>3} ({pct:>5.1f}%)")
    print()

    print("INCIDENT TYPE BREAKDOWN:")
    for itype in sorted(type_breakdown.keys()):
        count = type_breakdown[itype]
        pct = (count / total_records) * 100 if total_records > 0 else 0
        print(f"  {itype:<30} {count:>3} ({pct:>5.1f}%)")
    print()

    print("ACCESSIBILITY BREAKDOWN:")
    for status in sorted(accessibility_breakdown.keys()):
        count = accessibility_breakdown[status]
        pct = (count / total_records) * 100 if total_records > 0 else 0
        print(f"  {status:<20} {count:>3} ({pct:>5.1f}%)")
    print()

    print("DATA CLASSIFICATION BREAKDOWN:")
    for classification in sorted(classification_breakdown.keys()):
        count = classification_breakdown[classification]
        pct = (count / total_records) * 100 if total_records > 0 else 0
        print(f"  {classification:<30} {count:>3} ({pct:>5.1f}%)")
    print()

    # Validation Errors
    if all_errors:
        print(f"VALIDATION ERRORS FOUND: {len(all_errors)}")
        print("-" * 70)
        for error in all_errors:
            print(f"  {error}")
        print()
        return 1

    if url_errors and args.strict:
        print(f"URL REACHABILITY ERRORS FOUND: {len(url_errors)}")
        print("-" * 70)
        for record_idx, url, status in url_errors:
            print(f"  Record {record_idx}: {url} ({status})")
        print()
        return 1

    print(f"{'='*70}")
    print("VALIDATION PASSED: Dataset is valid")
    print(f"{'='*70}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
