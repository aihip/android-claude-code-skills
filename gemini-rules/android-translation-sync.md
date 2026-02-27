# Android Translation Sync

> Synchronize Android project multilingual resources from Excel spreadsheet. Update strings.xml files for ALL languages including English. Write generated keys to Excel first column.

## When to Apply

Apply this workflow when the user asks to:
- Sync Android translations from Excel
- Update strings.xml from a translation sheet
- 多语言翻译同步 / 更新strings.xml
- android translation sync

## Process

### 1. Read Excel Spreadsheet

- Parse the Excel file provided by the user
- First row contains language headers
- **First column: "key"** (generated key for each translation)
- **Second column: "English"** (source language)
- Following columns: target languages (zh, es, fr, etc.)

**Excel format:**

| key | English | zh | es |
|-----|---------|-----|-----|
| | Sign In | 登录 | Iniciar |
| | Welcome | 欢迎 | Bienvenido |

### 2. Generate Keys for English Text

| First Column (key) | Action |
|--------------------|--------|
| **Empty** | Generate new key (10-20 chars, based on English) |
| **Has value** | Use existing key (don't regenerate) |

**Key generation rules:**
- Length: 10-20 characters
- Format: `lowercase_with_underscores`
- Must not conflict with existing keys in strings.xml

Examples: `"Sign In"` → `sign_in_button` · `"Welcome to our app"` → `welcome_message`

### 3. Write Keys Back to Excel First Column

For each empty key row: generate key → write to first column. For rows with existing key: keep as-is.

### 4. Update strings.xml Files — CRITICAL RULES

**RULE: Replace ONLY the text content between `<string>` and `</string>` tags.**

**ABSOLUTE RULES:**
- ✅ Find `<string name="xxx">existing_value</string>` → replace ONLY `existing_value`
- ❌ DO NOT add any new lines
- ❌ DO NOT remove any existing lines
- ❌ DO NOT modify anything else (comments, blank lines, attributes, indentation)

**Correct example:**
```xml
<!-- BEFORE -->
<string name="skip">Skip</string>

<string name="quit">Quit</string>

<!-- AFTER — only value changed, nothing else -->
<string name="skip">تخطى</string>

<string name="quit">خروج</string>
```

**Update rules per key:**

| Scenario | Action |
|----------|--------|
| Key exists in file | Update ONLY value content |
| Key missing in file | Append new entry at bottom |
| Language file missing | Create new file in `values-<lang>/` directory |

**File locations:**
- `app/src/main/res/values/strings.xml` ← English column
- `app/src/main/res/values-zh/strings.xml` ← zh column
- `app/src/main/res/values-es/strings.xml` ← es column
- (and so on for all language columns in Excel)

### 5. Output Summary

After processing, report:
```
Translation Sync Summary:
- Excel file: translations.xlsx
- Total rows processed: N
- Keys generated: N (written to Excel)
- Keys preserved: N (kept from Excel)
- New keys added to strings.xml: N
- Updated keys in strings.xml: N
Files updated: values/strings.xml, values-zh/strings.xml, ...
```

## Key Generation Strategy

1. Check Excel first column — if empty, generate; if has value, use it
2. Analyze English text: identify button / label / message / title
3. Generate: lowercase, underscores, remove special chars, add suffix
4. Validate uniqueness against existing keys in values/strings.xml

## Supported Excel Formats

- `.xlsx` (Excel 2007+)
- `.xls` (Excel 97-2003)

Required columns: first = `key`, second = `English`, remaining = target language codes.

## Important Notes

1. **PRECISE VALUE REPLACEMENT ONLY** — do not alter surrounding lines
2. **Preserve ALL**: empty lines, comments, formatting, attributes
3. **Excel is source of truth** — all strings.xml files are driven from Excel
4. **Excel is modified** — generated keys are written back to first column
