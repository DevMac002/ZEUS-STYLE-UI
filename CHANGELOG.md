# Changelog

## 1.3.0
- Accessibility: added the WCAG 2.2 AA success criteria (focus not obscured, dragging movements, 24×24 CSS px target size, consistent help, redundant entry, accessible authentication) and concrete touch-target numbers (WCAG, Material 48 dp, Apple 44 pt).
- Performance: added Core Web Vitals good thresholds (LCP ≤ 2500 ms, INP ≤ 200 ms, CLS ≤ 0.1) to frontend guidance and quality gates, with measure-before-claiming rule.
- Typography: added concrete starting points (line height 1.4–1.6, 60–75 character measure, fluid `clamp()` with a `rem` term, WOFF2 + `font-display`).
- Forms: added validation best practices (no premature errors, clear messages, error summary + inline, avoid disabled submit as only mechanism).
- Frontend: documented modern native CSS capabilities (`@container`, `:has()`, `@layer`, `:is()`/`:where()`, `clamp()`) as first choice over dependencies.
- Art direction: separated observed trends (serif display type, restrained palettes, asymmetric grids, kinetic type) from durable principles.
- Tests: added WCAG 2.2 audit and form-validation acceptance cases.

## 1.2.0
- Added `references/visual-research.md`: systematic visual reference research with curated sources, research rules, theme adaptation, and analysis/synthesis method.
- Added `references/continuous-learning.md`: three-level knowledge model (universal, platform/stack, project), integration rules, and the improvement cycle.
- Added `templates/session-report.md` end-of-cycle report template.
- Added a `Learn` step to the SKILL.md workflow feeding validated discoveries back into the skill.
- Expanded `references/design-systems.md` with a justified color system (semantic tokens, WCAG 2.2 contrast rules) and typography/layout system guidance.
- Added visual research and continuous learning defaults to `config/design-preferences.yaml`.
- Added acceptance cases for reference honesty and continuous learning.

## 1.1.0
- Expanded the skill from web-only to web and mobile: HTML/CSS/JavaScript, React, Next.js, Vue, Nuxt, Svelte, Flutter, and React Native.
- Added mobile engineering and cross-platform design system guidance.
- Added mobile-app and cross-platform workflows.
- Added configurable platform preferences.
- Clarified discovery: ask 2–3 targeted questions when purpose or scope is unclear, and more only when material ambiguity remains.
- Added Flutter, React Native, cross-platform, and discovery acceptance cases.

## 1.0.0
- Initial portable skill package with guided design workflow, configurable defaults, references, task workflows, and acceptance tests.
