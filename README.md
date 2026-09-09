# Localization Gate

Catch localization mistakes before they reach production.

Localization Gate is a lightweight, dependency-free checker for translation JSON files.

## Checks

- Missing translation keys
- Empty translations
- Placeholder mismatches
- Unexpected extra keys
- Possibly untranslated strings

## Usage

```bash
python localization_gate.py en.json ja.json
```

For stricter validation, warnings can also block the release:

```bash
python localization_gate.py en.json ja.json --strict
```

Localization Gate exits with a non-zero status when release-blocking findings are detected.

## GitHub Actions

The included workflow runs the checker automatically on pushes and pull requests. Edit the JSON paths to match your repository.

## Self-service edition

A separate self-service edition with an offline browser interface, Markdown report export, enhanced CLI, workflow template, examples, and step-by-step documentation is in development.

Purchasing is currently paused. Individual repository setup, implementation, translation, debugging, and email-based technical support are not offered.

Status: MVP / public preview
