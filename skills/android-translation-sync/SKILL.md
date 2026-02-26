# Android Translation Sync

> Synchronize Android project multilingual resources from Excel spreadsheet. Update strings.xml files based on English translations.

## When to Use

**Trigger phrases:**
- "sync translations from excel"
- "update android strings from excel"
- "多语言翻译同步"
- "更新strings.xml"
- "android translation sync"

## Usage

Provide the Excel file path:

```
Please update translations from: /path/to/translations.xlsx
```

## Process

### 1. Read Excel Spreadsheet

- Parse the Excel file provided
- Identify columns: English and other languages (zh, es, fr, etc.)
- First row contains language headers

### 2. Generate Keys for English Text

For new translations (key doesn't exist):

```
Key generation rules:
- Length: 10-20 characters
- Based on English text meaning
- Format: lowercase_with_underscores
- Must not conflict with existing keys in strings.xml
```

Examples:
- "Sign In" → "sign_in_button"
- "Welcome to our app" → "welcome_message"
- "Settings" → "settings_title"

### 3. Update strings.xml Files

**File locations:**
- `app/src/main/res/values/strings.xml` (default/English)
- `app/src/main/res/values-zh/strings.xml` (Chinese)
- `app/src/main/res/values-es/strings.xml` (Spanish)
- etc.

**Update rules:**

| Scenario | Action |
|----------|--------|
| Key exists | Update the value |
| Key doesn't exist | Append to bottom of file |
| File doesn't exist | Create new file in appropriate values directory |

### 4. Output Format

```xml
<!-- New entries appended at bottom -->
<resources>
    <!-- existing entries... -->

    <!-- New translation from Excel -->
    <string name="generated_key">Translated text</string>
</resources>
```

## Example Workflow

```bash
# User provides Excel path
Please sync translations from: ./translations/strings_v1.2.xlsx

# Skill will:
# 1. Read Excel file
# 2. Check existing strings.xml for duplicate keys
# 3. Generate new keys for untranslated items
# 4. Update all language files
# 5. Report changes made
```

## Output Summary

After processing, the skill reports:

```
Translation Sync Summary:
- Processed: translations.xlsx
- Total entries: 45
- New keys added: 12
- Updated keys: 28
- Skipped (unchanged): 5

Files updated:
- values/strings.xml (+12 new, -28 updated)
- values-zh/strings.xml (+12 new, -28 updated)
- values-es/strings.xml (+12 new, -28 updated)
```

## Key Generation Strategy

1. **Analyze English text meaning**
   - Identify if it's a button, label, message, title
   - Extract key concepts

2. **Generate candidate key**
   - Convert to lowercase
   - Replace spaces with underscores
   - Remove special characters
   - Add suffix (button, title, message, label)

3. **Validate uniqueness**
   - Check against existing keys
   - Append number if conflict exists

## Supported Excel Formats

- `.xlsx` (Excel 2007+)
- `.xls` (Excel 97-2003)

Required columns:
- English (source language)
- At least one target language (zh, es, fr, de, ja, etc.)

## Code Pattern

```python
# Key generation pattern
def generate_key(english_text, existing_keys):
    # Extract meaningful words
    words = english_text.lower().split()[:3]

    # Build base key
    base_key = "_".join(words)

    # Add appropriate suffix
    suffix = detect_type(english_text)  # button, label, etc.
    key = f"{base_key}_{suffix}"

    # Ensure uniqueness
    counter = 1
    while key in existing_keys:
        key = f"{base_key}_{suffix}_{counter}"
        counter += 1

    return key
```

## Android Project Structure

```
app/src/main/res/
├── values/
│   └── strings.xml        # Default (English)
├── values-zh/
│   └── strings.xml        # Chinese
├── values-es/
│   └── strings.xml        # Spanish
├── values-fr/
│   └── strings.xml        # French
└── ...
```
