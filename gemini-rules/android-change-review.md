# Android Change Review

Review Android code changes with a focus on runtime safety, lifecycle correctness, and regression risk. Prioritize crash paths over style-only comments.

## When to Apply

Apply this workflow when the user asks to:
- Review staged changes / code review after coding
- Review a specific commit-id or branch diff
- 检查当前修改代码 / 边界条件检查 / 崩溃风险检查 / 内存泄漏检查 / 回归检查

## Step 1 — Confirm Review Scope

| Scope | Command |
|-------|---------|
| Staged changes (after `git add .`) | `git diff --cached --stat` then `git diff --cached` |
| Unstaged working tree | `git diff --stat` then `git diff` |
| Branch vs base (PR review) | `git diff main...HEAD --stat` then `git diff main...HEAD` |
| Specific commit | `git show --stat --patch <commit-id>` |

## Step 2 — Triage Large Diffs

If diff exceeds **30 files or 600 lines**:
- **Tier 1** (review first): lifecycle classes, ViewModel, data/repo layer, navigation
- **Tier 2** (review second): adapters, custom views, service/worker classes
- **Tier 3** (skip or last): utility files, string resources, non-logic config
- Explicitly state which files were skipped

## Step 3 — Risk Checklist

### Crash / Exception Risks

- `!!` operator, platform types, nullable API response fields
- Index/position access without bounds check
- `FragmentManager` operations after state saved
- Background thread touching UI (`View`, `Fragment`, `Activity`)
- Coroutine/Flow callbacks firing after lifecycle end
- Missing permission checks before protected API calls
- `lateinit` accessed before initialization
- `requireContext()` / `requireActivity()` without lifecycle safety
- `by lazy` accessed from multiple threads without `SYNCHRONIZED`
- `object` singleton holding `Activity`/`Context` reference
- `sealed class` + `when` without `else`
- Parsing failures (JSON/Enum/date) — new Enum value not in client `when`

### Boundary Conditions

- Empty lists / empty strings / null server fields
- Zero, negative, max, overflow-sized values
- Duplicate taps / re-entrancy / repeated callbacks
- Configuration changes (rotation) and process recreation
- **Process death**: state must survive `onSaveInstanceState` → restore
- Feature flags off/on combinations
- Not-logged-in / low-balance / permission denied / network unavailable

### Regression Risks

- Changed `if` conditions or early returns
- Error handling removed or exceptions swallowed
- Order-of-operations changes (init before validate, async timing)
- Navigation route/argument changes without matching callers updated
- UI visibility or button enabled-state logic drift

## Step 4 — Android Component Hotspots

### Activity / Fragment / DialogFragment
- View binding used after `onDestroyView()`
- Observers collecting with Fragment lifecycle instead of `viewLifecycleOwner`
- `childFragmentManager` / navigation after state saved

### ViewModel / LiveData / Flow / Coroutines
- Work in `GlobalScope` or unmanaged scope
- Duplicate collectors after repeated `onStart`/`onResume`
- Exceptions in coroutine chains now uncaught after refactor

### Jetpack Compose
- `LaunchedEffect` / `DisposableEffect` keys changed incorrectly
- One-shot events triggered on every recomposition
- `remember` used where `rememberSaveable` required
- Mutable state updated from background thread

### RecyclerView / Adapter / Paging
- `adapterPosition` used without `NO_POSITION` guard
- List updates racing with click callbacks
- DiffUtil identity/content rules changed

### Navigation / Intent / Deep Link
- Destination args changed but call sites not updated
- Nullable extras now assumed non-null
- Multiple rapid navigations causing duplicate destination pushes

### Permissions / Privacy
- Runtime permission checks removed or bypassed
- "Don't ask again" permanently denied flow not handled
- API-level-specific behavior not gated with `Build.VERSION.SDK_INT`

### Room / Database
- DAO query return type nullability changed
- Migration path missing for schema change
- Enum/string mapping changes breaking old persisted values

### Memory & Resource Leaks
- `Bitmap` not recycled; `Cursor` not closed in `finally`/`use`
- `MediaPlayer`, `Camera`, `AudioTrack` not released in lifecycle callback
- `BroadcastReceiver` registered but never unregistered
- `Handler`/`HandlerThread` kept alive via anonymous `Runnable`

### ProGuard / R8
- Classes used via reflection without `@Keep` — `ClassNotFoundException` in release only
- `data class` used as JSON target with no `@SerializedName` → silent null fields in release
- `Enum` values referenced by name in serialized data renamed by R8

## Step 5 — Severity Framework

| Severity | Criteria |
|----------|----------|
| **High** | Deterministic crash; data corruption; auth/payment broken |
| **High** | Silent data loss: state not saved, wrong data persisted |
| **Medium** | Crash under race condition or edge-case input |
| **Medium** | Regression in business logic without crash |
| **Low** | Logic error with no immediate user-visible impact |
| **Low** | Test coverage gap leaving crash path unverified |

Escalate Low → Medium if finding is in payment, authentication, or data persistence path.

## Step 6 — Optional Validation Commands

```bash
./gradlew :app:compileDebugKotlin
./gradlew :app:lintDebug
./gradlew :app:testDebugUnitTest
```

Report whether these were run or skipped.

## Output Format

1. **Findings** ordered by severity (High → Medium → Low)
   - File + line reference
   - What changed / why it can crash or regress
   - Concrete trigger scenario
   - Suggested fix direction

2. **If no findings**: state "no major issues found" with residual risks noted

## Fast Triage Patterns (large diffs)

Prioritize hunks containing:
`!!` · `lateinit` · `requireContext(` · `requireActivity(` · `launch {` · `collect` · `observe` · `Fragment` · `Activity` · `onCreate` · `onDestroyView` · `NavController` · `navigate(` · `adapterPosition` · `Permission` · `registerForActivityResult` · `WorkManager` · `Room` · `Migration` · `Parcelable` · `Bitmap` · `recycle` · `close(` · `release(` · `@Keep` · `@SerializedName` · `@Singleton` · `@InstallIn` · `by lazy` · `object companion`
