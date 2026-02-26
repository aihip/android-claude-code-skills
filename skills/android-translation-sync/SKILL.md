# Android Translation Sync

> Synchronize Android project multilingual resources from Excel spreadsheet. Update strings.xml files for ALL languages including English. Write generated keys to Excel first column.

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
- First row contains language headers
- **First column: "key"** (generated key for each translation)
- **Second column: "English"** (source language)
- Following columns: target languages (zh, es, fr, etc.)

**Excel format example:**

| key | English | zh | es |
|-----|---------|-----|-----|
| | Sign In | 登录 | Iniciar |
| | Welcome | 欢迎 | Bienvenido |

### 2. Generate Keys for English Text

**Key generation logic:**

| First Column (key) | Action |
|--------------------|--------|
| **Empty** | Generate new key (10-20 chars, based on English) |
| **Has value** | Use existing key (don't regenerate) |

**Key generation rules:**
- Length: 10-20 characters
- Based on English text meaning
- Format: lowercase_with_underscores
- Must not conflict with existing keys in strings.xml

Examples:
- "Sign In" → "sign_in_button"
- "Welcome to our app" → "welcome_message"
- "Settings" → "settings_title"

### 3. Write Keys to Excel First Column

**For each row:**

```
If first column (key) is empty:
    Generate key from English text
    Write key to first column
Else:
    Use existing key from first column
```

**Excel after processing:**

| key | English | zh | es |
|-----|---------|-----|-----|
| sign_in_button | Sign In | 登录 | Iniciar |
| welcome_message | Welcome | 欢迎 | Bienvenido |
| settings_title | Settings | 设置 | Configura |

### 4. Update strings.xml Files

**CRITICAL: Minimize Code Changes**

When updating strings.xml, **ONLY modify the string values that need updating**:

| Preserve | Don't Touch |
|----------|-------------|
| ✅ Empty lines | ❌ Don't remove blank lines |
| ✅ Comments (`<!-- ... -->`) | ❌ Don't remove comments |
| ✅ Original formatting | ❌ Don't reformat code |
| ✅ Original indentation | ❌ Don't change spacing |
| ✅ `translatable="false"` | ❌ Don't modify attributes |

**What to change:**
- ✅ Update the **value content** between `<string>` tags
- ✅ Append **new entries** at the bottom

**Example - ONLY update the value:**

```xml
<!-- BEFORE -->
<string name="login_title">Sign In</string>

<!-- AFTER - value updated, nothing else changed -->
<string name="login_title">登录</string>
```

**Example - Preserve everything else:**

```xml
<!-- Keep this structure intact -->
    <string name="both">الجميع</string>

    <string name="permission_open">السماح بالأذونات</string>
    <string name="permission_new_prompt">للاستمتاع بأفضل تجربة...</string>

    <string name="new_permission_settings">اذهب إلى الإعدادات</string>

    <string name="bind_tips">نصائح</string>
    <!--2018.12.27-->
    <string name="discount_percent" translatable="false">%1$d%%</string>

    <string name="remove_friend">حذف الرسائل؟</string>

    <string name="filter_company_price">/توافق</string>

    <!-- 新文案 20181228 -->
    <string name="register_go">انتقل</string>
    <string name="dialog_yes">نعم</string>

<!-- Only update the translated text, keep all empty lines and comments -->
```

**File locations:**
- `app/src/main/res/values/strings.xml` (English)
- `app/src/main/res/values-zh/strings.xml` (Chinese)
- `app/src/main/res/values-es/strings.xml` (Spanish)
- etc.

**Update rules:**

| Scenario | Action |
|----------|--------|
| Key exists | Update ONLY the value content, preserve everything else |
| Key doesn't exist | Append to bottom of file |
| File doesn't exist | Create new file in appropriate values directory |

**All languages synchronized from Excel:**
- English column → values/strings.xml
- zh column → values-zh/strings.xml
- es column → values-es/strings.xml

## Example Workflow

```bash
# Step 1: User provides Excel path
Please sync translations from: ./translations/strings_v1.2.xlsx

# Step 2: Excel BEFORE processing (key column empty):
| key | English              | zh           | es         |
|-----|----------------------|--------------|------------|
|     | Sign In              | 登录         | Iniciar    |
|     | Welcome to our app   | 欢迎使用     | Bienvenido |
|     | Settings             | 设置         | Configura  |

# Step 3: Skill processes:
# 1. Read Excel
# 2. Check if key column is empty
# 3. Generate keys for empty rows
# 4. Write keys to Excel first column
# 5. Update all strings.xml files

# Step 4: Excel AFTER processing (keys generated):
| key              | English              | zh           | es         |
|------------------|----------------------|--------------|------------|
| sign_in_button   | Sign In              | 登录         | Iniciar    |
| welcome_message  | Welcome to our app   | 欢迎使用     | Bienvenido |
| settings_title   | Settings             | 设置         | Configura  |

# Step 5: strings.xml updated:
# values/strings.xml       <- English column
# values-zh/strings.xml    <- zh column
# values-es/strings.xml    <- es column
```

## Output Summary

After processing, the skill reports:

```
Translation Sync Summary:
- Excel file: translations.xlsx
- Total rows: 45
- Keys generated: 12 (written to Excel)
- Keys existed: 28 (kept from Excel)
- New keys added to strings.xml: 12
- Updated keys in strings.xml: 28

Excel updated: /path/to/translations.xlsx
Files updated:
- values/strings.xml       (+12 new, -28 updated)
- values-zh/strings.xml    (+12 new, -28 updated)
- values-es/strings.xml    (+12 new, -28 updated)
```

## Key Generation Strategy

1. **Check Excel first column**
   - If empty → generate new key
   - If has value → use existing key

2. **Analyze English text meaning**
   - Identify if it's a button, label, message, title
   - Extract key concepts

3. **Generate candidate key**
   - Convert to lowercase
   - Replace spaces with underscores
   - Remove special characters
   - Add suffix (button, title, message, label)

4. **Validate uniqueness**
   - Check against existing keys in values/strings.xml
   - Check against other keys in Excel
   - Append number if conflict exists

## Supported Excel Formats

- `.xlsx` (Excel 2007+)
- `.xls` (Excel 97-2003)

Required columns:
- **First column: "key"** (will be generated if empty)
- **Second column: "English"** (source language)
- Following columns: target languages (zh, es, fr, de, ja, etc.)

## Important Notes

1. **MINIMIZE CODE CHANGES** - Only update string values, preserve all formatting
2. **Preserve empty lines** - Don't remove blank lines in strings.xml
3. **Preserve comments** - Keep all `<!-- ... -->` comments intact
4. **Excel is modified** - Keys are written to first column
5. **Key preservation** - If key exists in Excel, it won't be regenerated
6. **English is updated** - values/strings.xml is synced from Excel English column
7. **All languages synced** - Every language column updates its corresponding strings.xml
8. **Excel is source of truth** - All strings.xml files are updated from Excel

## Code Pattern

```python
# Process Excel and sync translations
def sync_translations(excel_file, existing_keys):
    for row in excel_file:
        # Check if key column is empty
        if row['key'].empty():
            # Generate key from English text
            english_text = row['English']
            key = generate_key(english_text, existing_keys)
            # Write key to Excel first column
            row['key'] = key
        else:
            # Use existing key from Excel
            key = row['key']

        # Update ALL language files from Excel columns
        update_strings_xml('values/strings.xml', key, row['English'])
        update_strings_xml('values-zh/strings.xml', key, row['zh'])
        update_strings_xml('values-es/strings.xml', key, row['es'])

    # Save updated Excel file
    excel_file.save()
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
