# APK Analyzer

Comprehensive APK file analysis: extract metadata, classify permissions by risk level, verify signatures, inspect exported components, detect native libraries and third-party SDKs, and produce a security audit report.

## When to Apply

Apply this workflow when the user asks to:
- Analyze / inspect / parse an APK file
- Check APK permissions or signature
- Audit Android app security
- apk信息提取 / apk权限分析 / apk签名检查 / apk安全审计

## Step 1 — Basic Metadata

```bash
APK="path/to/your.apk"
aapt dump badging "$APK" | grep -E "^package:|^sdkVersion:|^targetSdkVersion:|^application-label:"
```

Extract: package name, version code/name, min SDK, target SDK, app label.

## Step 2 — Permission Audit

```bash
aapt dump permissions "$APK"
```

Classify every permission:

| Tier | Examples |
|------|---------|
| **Dangerous** | CAMERA, READ_CONTACTS, ACCESS_FINE_LOCATION, RECORD_AUDIO, READ_SMS |
| **High-Risk** | RECEIVE_BOOT_COMPLETED, SYSTEM_ALERT_WINDOW, BIND_ACCESSIBILITY_SERVICE |
| **Normal** | INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE |

## Step 3 — Signature Verification

```bash
apksigner verify --verbose --print-certs "$APK" 2>&1 | \
  grep -E "Verified|Signer|Subject|Issuer|SHA-256|Expir"
```

- Report V1 / V2 / V3 scheme usage
- Show subject, issuer, expiry, SHA-256 fingerprint
- Flag debug keystore (SHA-1: `61:ED:37:7E:85:D3:86:A8:DF:EE:6B:86:4B:D8:5B:27:44:9D:42:1D`)

## Step 4 — Manifest Component Analysis

```bash
apktool d "$APK" -o apk_out --no-src -f 2>/dev/null
grep -E "debuggable|allowBackup|cleartext|usesCleartextTraffic" apk_out/AndroidManifest.xml
grep 'exported="true"' apk_out/AndroidManifest.xml
```

Flag exported components that lack `android:permission`.

## Step 5 — Native Libraries & SDK Detection

```bash
unzip -l "$APK" | grep "\.so$"
```

Report ABIs (`armeabi-v7a`, `arm64-v8a`, `x86`, `x86_64`) and detect frameworks from lib names:
`libflutter.so` → Flutter, `libreactnativejni.so` → React Native, `libweexjss.so` → Weex

## Step 6 — Security Audit

| Check | Severity |
|-------|---------|
| `debuggable="true"` | CRITICAL |
| Debug keystore | HIGH |
| Exported component without permission | HIGH |
| `allowBackup="true"` | MEDIUM |
| Cleartext traffic permitted | MEDIUM |
| No V2/V3 signature | MEDIUM |

```bash
# Hardcoded secrets
unzip -p "$APK" "res/values/strings.xml" | grep -iE "(api_key|secret|token|password)" | head -20
```

## Output Format

```
Package:        com.example.app
Version:        1.0.0 (100)
Min SDK:        21  /  Target SDK: 34
Signature:      V1+V2+V3, Subject: CN=Example Corp, Valid Until: 2030-01-01, Debug: NO ✓
Permissions:    Dangerous(8) High-Risk(2) Normal(14)
Components:     Activities 12(2 exported) / Services 5(1 unprotected ⚠) / Receivers 3 / Providers 1
Native ABIs:    armeabi-v7a, arm64-v8a
SDKs:           Firebase, AppsFlyer, Sentry

Security Findings:
[HIGH]    Exported service without permission: .MyService
[MEDIUM]  allowBackup=true
[INFO]    debuggable=false ✓
[INFO]    No cleartext traffic ✓
```
