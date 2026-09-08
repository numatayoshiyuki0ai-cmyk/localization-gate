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
  [ERROR] PLACEHOLDER       items
  [ERROR] EMPTY VALUE       logout

WARNINGS
  [WARN]  EXTRA KEY         unused

==================================================
FAIL - Release blocked.
