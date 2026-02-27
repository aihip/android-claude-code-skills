---
name: apk-analyzer
description: "Analyze Android APK files: extract metadata, parse AndroidManifest.xml, audit permissions, verify signatures/certificates, inspect DEX files, detect native libraries and third-party SDKs, and perform security auditing. Use when asked to analyze APK, inspect permissions, check APK signature, review manifest, audit Android app security, or perform APK 解析/安全审计."
---

# APK Analyzer

> Comprehensive APK file analysis: metadata extraction, permission auditing, signature verification, component inspection, library detection, and security assessment.

## When to Use

**Trigger phrases:**
- "analyze apk"
- "inspect apk"
- "check apk permissions"
- "verify apk signature"
- "parse android manifest"
- "audit apk security"
- "apk信息提取"
- "apk权限分析"
- "apk签名检查"
- "apk安全审计"

## Prerequisites

Install required tools:

```bash
# macOS
brew install apktool jadx

# Android SDK tools (via Android Studio or sdkmanager)
# Provides: aapt, aapt2, dexdump, apksigner

# Python tools
pip install androguard

# Verify tools
aapt version
apktool --version
apksigner --version
```

## Analysis Workflow

### Step 1 — Basic Metadata

```bash
APK="path/to/your.apk"

# Package name, version, min/target SDK, label, icon
aapt dump badging "$APK"

# Quick one-liners
aapt dump badging "$APK" | grep -E "package:|sdkVersion:|targetSdkVersion:|application-label:"
```

**Key fields to extract:**

| Field | aapt Key | Description |
|-------|----------|-------------|
| Package name | `package: name=` | Unique app identifier |
| Version code | `versionCode=` | Internal build number |
| Version name | `versionName=` | User-facing version string |
| Min SDK | `sdkVersion:` | Minimum Android version |
| Target SDK | `targetSdkVersion:` | Intended Android version |
| App label | `application-label:` | Display name |

---

### Step 2 — Permission Audit

```bash
# All declared permissions
aapt dump permissions "$APK"

# Or from decompiled manifest
apktool d "$APK" -o apk_out --no-src
cat apk_out/AndroidManifest.xml | grep "uses-permission"
```

**Classify permissions by risk level:**

#### Dangerous Permissions (require runtime grant)
```
READ_CONTACTS / WRITE_CONTACTS
READ_CALL_LOG / WRITE_CALL_LOG
CAMERA
RECORD_AUDIO
READ_EXTERNAL_STORAGE / WRITE_EXTERNAL_STORAGE
ACCESS_FINE_LOCATION / ACCESS_COARSE_LOCATION / ACCESS_BACKGROUND_LOCATION
READ_PHONE_STATE / CALL_PHONE
SEND_SMS / RECEIVE_SMS / READ_SMS
BODY_SENSORS
PROCESS_OUTGOING_CALLS
```

#### High-Risk / Sensitive Permissions
```
BIND_DEVICE_ADMIN
CHANGE_COMPONENT_ENABLED_STATE
INSTALL_PACKAGES / DELETE_PACKAGES
RECEIVE_BOOT_COMPLETED
SYSTEM_ALERT_WINDOW
WRITE_SECURE_SETTINGS
PACKAGE_USAGE_STATS
BIND_ACCESSIBILITY_SERVICE
```

#### Network Permissions
```
INTERNET
ACCESS_NETWORK_STATE
ACCESS_WIFI_STATE
CHANGE_WIFI_STATE
CHANGE_NETWORK_STATE
```

**Analysis output format:**
```
=== Permission Audit ===
Total: 24 permissions

[DANGEROUS] (8)
  ✗ READ_CONTACTS
  ✗ CAMERA
  ✗ ACCESS_FINE_LOCATION
  ...

[HIGH-RISK] (2)
  ⚠ RECEIVE_BOOT_COMPLETED
  ⚠ SYSTEM_ALERT_WINDOW

[NORMAL] (14)
  ✓ INTERNET
  ✓ ACCESS_NETWORK_STATE
  ...
```

---

### Step 3 — Signature Verification

```bash
# Verify APK signature (Android SDK apksigner)
apksigner verify --verbose "$APK"

# Show certificate details
apksigner verify --verbose --print-certs "$APK"

# Alternative: keytool (for V1 JAR signature)
keytool -printcert -jarfile "$APK"

# Check which signature schemes are used
apksigner verify --verbose "$APK" 2>&1 | grep -E "Verified using|v[0-9] scheme"
```

**Signature analysis checklist:**

| Check | Command | Expected |
|-------|---------|----------|
| V1 (JAR) signed | `apksigner verify --verbose` | Verified using v1 scheme |
| V2 (APK) signed | `apksigner verify --verbose` | Verified using v2 scheme |
| V3 signed | `apksigner verify --verbose` | Verified using v3 scheme |
| Certificate valid | `apksigner verify --print-certs` | Not expired |
| Debug keystore | Check SHA-1/SHA-256 fingerprint | Should not be debug cert |
| Self-signed | Check issuer vs subject | Issuer ≠ Subject means CA-signed |

**Debug keystore fingerprint (SHA-1):**
```
61:ED:37:7E:85:D3:86:A8:DF:EE:6B:86:4B:D8:5B:27:44:9D:42:1D
```

---

### Step 4 — Manifest Component Analysis

```bash
# Decompile resources (preserves original XML)
apktool d "$APK" -o apk_out

# View decoded manifest
cat apk_out/AndroidManifest.xml
```

**Components to audit:**

#### Activities
```bash
grep -A5 "<activity" apk_out/AndroidManifest.xml | grep -E "name=|exported=|launchMode="
```

#### Services
```bash
grep -A5 "<service" apk_out/AndroidManifest.xml | grep -E "name=|exported=|permission="
```

#### Broadcast Receivers
```bash
grep -A10 "<receiver" apk_out/AndroidManifest.xml | grep -E "name=|exported=|permission="
```

#### Content Providers
```bash
grep -A5 "<provider" apk_out/AndroidManifest.xml | grep -E "name=|exported=|readPermission=|writePermission="
```

**Security flags to check per component:**

| Flag | Risk if missing |
|------|----------------|
| `exported="false"` | Component accessible to other apps |
| `android:permission` | Unprotected exported component |
| `android:grantUriPermissions` | Potential URI permission escalation |

---

### Step 5 — DEX File Inspection

```bash
# List DEX files inside APK
unzip -l "$APK" | grep "\.dex"

# Dump DEX header info
dexdump -f "$APK"

# Class/method count per DEX
dexdump -f "$APK" | grep -E "class_defs_size|method_ids_size"

# List all classes (requires jadx or dexdump)
dexdump -l xml "$APK" | grep "class name" | head -50

# Decompile to Java source (jadx)
jadx -d jadx_out "$APK"
```

**Multi-DEX analysis:**
```bash
# Check if multidex enabled
unzip -l "$APK" | grep -c "\.dex"
# > 1 means multidex

# Inspect each DEX
for dex in $(unzip -l "$APK" | grep "\.dex" | awk '{print $4}'); do
  echo "=== $dex ==="
  unzip -p "$APK" "$dex" | dexdump -f /dev/stdin | grep -E "class_defs_size|method_ids_size"
done
```

---

### Step 6 — Native Library & SDK Detection

```bash
# List all .so files
unzip -l "$APK" | grep "\.so$"

# Extract and check architectures
unzip "$APK" "lib/*" -d apk_libs
ls apk_libs/lib/

# Inspect native libraries
file apk_libs/lib/arm64-v8a/*.so
nm -D apk_libs/lib/arm64-v8a/libexample.so 2>/dev/null | head -30
```

**Supported ABI directories:**
```
lib/armeabi-v7a/    # 32-bit ARM
lib/arm64-v8a/      # 64-bit ARM (required for Google Play since Aug 2019)
lib/x86/            # 32-bit x86
lib/x86_64/         # 64-bit x86
```

**Common third-party SDK detection (from class names or lib names):**

| Library Name Pattern | SDK |
|---------------------|-----|
| `com.google.firebase` | Firebase |
| `com.google.android.gms` | Google Play Services |
| `com.facebook.` | Facebook SDK |
| `io.branch.` | Branch.io |
| `com.appsflyer.` | AppsFlyer |
| `com.adjust.sdk` | Adjust |
| `com.bugsnag.` | Bugsnag |
| `io.sentry.` | Sentry |
| `libweexjss.so` | Weex |
| `libflutter.so` | Flutter |
| `libxwalk_core_java.so` | Crosswalk |
| `libreactnativejni.so` | React Native |

```bash
# Detect framework from native libs
ls apk_libs/lib/arm64-v8a/ | grep -E "flutter|react|weex|xamarin"

# Detect from DEX class names
jadx -d jadx_out "$APK" 2>/dev/null
find jadx_out -name "*.java" | head -5
ls jadx_out/sources/
```

---

### Step 7 — Security Audit

#### 7.1 Network Security Config
```bash
# Find network_security_config.xml
find apk_out/res -name "network_security_config.xml"
cat apk_out/res/xml/network_security_config.xml
```

**Red flags:**
```xml
<!-- DANGER: Trust all CAs including user-installed -->
<trust-anchors>
    <certificates src="user"/>
</trust-anchors>

<!-- DANGER: Allow cleartext HTTP -->
<domain-config cleartextTrafficPermitted="true">
```

#### 7.2 Exported Components Without Protection
```bash
# Find exported components (potential attack surface)
grep -B2 -A10 'exported="true"' apk_out/AndroidManifest.xml | \
  grep -v "android:permission"
```

#### 7.3 Backup Config
```bash
# Check if backups are allowed (may expose sensitive data)
grep "allowBackup" apk_out/AndroidManifest.xml
# android:allowBackup="true" is a risk for sensitive apps
```

#### 7.4 Debuggable Flag
```bash
grep "debuggable" apk_out/AndroidManifest.xml
# android:debuggable="true" must NOT be in release builds
```

#### 7.5 Hardcoded Secrets (Static Analysis)
```bash
# Search for potential API keys / tokens in strings
unzip -p "$APK" "res/values/strings.xml" | \
  grep -iE "(api_key|secret|token|password|apikey)" | head -20

# Search in decompiled source
find jadx_out -name "*.java" -exec grep -lE \
  "(API_KEY|SECRET|TOKEN|password|apiKey)" {} \; | head -10
```

#### 7.6 SSL Pinning Detection
```bash
# Check for SSL pinning implementation
grep -r "CertificatePinner\|TrustManager\|X509TrustManager\|checkServerTrusted" \
  jadx_out/sources/ 2>/dev/null | head -10
```

**Security audit output format:**
```
=== Security Audit ===

[CRITICAL]
  ✗ debuggable=true found in manifest
  ✗ Network security config allows cleartext traffic

[HIGH]
  ⚠ allowBackup=true (sensitive data may be backed up)
  ⚠ 3 exported components without permission protection

[MEDIUM]
  ~ Signed with debug keystore
  ~ No SSL pinning detected

[INFO]
  ✓ V2/V3 signature scheme used
  ✓ No hardcoded secrets found in strings.xml
```

---

### Step 8 — File Structure Summary

```bash
# Full APK content listing
unzip -l "$APK"

# Key files to check
unzip -l "$APK" | grep -E \
  "AndroidManifest|\.dex|\.so$|network_security|google-services|classes"
```

**Standard APK structure:**
```
your.apk
├── AndroidManifest.xml       # App manifest (binary XML in raw APK)
├── classes.dex               # Main DEX (compiled code)
├── classes2.dex              # MultiDex overflow
├── resources.arsc            # Compiled resources table
├── res/                      # Resources (layouts, drawables, strings)
│   ├── layout/
│   ├── drawable/
│   └── values/
├── assets/                   # Raw assets
├── lib/                      # Native libraries
│   ├── armeabi-v7a/
│   └── arm64-v8a/
├── META-INF/                 # Signature files (V1)
│   ├── MANIFEST.MF
│   ├── CERT.SF
│   └── CERT.RSA
└── kotlin/                   # Kotlin metadata (if Kotlin app)
```

---

## Full Analysis Script

```bash
#!/usr/bin/env bash
# apk-analyze.sh — Full APK analysis report
set -euo pipefail

APK="${1:?Usage: $0 <path/to/app.apk>}"
OUT_DIR="apk_analysis_$(basename "$APK" .apk)"
mkdir -p "$OUT_DIR"

echo "======================================"
echo " APK Analyzer — $(basename "$APK")"
echo "======================================"

# 1. Basic metadata
echo -e "\n[1/7] Basic Metadata"
aapt dump badging "$APK" | grep -E \
  "^package:|^sdkVersion:|^targetSdkVersion:|^application-label:"

# 2. Permissions
echo -e "\n[2/7] Permissions"
aapt dump permissions "$APK"

# 3. Signature
echo -e "\n[3/7] Signature Info"
apksigner verify --verbose --print-certs "$APK" 2>&1 | grep -E \
  "Verified|Signer|Subject|Issuer|SHA-256|Expir"

# 4. Decompile manifest & resources
echo -e "\n[4/7] Decompiling..."
apktool d "$APK" -o "$OUT_DIR/decompiled" --no-src -f 2>/dev/null

# 5. Component analysis
echo -e "\n[5/7] Exported Components"
grep 'exported="true"' "$OUT_DIR/decompiled/AndroidManifest.xml" | \
  grep -oP 'android:name="\K[^"]+' || echo "  None found"

# 6. Security flags
echo -e "\n[6/7] Security Flags"
grep -E "debuggable|allowBackup|cleartext|usesCleartextTraffic" \
  "$OUT_DIR/decompiled/AndroidManifest.xml" || echo "  No issues found"

# 7. Native libraries
echo -e "\n[7/7] Native Libraries"
unzip -l "$APK" | grep "\.so$" | awk '{print $4}' || echo "  None"

echo -e "\n======================================"
echo " Analysis complete → $OUT_DIR/"
echo "======================================"
```

---

## Python Analysis (androguard)

```python
from androguard.misc import AnalyzeAPK

apk_path = "path/to/your.apk"
a, d, dx = AnalyzeAPK(apk_path)

# Basic info
print(f"Package:     {a.get_package()}")
print(f"Version:     {a.get_androidversion_name()} ({a.get_androidversion_code()})")
print(f"Min SDK:     {a.get_min_sdk_version()}")
print(f"Target SDK:  {a.get_target_sdk_version()}")
print(f"App Name:    {a.get_app_name()}")

# Permissions
print("\nDeclared Permissions:")
for perm in a.get_permissions():
    print(f"  {perm}")

# Signature
print("\nCertificate SHA-256:")
for cert in a.get_certificates():
    print(f"  {cert.sha256_fingerprint}")

# Activities
print("\nActivities:")
for act in a.get_activities():
    print(f"  {act}")

# Services
print("\nServices:")
for svc in a.get_services():
    print(f"  {svc}")

# Exported components
print("\nExported Activities:")
for act in a.get_activities():
    filters = a.get_intent_filters("activity", act)
    if filters:
        print(f"  [EXPORTED] {act}")
```

---

## Output Report Template

After running analysis, summarize results:

```
============================================
APK Analysis Report
============================================
File:           com.example.app-1.0.apk
Package:        com.example.app
Version:        1.0.0 (100)
Min SDK:        21 (Android 5.0)
Target SDK:     34 (Android 14)
App Name:       Example App
File Size:      45.2 MB

--- Signature ---
Scheme:         V1 + V2 + V3
Subject:        CN=Example Corp, O=Example, C=US
Issuer:         CN=Example CA
SHA-256:        AA:BB:CC:...
Valid Until:    2030-01-01
Debug Cert:     NO ✓

--- Permissions (24 total) ---
Dangerous (8):  CAMERA, READ_CONTACTS, ACCESS_FINE_LOCATION, ...
High-Risk (2):  RECEIVE_BOOT_COMPLETED, SYSTEM_ALERT_WINDOW
Normal (14):    INTERNET, ACCESS_NETWORK_STATE, ...

--- Components ---
Activities:     12 (2 exported)
Services:        5 (1 exported, 1 without permission)
Receivers:       3 (2 exported)
Providers:       1 (not exported ✓)

--- Libraries ---
Native ABIs:    armeabi-v7a, arm64-v8a
SDKs detected: Firebase, AppsFlyer, Sentry

--- Security Findings ---
[HIGH]   Exported service without permission: .MyService
[MEDIUM] allowBackup=true
[INFO]   debuggable=false ✓
[INFO]   Network security config: no cleartext ✓
============================================
```

## Checklist

Before marking analysis complete:
- [ ] Basic metadata extracted (package, version, SDK levels)
- [ ] All permissions listed and classified by risk
- [ ] Signature verified and certificate details shown
- [ ] Exported components identified and assessed
- [ ] Security flags checked (debuggable, allowBackup, cleartext)
- [ ] Native libraries and SDKs listed
- [ ] Report summary produced
