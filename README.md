# Localization Gate

Catch localization mistakes before they reach production.

Localization Gate is a lightweight CI checker for translation JSON files. It helps development teams catch 
common localization problems automatically before release.

## What it detects

- Missing translation keys
- Empty translations
- Placeholder mismatches
- Unexpected extra keys
- Possibly untranslated strings

## Example

```text
Localization Gate
==================================================
Source : en.json
Target : ja.json

RELEASE BLOCKERS
  [ERROR] MISSING KEY      profile.save
  [ERROR] PLACEHOLDER      items
  [ERROR] EMPTY VALUE      logout

WARNINGS
  [WARN]  EXTRA KEY        unused

==================================================
FAIL - Release blocked.

```

## Why use it?

Localization bugs are easy to miss during code review.

A missing key, empty translation, or broken placeholder can reach production without being noticed until a user 
encounters it.

Localization Gate adds an automated check to your CI workflow so these problems can block a release before they 
reach production.

## Usage

Run:

```bash
python localization_gate.py en.json ja.json
```

If release-blocking problems are found, Localization Gate exits with a non-zero status code.

For stricter validation, warnings can also block the release:

```bash
python localization_gate.py en.json ja.json --strict
```

## GitHub Actions

Localization Gate can run automatically on every push and pull request.

This allows localization problems to be detected as part of your existing GitHub workflow before changes are 
released.

## Early Access

I am currently offering early-access setup for a small number of development teams using JSON-based 
localization.

### Setup includes

- Integration into your GitHub repository
- Configuration for your localization files
- GitHub Actions / CI setup
- Initial verification
- Help getting the first successful check running

**Early access price: ¥4,980**

Purchase Early Access: https://quietlayer.github.io/localization-gate/

Please do not share private repository details, credentials, API keys, or other sensitive information in a public issue.

## Status

Early access / MVP
