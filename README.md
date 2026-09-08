# Localization Gate

Catch localization mistakes before they reach production.

Localization Gate checks translation JSON files before release.

## Detects

- Missing translation keys
- Empty translations
- Placeholder mismatches
- Unexpected extra keys

## Usage

Run: python localization_gate.py en.json ja.json

If errors are found, Localization Gate returns FAIL and blocks the release.

If no errors are found, Localization Gate returns PASS.

## Status

Early access / MVP
