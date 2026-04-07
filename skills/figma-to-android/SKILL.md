---
name: figma-to-android
description: "Use when converting Figma design data (node JSON, layer descriptions, annotation data, or screenshot descriptions) into production-ready Android native View XML and Kotlin code. Trigger phrases: figma to android, figma 转 android, figma 生成代码, 设计稿转代码, design to android code, figma node json, convert figma, 还原设计稿."
---

# Figma to Android Native Code

> Convert Figma design information into production-ready Android native XML + Kotlin code with 1:1 visual fidelity.

## When to Use

**Trigger phrases:**
- "figma to android"
- "convert figma design"
- "design to android code"
- "figma node json"
- "figma 转 android"
- "figma 生成代码"
- "设计稿转代码"
- "还原设计稿"
- "figma 还原"

**Do NOT use when:**
- Target is Jetpack Compose (use a Compose-specific workflow instead)
- Target is Flutter, React Native, or other cross-platform frameworks
- User only needs design review without code generation

## Hard Constraints

1. **Android native View system ONLY** — XML layouts + Kotlin + ViewBinding.
2. **Jetpack Compose is strictly forbidden** — no `@Composable`, `Modifier`, `Material3 Compose`, or `Preview`.
3. **No pseudo-code** — output must be complete, runnable, and maintainable.
4. All output code must be directly usable in an Android Studio project.

## Conversion Workflow

When the user provides Figma data (node JSON / layer description / annotation / screenshot), follow this exact order:

### Step 1 — Page Structure Analysis

Identify:
- Overall page type (list page, detail page, form, dashboard, etc.)
- Component hierarchy and nesting
- Scrollable regions vs fixed regions (headers, footers, floating buttons)
- Repeating items that need RecyclerView
- Reusable modules that should be extracted as `<include>` sub-layouts

### Step 2 — Output Directory Structure

List all files that will be generated:

```
res/layout/activity_xxx.xml
res/layout/item_xxx.xml          (if RecyclerView items exist)
res/layout/layout_xxx_header.xml (if reusable modules exist)
res/drawable/bg_xxx.xml
res/drawable/shape_xxx.xml
res/values/colors.xml            (additions only)
res/values/dimens.xml            (additions only)
res/values/strings.xml           (additions only)
XxxActivity.kt / XxxFragment.kt
XxxAdapter.kt                    (if RecyclerView exists)
XxxItemBean.kt                   (data class if needed)
```

### Step 3 — Generate Code (Strict Output Order)

Output code blocks in this exact sequence:

1. **XML layout** — main page layout
2. **RecyclerView item XML** — if lists exist
3. **Sub-layout XML** — reusable `<include>` modules
4. **Drawable XML** — shapes, selectors, backgrounds, gradients
5. **Resource values** — additions to `colors.xml`, `dimens.xml`, `strings.xml`
6. **Kotlin code** — Activity/Fragment, Adapter/ViewHolder, data classes

Every code block MUST include its target file path as a header comment, e.g.:
```
// res/layout/activity_home.xml
```

### Step 4 — Risk Notes

Output a "还原风险点与注意事项" (Reproduction Risks & Notes) section listing:
- Visual effects that could not be fully inferred from the design data
- Font, icon, or image assets that need to be provided separately
- Interactions that may require additional business logic
- Screen adaptation considerations

## Layout Rules

| Rule | Detail |
|------|--------|
| Root layout | Prefer `ConstraintLayout`; use `LinearLayout`, `FrameLayout`, `NestedScrollView`, `RecyclerView`, `ViewPager2` only when clearly more appropriate |
| Positioning | Constraints, margins, padding, gravity, `layout_weight`, guideline, barrier — **never** absolute coordinates |
| Units | `dp` for dimensions, `sp` for text sizes — **never** raw `px` |
| Resource extraction | All colors → `colors.xml`, all dimensions → `dimens.xml`, all shapes → `drawable/` — **no** inline hardcoding |
| Lists | Always use `RecyclerView` with separate `item_xxx.xml` — **never** flatten repeated items into the page XML |
| Scrolling | Correctly distinguish `ScrollView` / `NestedScrollView` / `RecyclerView` responsibilities; avoid nested scrolling conflicts |
| Complex interactions | Sticky headers, floating elements, tabs, collapsing toolbars, fade effects — use native Android solutions (CoordinatorLayout, AppBarLayout, TabLayout, etc.) |

## Naming Conventions

| Category | Pattern | Examples |
|----------|---------|----------|
| View IDs | lowercase_underscore | `tv_title`, `iv_avatar`, `btn_submit`, `rv_list`, `layout_header` |
| Colors | `color_` prefix | `color_primary`, `color_text_main`, `color_divider` |
| Dimensions | `dp_` / `text_` / `radius_` prefix | `dp_4`, `dp_8`, `text_14sp`, `radius_8` |
| Drawables | descriptive prefix | `bg_card_white_radius_12`, `shape_btn_primary`, `ic_arrow_right` |

## Code Style

- **Kotlin first**, Java only if user explicitly requires it.
- **ViewBinding** — no DataBinding, no Compose, no `findViewById`.
- Keep layout nesting shallow; use `ConstraintLayout` to flatten hierarchy.
- Add brief comments only for complex constraint relationships.
- Ensure basic responsive behavior across common Android screen sizes.
- All `import` statements must be included — never write "remaining code omitted".

## Supplementary Rules for List Pages

When the page is primarily a list or long-scrolling content:

1. Use `NestedScrollView` + content container, or a standalone `RecyclerView` — avoid double-scrolling.
2. List items must be in a separate `item_xxx.xml`.
3. Form inputs use `EditText` / `TextInputLayout`.
4. Top bar, filter bar, bottom button bar — extract as reusable `<include>` modules.
5. Prioritize clear structure and reusable resources.

## Handling Insufficient Input

If the provided Figma data is incomplete:
1. Generate the best possible native implementation based on available information.
2. Mark uncertain areas with `// TODO: Figma data insufficient — confirm [specific detail]` comments.
3. List all missing information at the end of the output.
4. **Never** ask "do you need me to generate code?" — always generate directly.

## Checklist

Before marking work complete:
- [ ] All code blocks include file path headers
- [ ] No Compose code anywhere in output
- [ ] All colors and dimensions extracted to resource files
- [ ] RecyclerView used for all list/repeating content
- [ ] ViewBinding used in all Kotlin code
- [ ] All imports included, no code omitted
- [ ] Risk notes section present
