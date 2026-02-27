---
name: android-project-analyzer
description: "Analyze an Android project codebase to produce a comprehensive report covering: project structure and modules, feature inventory, architecture pattern (MVVM/MVI/MVP/Clean Architecture), dependency list with versions, build configuration, code quality indicators, and potential issues. Use when asked to analyze an Android project, understand its architecture, audit dependencies, review project health, assess code quality, or produce a technical overview. Trigger phrases: analyze android project, project architecture review, dependency audit, 分析安卓项目, 项目架构分析, 依赖审计, 代码质量分析."
---

# Android Project Analyzer

> Produce a full technical report of an Android project: structure, features, architecture, dependencies, code quality, and potential issues.

## When to Use

**Trigger phrases:**
- "analyze android project"
- "analyze this project"
- "project architecture review"
- "what does this project do"
- "dependency audit"
- "code quality review"
- "project health check"
- "分析安卓项目"
- "项目架构分析"
- "依赖审计"
- "代码质量分析"
- "项目健康检查"

## Analysis Workflow

Run all steps in order. Each step feeds context into the next.

---

### Step 1 — Locate Project Root

Verify you are in the Android project root. Look for these markers:

```bash
ls settings.gradle settings.gradle.kts build.gradle build.gradle.kts gradlew 2>/dev/null
```

If not found, ask the user to confirm the project root path before continuing.

---

### Step 2 — Project Structure & Modules

```bash
# Top-level layout
ls -la

# All Gradle module declarations
cat settings.gradle 2>/dev/null || cat settings.gradle.kts 2>/dev/null

# Count source files by type
find . -name "*.kt" -not -path "*/.git/*" | wc -l
find . -name "*.java" -not -path "*/.git/*" | wc -l
find . -name "*.xml" -not -path "*/.git/*" -not -path "*/build/*" | wc -l

# Directory tree (2 levels, skip build artifacts)
find . -maxdepth 2 -type d \
  -not -path "*/.git/*" \
  -not -path "*/build/*" \
  -not -path "*/.gradle/*" \
  -not -path "*/node_modules/*"
```

**Extract:**
- Module list (`:app`, `:core`, `:feature:*`, etc.)
- Primary language (Kotlin / Java / mixed)
- Rough project size (file counts)

---

### Step 3 — App Metadata

```bash
# App-level manifest
find . -name "AndroidManifest.xml" -not -path "*/build/*" | head -5

# Read the main app manifest
cat app/src/main/AndroidManifest.xml 2>/dev/null || \
  cat $(find . -path "*/main/AndroidManifest.xml" -not -path "*/build/*" | head -1)
```

**Extract:**
- `package` / `applicationId`
- `minSdkVersion`, `targetSdkVersion`, `compileSdkVersion`
- All declared permissions — categorize as Dangerous / Normal / Signature
- Exported Activities, Services, Receivers, Providers
- `android:debuggable`, `android:allowBackup`, `android:usesCleartextTraffic`

---

### Step 4 — Build Configuration & Dependencies

```bash
# Version catalog (modern projects)
cat gradle/libs.versions.toml 2>/dev/null

# Root build file
cat build.gradle 2>/dev/null || cat build.gradle.kts 2>/dev/null

# App module build file
cat app/build.gradle 2>/dev/null || cat app/build.gradle.kts 2>/dev/null

# All module build files
find . -name "build.gradle" -o -name "build.gradle.kts" \
  | grep -v "^./build/" | grep -v "/.gradle/" \
  | xargs grep -l "dependencies" 2>/dev/null
```

**Extract for each dependency (implementation / api / kapt / ksp / testImplementation):**

| Column | Example |
|---|---|
| Group | `androidx.compose.ui` |
| Artifact | `ui` |
| Version | `1.6.0` |
| Scope | `implementation` |
| Category | UI / DI / Network / Database / Testing / etc. |

Also record:
- Kotlin version
- AGP (Android Gradle Plugin) version
- Java / JVM target version
- Build types (debug / release) and signing config presence
- ProGuard / R8 enabled?
- `buildFeatures` (Compose, ViewBinding, DataBinding, BuildConfig)

---

### Step 5 — Architecture Detection

```bash
# Architecture pattern signals
grep -r "ViewModel\|StateFlow\|LiveData\|MutableStateFlow" \
  --include="*.kt" -l --exclude-dir=build 2>/dev/null | head -20

grep -r "UseCase\|Interactor\|Repository\|DataSource" \
  --include="*.kt" -l --exclude-dir=build 2>/dev/null | head -20

grep -r "UiState\|UiEvent\|UiEffect\|Intent\|Action\|Reducer" \
  --include="*.kt" -l --exclude-dir=build 2>/dev/null | head -20

# DI framework
grep -r "@HiltAndroidApp\|@AndroidEntryPoint\|@HiltViewModel" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | head -5
grep -r "startKoin\|KoinComponent\|single {" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | head -5
grep -r "@Module\|@Component\|@Inject" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | head -5

# Navigation
grep -r "NavController\|NavHost\|NavGraph\|@Destination" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | head -5
grep -r "findNavController\|Navigation.findNavController" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | head -5

# UI layer
grep -r "@Composable" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | wc -l
grep -r "Fragment\|Activity" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | head -10

# Layer package structure
find . -type d \( \
  -name "ui" -o -name "presentation" \
  -o -name "domain" -o -name "data" \
  -o -name "repository" -o -name "usecase" \
  -o -name "viewmodel" -o -name "model" \
  -o -name "network" -o -name "database" \
  \) -not -path "*/build/*" 2>/dev/null
```

**Determine:**
- Architecture pattern: Clean Architecture / MVVM / MVI / MVP / mixed
- Layer separation quality: strict / partial / flat
- DI framework: Hilt / Koin / Dagger / manual / none
- Navigation: Navigation Component / manual Fragment transactions / Compose Navigation
- UI paradigm: Jetpack Compose / View system / mixed

---

### Step 6 — Feature Inventory

```bash
# Feature modules (multi-module projects)
cat settings.gradle 2>/dev/null | grep "feature"

# Feature packages (single-module projects)
find . -type d -not -path "*/build/*" -not -path "*/.git/*" \
  | grep -E "feature|screen|module" | head -30

# Entry points — Activities and top-level Composables
grep -r "AppCompatActivity\|ComponentActivity\|FragmentActivity" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null

grep -r "@Composable" --include="*.kt" -l --exclude-dir=build 2>/dev/null \
  | xargs grep -l "fun [A-Z][a-zA-Z]*Screen\b" 2>/dev/null | head -20

# Deep link / route declarations
grep -r "deepLink\|@DeepLink\|navDeepLink\|route = " \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | head -10
```

**List discovered features** with their entry-point file and package path.

---

### Step 7 — Code Quality Indicators

```bash
# Test coverage surface
find . -path "*/test/*.kt" -not -path "*/build/*" | wc -l
find . -path "*/androidTest/*.kt" -not -path "*/build/*" | wc -l
find . -path "*/test/*.kt" -not -path "*/build/*" | head -20

# Large files (complexity risk)
find . -name "*.kt" -not -path "*/build/*" \
  | xargs wc -l 2>/dev/null \
  | sort -rn | head -20

# God classes / bloated files (>500 lines)
find . -name "*.kt" -not -path "*/build/*" \
  | xargs wc -l 2>/dev/null \
  | awk '$1 > 500 {print $1, $2}' | sort -rn

# TODO / FIXME / HACK markers
grep -r "TODO\|FIXME\|HACK\|XXX" \
  --include="*.kt" --include="*.java" \
  -n --exclude-dir=build 2>/dev/null | wc -l

grep -r "TODO\|FIXME\|HACK" \
  --include="*.kt" --include="*.java" \
  -n --exclude-dir=build 2>/dev/null | head -20

# Hardcoded strings in code (i18n debt)
grep -r "\"[A-Za-z ]\{10,\}\"" \
  --include="*.kt" -n --exclude-dir=build \
  --exclude-dir=test --exclude-dir=androidTest 2>/dev/null | wc -l

# Deprecated API usage
grep -r "@Deprecated\|\.deprecated\b" \
  --include="*.kt" -rl --exclude-dir=build 2>/dev/null | head -10
```

---

### Step 8 — Potential Issues Detection

Run each check and record findings with file + line reference.

#### 8a. Security Issues

```bash
# Hardcoded secrets / credentials
grep -rn "password\s*=\s*\"\|api_key\s*=\s*\"\|apiKey\s*=\s*\"\|secret\s*=\s*\"" \
  --include="*.kt" --include="*.java" --include="*.xml" \
  --exclude-dir=build --exclude-dir=test 2>/dev/null | grep -v "//.*password"

# Cleartext HTTP
grep -rn "http://" --include="*.kt" --include="*.java" \
  --exclude-dir=build 2>/dev/null | grep -v "localhost\|127.0.0.1\|//schemas\|//xmlns"

# Logging sensitive data
grep -rn "Log\.\(d\|i\|v\|w\|e\).*password\|Log\.\(d\|i\|v\|w\|e\).*token\|Log\.\(d\|i\|v\|w\|e\).*secret" \
  --include="*.kt" --include="*.java" --exclude-dir=build 2>/dev/null

# WebView security
grep -rn "setJavaScriptEnabled(true)\|addJavascriptInterface\|setAllowFileAccess(true)" \
  --include="*.kt" --include="*.java" --exclude-dir=build 2>/dev/null
```

#### 8b. Stability Issues

```bash
# Force unwrap / non-null assertion (crash risk)
grep -rn "!!" --include="*.kt" --exclude-dir=build \
  --exclude-dir=test --exclude-dir=androidTest 2>/dev/null | wc -l

grep -rn "!!" --include="*.kt" --exclude-dir=build \
  --exclude-dir=test --exclude-dir=androidTest 2>/dev/null | head -20

# Unsafe casts
grep -rn " as [A-Z]" --include="*.kt" --exclude-dir=build 2>/dev/null | head -10

# Network on main thread risk
grep -rn "runBlocking\b" --include="*.kt" --exclude-dir=build 2>/dev/null | head -10

# SharedPreferences on main thread
grep -rn "getSharedPreferences\|PreferenceManager" \
  --include="*.kt" --exclude-dir=build 2>/dev/null | head -10
```

#### 8c. Performance Issues

```bash
# Memory leak patterns
grep -rn "companion object.*context\|object.*Context\b\|static.*Context" \
  --include="*.kt" --include="*.java" --exclude-dir=build 2>/dev/null | head -10

# Overdraw / nested layouts in XML
find . -name "*.xml" -path "*/layout/*" -not -path "*/build/*" \
  | xargs grep -l "LinearLayout.*LinearLayout\|RelativeLayout.*RelativeLayout" 2>/dev/null | head -10

# Large bitmap operations on main thread
grep -rn "BitmapFactory.decodeFile\|BitmapFactory.decodeStream" \
  --include="*.kt" --include="*.java" --exclude-dir=build 2>/dev/null | head -10
```

#### 8d. Outdated / Deprecated Dependencies

For each dependency found in Step 4, check:
- Is the version pinned to an old major version?
- Does the library have a known successor? (e.g., `RxJava` → `Coroutines`, `Volley` → `Retrofit/Ktor`, `AsyncTask` removed, `com.android.support` → `androidx`)
- Is `minSdkVersion` still meaningful for the targetSdkVersion?

---

### Step 9 — Compose Output Report

Produce the final report in this exact structure:

---

## 📱 Project Overview

| Field | Value |
|---|---|
| Application ID | |
| Package Name | |
| Min SDK | |
| Target SDK | |
| Compile SDK | |
| Kotlin Version | |
| AGP Version | |
| Language | |
| Total Kotlin Files | |
| Total Java Files | |

---

## 🏗️ Architecture

- **Pattern**: (Clean Architecture / MVVM / MVI / MVP / mixed)
- **Layer Separation**: (strict / partial / flat)
- **DI Framework**: (Hilt / Koin / Dagger / manual / none)
- **Navigation**: (Navigation Component / Compose Navigation / manual)
- **UI Paradigm**: (Jetpack Compose / View system / mixed)
- **Async**: (Coroutines + Flow / RxJava / mixed)

**Module Structure:**
```
(list each Gradle module and its responsibility)
```

---

## ✨ Features

| Feature | Entry Point | Package |
|---|---|---|
| (feature name) | (Activity / Screen composable) | (package path) |

---

## 📦 Dependencies

### Core
| Library | Version | Category | Notes |
|---|---|---|---|

### UI
| Library | Version | Category | Notes |
|---|---|---|---|

### Network
| Library | Version | Category | Notes |
|---|---|---|---|

### Database / Storage
| Library | Version | Category | Notes |
|---|---|---|---|

### DI
| Library | Version | Category | Notes |
|---|---|---|---|

### Testing
| Library | Version | Category | Notes |
|---|---|---|---|

### Other
| Library | Version | Category | Notes |
|---|---|---|---|

---

## 📊 Code Quality

| Metric | Value | Assessment |
|---|---|---|
| Unit test files | | ✅ / ⚠️ / ❌ |
| Instrumented test files | | ✅ / ⚠️ / ❌ |
| TODO / FIXME markers | | |
| Force unwrap (`!!`) count | | ✅ / ⚠️ / ❌ |
| Files > 500 lines | | ✅ / ⚠️ / ❌ |
| Hardcoded UI strings (approx.) | | |

**Top 5 largest files:**
```
(file path — N lines)
```

---

## ⚠️ Potential Issues

Group findings by severity:

### 🔴 CRITICAL
- (issue) — `file:line`

### 🟠 HIGH
- (issue) — `file:line`

### 🟡 MEDIUM
- (issue) — `file:line`

### 🔵 INFO / Recommendations
- (observation or improvement suggestion)

---

## 💡 Summary & Recommendations

1–5 prioritized action items the team should address first, with rationale.

---

## Output Rules

- Always include file paths and line numbers for concrete findings.
- If a metric cannot be determined (e.g., no Gradle file found), state "N/A — reason" rather than guessing.
- Do not fabricate dependency versions; read them directly from build files.
- Keep the report factual and scannable — avoid lengthy prose paragraphs.
- If the project is large (>200 Kotlin files), sample representative files rather than reading every file; note this in the report.
