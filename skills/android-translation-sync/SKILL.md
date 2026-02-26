# Android Translation Sync

> Synchronize Android project multilingual resources from Excel spreadsheet. Update strings.xml files for ALL languages including English.

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
- First row contains language headers (e.g., English, zh, es, fr)
- **English column is the SOURCE - it will be updated to values/strings.xml**
- Other language columns are translations - updated to respective values-xx/strings.xml

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

**IMPORTANT: English (values/strings.xml) is also updated from Excel!**

**File locations:**
- `app/src/main/res/values/strings.xml` (English - **UPDATED from Excel English column**)
- `app/src/main/res/values-zh/strings.xml` (Chinese - updated from Excel zh column)
- `app/src/main/res/values-es/strings.xml` (Spanish - updated from Excel es column)
- etc.

**Update rules:**

| Scenario | Action |
|----------|--------|
| Key exists in ALL language files | Update ALL values (including English) |
| Key doesn't exist | Append to bottom of ALL language files |
| File doesn't exist | Create new file in appropriate values directory |

**Key Point:**
- English text from Excel → values/strings.xml
- Chinese text from Excel → values-zh/strings.xml
- Spanish text from Excel → values-es/strings.xml
- **ALL languages are synchronized from Excel**

### 4. Output Format

```xml
<!-- values/strings.xml - Updated with English from Excel -->
<resources>
    <!-- existing entries... -->

    <!-- New/Updated translation from Excel -->
    <string name="generated_key">English text from Excel</string>
</resources>

<!-- values-zh/strings.xml - Updated with Chinese from Excel -->
<resources>
    <!-- existing entries... -->

    <!-- New/Updated translation from Excel -->
    <string name="generated_key">中文翻译</string>
</resources>
```

## Example Workflow

```bash
# User provides Excel path
Please sync translations from: ./translations/strings_v1.2.xlsx

# Excel content example:
| English              | zh           | es         |
|----------------------|--------------|------------|
| Sign In              | 登录         | Iniciar    |
| Welcome to our app   | 欢迎使用     | Bienvenido |
| Settings             | 设置         | Configura  |

# Skill will:
# 1. Read Excel file
# 2. Check existing strings.xml for duplicate keys
# 3. Generate new keys for untranslated items
# 4. Update ALL language files including English:
#    - values/strings.xml       ← English column
#    - values-zh/strings.xml    ← zh column
#    - values-es/strings.xml    ← es column
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
- values/strings.xml       (+12 new, -28 updated)  ← English updated
- values-zh/strings.xml    (+12 new, -28 updated)
- values-es/strings.xml    (+12 new, -28 updated)
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
   - Check against existing keys in values/strings.xml
   - Append number if conflict exists

## Supported Excel Formats

- `.xlsx` (Excel 2007+)
- `.xls` (Excel 97-2003)

Required columns:
- **English** (source language - will be synced to values/strings.xml)
- At least one target language (zh, es, fr, de, ja, etc.)

## Important Notes

1. **English is NOT static** - It will be updated from Excel just like other languages
2. **Excel is the source of truth** - All strings.xml files are updated from Excel
3. **If key exists** - Update the value in ALL language files
4. **If key is new** - Append to bottom of ALL language files
5. **First row = language headers** - Must include "English" and target languages

## Code Pattern

```python
# Sync all languages from Excel
def sync_translations(excel_data, existing_keys):
    results = {}

    for row in excel_data:
        # Generate key from English text
        english_text = row['English']
        key = generate_key(english_text, existing_keys)

        # Update ALL languages
        results[key] = {
            'values/strings.xml': row['English'],      # ← English updated!
            'values-zh/strings.xml': row['zh'],
            'values-es/strings.xml': row['es'],
            # ... other languages
        }

    return results
```

## Android Project Structure

```
app/src/main/res/
├── values/
│   └── strings.xml        # English - Updated from Excel English column
├── values-zh/
│   └── strings.xml        # Chinese - Updated from Excel zh column
├── values-es/
│   └── strings.xml        # Spanish - Updated from Excel es column
├── values-fr/
│   └── strings.xml        # French - Updated from Excel fr column
└── ...
```
