# Figma to Android Native Code

Convert Figma design data (node JSON, layer descriptions, annotations, screenshots) into production-ready Android native XML + Kotlin code with 1:1 visual fidelity.

## When to Apply

Apply this workflow when the user asks to:
- Convert Figma design to Android native code
- Generate Android XML/Kotlin from design data
- figma 转 android / figma 生成代码 / 设计稿转代码 / 还原设计稿

## Hard Constraints

1. **Android native View system ONLY** — XML layouts + Kotlin + ViewBinding.
2. **Jetpack Compose is strictly forbidden** — no `@Composable`, `Modifier`, `Material3 Compose`, or `Preview`.
3. **No pseudo-code** — output must be complete, runnable, and maintainable.

## Conversion Workflow

### Step 1 — Page Structure Analysis

Identify page type, component hierarchy, scrollable vs fixed regions, repeating items (→ RecyclerView), and reusable modules (→ `<include>`).

### Step 2 — Output Directory Structure

List all files: `res/layout/`, `res/drawable/`, `res/values/`, Activity/Fragment/Adapter Kotlin files.

### Step 3 — Generate Code (Strict Order)

1. XML layout (main page)
2. RecyclerView item XML
3. Sub-layout XML (`<include>` modules)
4. Drawable XML (shapes, selectors, gradients)
5. Resource values (colors.xml, dimens.xml, strings.xml additions)
6. Kotlin code (Activity/Fragment, Adapter/ViewHolder, data classes)

Every code block MUST include file path header.

### Step 4 — Risk Notes

Output risks: effects not fully inferred, missing assets, interactions needing business logic, screen adaptation.

## Layout Rules

- Root: prefer `ConstraintLayout`
- Position: constraints, margins, padding, gravity, `layout_weight`, guideline, barrier — never absolute coords
- Units: `dp` / `sp` only, never `px`
- Resources: colors → `colors.xml`, dimensions → `dimens.xml`, shapes → `drawable/`
- Lists: always `RecyclerView` + separate `item_xxx.xml`
- Scrolling: correctly distinguish `ScrollView` / `NestedScrollView` / `RecyclerView`

## Naming Conventions

- View IDs: `tv_title`, `iv_avatar`, `btn_submit`, `rv_list`
- Colors: `color_primary`, `color_text_main`, `color_divider`
- Dimensions: `dp_4`, `dp_8`, `text_14sp`, `radius_8`
- Drawables: `bg_card_white_radius_12`, `shape_btn_primary`, `ic_arrow_right`

## Code Style

- Kotlin first, ViewBinding (no DataBinding, no Compose)
- All imports included, no code omitted
- Shallow nesting via ConstraintLayout
