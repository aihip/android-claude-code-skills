---
name: android-change-review
description: "Review Android code changes after implementation to catch crash risks, boundary-condition bugs, and behavioral regressions before commit or merge. Use when asked to inspect staged changes after git add ., review current modified code, review a branch diff, or review a specific commit-id for issues such as null/empty handling, index bounds, lifecycle problems, threading mistakes, memory leaks, ProGuard/R8 shrinking, process death, permission gating, and new crash paths. Trigger examples include code review after coding, 检查当前修改代码, 检查指定 commit-id, 边界条件检查, 崩溃风险检查, 内存泄漏检查, 回归检查, and review staged changes for Android crash risks."
---

# Android Change Review

## Overview

Use this skill after code is written to perform a risk-focused review of Android changes.
Supports staged changes, working tree, branch diff, or a specific commit.
Prioritize runtime safety, Android lifecycle correctness, and regression risk over style-only comments.

## Review Scope

Choose the review source first:

- **Staged changes (preferred for "current changes")**
  - User has already run `git add .`
  - Review with `git diff --cached`
  - Best for pre-commit safety checks

- **Working tree changes (fallback)**
  - If changes are not staged
  - Review with `git diff`
  - Clearly state that unstaged changes can still change during review

- **Branch diff (for PR / feature branch review)**
  - User wants to review all changes since branching from base
  - Review with `git diff <base-branch>...HEAD`
  - Best for PR review before merge

- **Specific commit**
  - User provides commit hash/id
  - Review with `git show --stat --patch <commit-id>`
  - Best for regression auditing or post-merge incident analysis

## Quick Start

### A. Review Staged Changes After `git add .`

```bash
git add .
git diff --cached --stat
git diff --cached
```

### B. Review Branch Diff (All Changes vs Base)

```bash
git diff main...HEAD --stat
git diff main...HEAD
```

### C. Review a Specific Commit

```bash
git show --stat --patch <commit-id>
```

Optional narrower review:

```bash
git show <commit-id> -- app/src/main/java/.../TargetFile.kt
```

## Review Workflow

1. Confirm scope
   - Staged diff, working tree diff, branch diff, or specific commit-id
   - If commit review, confirm exact hash when ambiguous

2. Load the diff before reading full files
   - Start from `--stat` to see file spread and risk areas
   - If diff exceeds 30 files or 600 lines, triage by risk: prioritize lifecycle/state/data files over utility/resource files; explicitly state which files were skipped
   - Then inspect patch hunks for changed conditions, null checks, thread/lifecycle usage

3. Review for runtime safety and regressions (highest priority first)
   - Crash paths and boundary conditions
   - ANR / main-thread blocking risk
   - Memory and resource leaks
   - Behavioral regressions
   - For each Android component type touched in the diff (Activity, Fragment, ViewModel, Compose, RecyclerView, Room, etc.), apply the corresponding hotspot section below

4. Read surrounding code only where needed
   - Expand to nearby functions/classes when a patch changes control flow, state, lifecycle, or async behavior

5. Report findings ordered by severity
   - Include file/line references
   - Explain why it can crash/regress and a concrete trigger scenario

## Risk Checklist (Android-Focused)

### Crash / Exception Risks

Check whether the change can introduce new crash paths:

- Nullability mismatches (`!!`, platform types, nullable API response fields)
- Index/position access (`list[index]`, adapter positions, cursor positions)
- Illegal state timing (`FragmentManager` state saved, duplicate navigation, lifecycle race)
- Class cast / type assumptions after refactor
- Background thread touching UI (`View`, `Fragment`, `Activity`)
- Coroutine/Flow callbacks firing after lifecycle end
- Missing permission checks before protected API calls
- Resource/context usage when `Activity`/`Fragment` is detached or destroyed
- Parsing failures (JSON/Int/Long/Enum/date parsing) after format changes — including new backend Enum value not in client `when` expression
- `lateinit` fields accessed before initialization
- `requireContext()` / `requireActivity()` / `requireArguments()` used without lifecycle safety
- Kotlin `by lazy` delegate accessed from multiple threads without `SYNCHRONIZED` mode
- `object` singleton holding `Activity`/`Context` reference (context leak + stale reference)
- `sealed class` + `when` without `else` — new subclass added silently falls through

### Boundary Conditions

Validate input and state boundaries, especially when conditions changed:

- Empty lists / empty strings / null server fields
- Zero, negative, max, overflow-sized values
- First item / last item / single item collections
- Timeout/retry edge behavior
- Duplicate taps / re-entrancy / repeated callbacks
- Configuration changes (rotation) and process recreation
- **Process death**: "Don't keep activities" enabled — does state survive `onSaveInstanceState` → restore?
  - `ViewModel` used where needed? `SavedStateHandle` used for transient UI state?
  - Deep link launched cold without backstack — does destination assume stack exists?
- Feature flags off/on combinations
- Not-logged-in / low-balance / permission denied / network unavailable states

### Regression Risks

Look for behavior changes that may not crash but can break flow:

- Changed `if` conditions or early returns
- Default value changes
- Error handling removed or exceptions swallowed
- Order-of-operations changes (init before validate, async timing changes)
- State reset/cleanup omitted
- Return value semantics changed
- UI visibility or button enabled-state logic drift
- Navigation route/argument changes without matching callers

## Android Component Hotspots (Extra Focus)

### Activity / Fragment / DialogFragment

Check for lifecycle and UI timing mistakes:

- View binding used after `onDestroyView()` in Fragment
- Observers collecting with Fragment lifecycle instead of `viewLifecycleOwner`
- `childFragmentManager` / navigation operations after state is saved
- `arguments` keys changed but callers still pass old names/types
- Result callbacks not re-registered after configuration change
- Dialog show/dismiss calls racing with lifecycle transitions

### ViewModel / LiveData / Flow / Coroutines

Check async state and cancellation behavior:

- Work launched in wrong scope (`GlobalScope`, unmanaged scope, missing cancellation)
- `viewModelScope`/`lifecycleScope` misuse causing leaks or lost work
- Flow collection without lifecycle awareness
- Duplicate collectors after repeated `onStart` / `onResume`
- State updates from background thread to non-thread-safe objects
- Exceptions in coroutine chains now uncaught after refactor

### Jetpack Compose (if touched)

Check Compose-specific runtime/regression risks:

- `LaunchedEffect` / `DisposableEffect` keys changed and now re-run incorrectly
- Navigation or one-shot events triggered on every recomposition
- `remember` used where `rememberSaveable` is required (state loss regression)
- Collecting flows without lifecycle-aware APIs when needed
- Mutable state updated from background thread
- `derivedStateOf` / state transformations causing stale UI or infinite recomposition loops

### RecyclerView / Adapter / Paging

Common crash and edge-case sources:

- `adapterPosition` / `bindingAdapterPosition` used without `NO_POSITION` guard
- List updates racing with click callbacks
- DiffUtil identity/content rules changed (incorrect item updates)
- Paging load states not handled for empty/error/retry paths
- Item count assumptions break on empty/one-item lists

### Navigation / Intent / Deep Link

Check route and argument safety:

- Destination args changed but call sites not updated
- Nullable extras now assumed non-null
- Deep-link parsing without validation
- Multiple rapid navigations causing duplicate destination pushes
- `PendingIntent` flags missing or incorrect for current targetSdk

### Permissions / Privacy / OS Restrictions

Android-specific gating checks:

- Runtime permission checks removed, moved, or bypassed
- "Denied once" / "Don't ask again" / permanently denied flows not handled
- Background location / notification / media permissions edge cases
- API-level-specific permission behavior not gated (`Build.VERSION.SDK_INT`)
- Feature call still reachable when permission or service is unavailable

### Services / WorkManager / Background Work

Check background execution and process/lifecycle resilience:

- Foreground service start timing/notification requirements broken
- Work constraints changed (network/charging/idle) causing unexpected execution
- Retry/backoff logic removed or changed
- Duplicate scheduled work due to missing unique work policy
- Broadcast/worker code assuming process state or in-memory cache exists

### Room / Database / Data Layer

Check schema and data assumptions:

- DAO query return type nullability changed
- Migration path missing for schema change
- Transaction boundary changed causing partial writes
- Empty query results no longer handled
- Enum/string mapping changes breaking old persisted values

### Memory & Resource Leaks

Common sources of OOM crashes and long-term degradation:

- `Bitmap` not recycled in `onDraw()`, `onBindViewHolder()`, or image callbacks; use `Glide`/`Coil` recycle helpers
- `Cursor` from `ContentResolver` or raw `Room` query not closed in `finally`/`use` block
- `InputStream`/`OutputStream` not closed — check for missing `use {}` block
- `MediaPlayer`, `AudioTrack`, `Camera`/`Camera2` not released in correct lifecycle callback
- `BroadcastReceiver` registered in `onResume()` but unregistered only in `onStop()` → double-registration risk; or registered but never unregistered
- `AnimatorSet`/`ObjectAnimator` holding a `View` reference after detach, preventing GC
- `Handler`/`HandlerThread` kept alive beyond scope via anonymous `Runnable`; use `WeakReference` or cancel in `onDestroy()`
- `object` companion/singleton holding `Activity` or non-application `Context`
- `registerReceiver` without corresponding `unregisterReceiver` in teardown path

### Dependency Injection / Multi-Module (Hilt / Dagger)

Check component scoping and binding correctness:

- `@Module` binding removed but consumer still has `@Inject` for it → compile passes, runtime crash
- `@Singleton` applied to a component that depends on `Activity` context → scope leak
- `@ActivityRetainedScoped` vs `@ViewModelScoped` confusion causing ViewModel outliving or underliving expected scope
- `@InstallIn(SingletonComponent::class)` on a module that should be per-Activity or per-Fragment
- Navigation Safe Args type change in one module but consuming module has stale generated class until clean build
- Gradle `api` → `implementation` change in a library module silently breaks consuming module compile without visible diff in app module

### ProGuard / R8 Shrinking

Release-build-only crashes — must check whenever serialization, reflection, or Parcelable is touched:

- Classes used via `Class.forName()` or reflection without `@Keep` or keep rule → `ClassNotFoundException` in release only
- Kotlin `data class` used as JSON deserialization target (Gson/Moshi/kotlinx.serialization) where fields have no `@SerializedName` → obfuscated names → silent `null` fields
- `Enum` values referenced by name in serialized data that are renamed by R8
- `@JsonAdapter` or custom `TypeAdapter` registered by class type that is renamed
- `Parcelable` in inner/anonymous class not surviving shrinking
- New serializable/reflective class added without updating `proguard-rules.pro` or `consumer-rules.pro`

### Manifest / Resources / Config

Android integration regressions often land here:

- `android:exported` / intent-filter combinations invalid on newer SDKs
- Component names / authorities / actions changed without callers updated
- Resource key/type changes (`string` → `plurals`, formatting placeholders mismatch `%s/%d`)
- Missing localized resource fallback assumptions
- Proguard/R8 keep rules not updated after reflection/serialization changes

## Android-Specific Diff Heuristics (Fast Triage)

When the diff is large, prioritize hunks containing these patterns:

- `!!`, `lateinit`, `requireContext(`, `requireActivity(`, `as `
- `launch {`, `async`, `withContext`, `collect`, `observe`, `postValue`
- `Fragment`, `Activity`, `onCreate`, `onStart`, `onResume`, `onDestroyView`
- `NavController`, `findNavController`, `navigate(`
- `adapterPosition`, `bindingAdapterPosition`, `DiffUtil`
- `Permission`, `requestPermissions`, `ActivityResult`, `registerForActivityResult`
- `WorkManager`, `Worker`, `Service`, `Foreground`
- `Room`, `Migration`, `Parcelable`, `Intent`, `PendingIntent`
- `Bitmap`, `recycle`, `cursor`, `close(`, `release(`, `unregister`
- `@Keep`, `@SerializedName`, `proguard`, `consumer-rules`
- `@Singleton`, `@InstallIn`, `@HiltViewModel`, `@Inject`
- `by lazy`, `object companion`, `object :`

**Large diff strategy (>30 files or >600 lines):**

1. Review files by risk tier first:
   - Tier 1 (review first): lifecycle classes, ViewModel, data/repo layer, navigation
   - Tier 2 (review second): adapters, custom views, service/worker classes
   - Tier 3 (review last or skip): utility files, string resources, non-logic config
2. Explicitly state which files were reviewed and which were skipped due to diff size
3. If scope was reduced, recommend a follow-up review on skipped files

## Severity Decision Framework

Use these criteria when assigning severity to findings:

| Severity | Criteria |
|----------|----------|
| **High** | Crash reproducible deterministically on any device or common user path; data corruption; auth/payment flow broken |
| **High** | Silent data loss: state not saved, wrong data persisted, wrong item deleted |
| **Medium** | Crash only under race condition, specific device, or edge-case input; wrong fallback behavior visible to user |
| **Medium** | Regression in business logic that does not crash but produces incorrect output |
| **Low** | Logic error with no immediate user-visible impact; maintainability gap increasing future risk |
| **Low** | Test coverage gap that leaves a crash path unverified |

Escalate Low → Medium if the finding is in a payment, authentication, or data persistence path.

## Optional Validation Commands (After Review Findings)

When useful and available, run targeted checks to increase confidence:

```bash
# Narrow compile checks (module/task depends on project)
./gradlew :app:compileDebugKotlin
./gradlew :app:compileDebugJavaWithJavac

# Lint / unit tests (prefer impacted module)
./gradlew :app:lintDebug
./gradlew :app:testDebugUnitTest
```

Use targeted tasks when the project is large. Report if checks were not run.

## Commands Reference

Use these commands depending on scope:

```bash
# Staged review (preferred after user runs git add .)
git diff --cached --name-only
git diff --cached --stat
git diff --cached

# Working tree review (if not staged)
git diff --name-only
git diff --stat
git diff

# Branch / PR review (all changes vs base branch)
git diff main...HEAD --stat
git diff main...HEAD

# Commit review
git show --name-only --stat <commit-id>
git show --stat --patch <commit-id>
```

## Output Format (Recommended)

When reporting review results:

1. Findings first (severity ordered)
   - `High`: likely crash / data corruption / major regression
   - `Medium`: edge-case breakage, flaky behavior, incorrect fallback
   - `Low`: maintainability/test gap that increases future risk

2. For each finding include
   - File + line reference
   - What changed
   - Why it can crash/regress
   - Concrete trigger/boundary scenario
   - Suggested fix direction (brief)

3. If no findings
   - State no major issues found in reviewed diff
   - Mention residual risks (for example: no runtime test executed, no process-death simulation, no release-build ProGuard verification, no device matrix validation)

## Example Requests

- "代码写完了，帮我做代码检查，我已经 `git add .` 了，重点看会不会 crash。"
- "请检查当前修改代码的边界条件和回归风险。"
- "我已经 git add . 了，帮我按 Android 生命周期/权限/线程角度做一轮代码检查。"
- "Review my staged changes for Android crash risks."
- "Review this Compose/Fragment change for lifecycle and recomposition regressions."
- "帮我检查 commit `abc1234`，看有没有新的崩溃路径。"
- "Review commit-id for boundary conditions and regressions."
- "帮我检查这个 branch 的所有修改，看有没有内存泄漏和 ProGuard 问题。"
- "Review all changes on this feature branch before PR merge."

## Checklist

Before finishing the review:

- [ ] Confirm review scope (staged / working tree / branch diff / commit-id)
- [ ] Inspect diff patch, not only filenames; apply large-diff triage strategy if needed
- [ ] Apply crash risk checklist (nullability, index, lifecycle, Kotlin traps)
- [ ] Apply boundary conditions checklist (empty/null/zero/process death/config change)
- [ ] Apply regression risk checklist (logic drift, state cleanup, return values)
- [ ] For each Android component type touched (Activity/Fragment/ViewModel/Compose/RecyclerView/Room/Service/etc.), apply corresponding hotspot section
- [ ] Check memory & resource leak patterns if any resource allocation or lifecycle changes are present
- [ ] Check DI/multi-module section if Hilt/Dagger annotations or module structure changed
- [ ] Check ProGuard/R8 section if any serialization, Parcelable, or reflection-based class is added/renamed/removed
- [ ] Check state restoration risk (process death / `onSaveInstanceState`) for any state management change
- [ ] Note whether validation commands (`./gradlew`) were run or skipped and why
- [ ] Report findings with file/line references, or explicitly state no findings with residual risk note
