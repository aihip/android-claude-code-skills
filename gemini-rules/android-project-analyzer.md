# Android Project Analyzer

> Analyze an Android project codebase and produce a comprehensive technical report covering project structure, features, architecture, dependencies, code quality, and potential issues.

## When to Use

Activate when the user asks to:
- Analyze an Android project
- Review project architecture
- Audit dependencies and versions
- Assess code quality
- Produce a project health report
- 分析安卓项目 / 项目架构分析 / 依赖审计 / 代码质量分析

## Analysis Steps

### 1. Locate Project Root
Verify `settings.gradle` / `settings.gradle.kts` / `gradlew` exist. Ask user to confirm root if not found.

### 2. Project Structure & Modules
Read `settings.gradle[.kts]` for module list. Count `.kt` / `.java` files. Map directory tree (2 levels, skip `build/`).

### 3. App Metadata
Read `app/src/main/AndroidManifest.xml`. Extract: applicationId, SDK versions, permissions (classify by risk), exported components, security flags (debuggable, allowBackup, cleartext traffic).

### 4. Build Configuration & Dependencies
Read `gradle/libs.versions.toml`, root `build.gradle[.kts]`, `app/build.gradle[.kts]`. Extract every dependency with version, scope, and category. Record: Kotlin version, AGP version, JVM target, ProGuard/R8, buildFeatures.

### 5. Architecture Detection
Grep source files for MVVM/MVI/Clean Architecture signals, DI framework (Hilt/Koin/Dagger), navigation setup, Compose vs View system usage.

### 6. Feature Inventory
Identify features from modules, feature packages, Activity/Screen entry points, route declarations.

### 7. Code Quality Indicators
Count: test files, TODO/FIXME markers, `!!` force-unwraps, files >500 lines. List 5 largest files.

### 8. Potential Issues
Scan for: hardcoded secrets, cleartext HTTP, sensitive log output, WebView risks, crash-prone `!!` patterns, main thread blocking, static Context leaks, legacy library usage.

## Output Format

Produce the report with these sections:

**📱 Project Overview** — SDK versions, language, module count, file counts

**🏗️ Architecture** — detected pattern, layer separation, DI, navigation, async approach

**✨ Features** — table with feature name, entry point, package path

**📦 Dependencies** — tables grouped by category (Core / UI / Network / Database / DI / Testing / Other), each row: library | version | notes

**📊 Code Quality** — metrics table + top 5 largest files

**⚠️ Potential Issues** — findings grouped as CRITICAL / HIGH / MEDIUM / INFO, each with file:line reference

**💡 Summary & Recommendations** — top 5 prioritized action items

Always cite file paths and line numbers for findings. Write "N/A — reason" when a metric cannot be determined. Never fabricate version numbers.
