#!/usr/bin/env python3

import argparse
import json
import re
import sys
from pathlib import Path


PLACEHOLDER_PATTERNS = [
    re.compile(r"\{\{?\s*([A-Za-z_][A-Za-z0-9_.-]*)\s*\}?\}"),
    re.compile(r"%\(([A-Za-z_][A-Za-z0-9_.-]*)\)[a-zA-Z]"),
    re.compile(r"%([a-zA-Z])"),
]


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        fail(f"File not found: {path}")
    except json.JSONDecodeError as e:
        fail(f"Invalid JSON in {path}: line {e.lineno}, column {e.colno}")

    if not isinstance(data, dict):
        fail(f"Top level of {path} must be a JSON object.")

    return data


def flatten(data, prefix=""):
    result = {}

    for key, value in data.items():
        full_key = f"{prefix}.{key}" if prefix else key

        if isinstance(value, dict):
            result.update(flatten(value, full_key))
        else:
            result[full_key] = value

    return result


def placeholders(value):
    if not isinstance(value, str):
        return set()

    found = set()

    for pattern in PLACEHOLDER_PATTERNS:
        found.update(pattern.findall(value))

    return found


def fail(message):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(2)


def compare(source_path, target_path):
    source = flatten(load_json(source_path))
    target = flatten(load_json(target_path))

    errors = []
    warnings = []

    source_keys = set(source)
    target_keys = set(target)

    for key in sorted(source_keys - target_keys):
        errors.append(f"MISSING KEY      {key}")

    for key in sorted(target_keys - source_keys):
        warnings.append(f"EXTRA KEY        {key}")

    for key in sorted(source_keys & target_keys):
        source_value = source[key]
        target_value = target[key]

        if target_value is None or (
            isinstance(target_value, str) and not target_value.strip()
        ):
            errors.append(f"EMPTY VALUE      {key}")

        source_ph = placeholders(source_value)
        target_ph = placeholders(target_value)

        if source_ph != target_ph:
            errors.append(
                f"PLACEHOLDER       {key} "
                f"(source={sorted(source_ph)}, target={sorted(target_ph)})"
            )

        if (
            isinstance(source_value, str)
            and isinstance(target_value, str)
            and source_value.strip()
            and source_value.strip() == target_value.strip()
        ):
            warnings.append(f"POSSIBLY UNTRANSLATED {key}")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(
        description="Localization Gate - deterministic localization file validator"
    )
    parser.add_argument("source", help="Source-language JSON file")
    parser.add_argument("target", help="Target-language JSON file")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as release-blocking failures",
    )

    args = parser.parse_args()

    errors, warnings = compare(args.source, args.target)

    print("\nLocalization Gate")
    print("=" * 50)
    print(f"Source : {args.source}")
    print(f"Target : {args.target}")

    if errors:
        print("\nRELEASE BLOCKERS")
        for item in errors:
            print(f"  [ERROR] {item}")

    if warnings:
        print("\nWARNINGS")
        for item in warnings:
            print(f"  [WARN]  {item}")

    print("\n" + "=" * 50)

    if errors or (args.strict and warnings):
        print(
            f"FAIL - {len(errors)} error(s), "
            f"{len(warnings)} warning(s). Release blocked."
        )
        sys.exit(1)

    print(
        f"PASS - {len(errors)} error(s), "
        f"{len(warnings)} warning(s). Safe to continue."
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
