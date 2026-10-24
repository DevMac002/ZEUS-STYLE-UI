# Changelog

## 1.11.0
- Added Creative Frontier guidance for theme-specific immersive interactions, scroll choreography, and experiential motion.
- Routed new motion-led projects through the guide while keeping the creative process proportional to scope.
- Added behavior expectations for functional controls, mobile alternatives, accessibility, reduced motion, and performance.

## 1.10.0
- Integrated the supplied Art Direction Workflow into the art direction reference and linked it from the main skill.
- Aligned new project, redesign, and mobile workflows around exploring directions internally and recommending one strong fit by default.
- Expanded design planning to cover project signature, scroll/motion intent, design tokens, implementation, and honest review.
- Removed stale directions that treated Ember Grid or a menu of concepts as the default.

## 1.9.0
- Added a personal visual profile based on the user's supplied product and coastal activity screenshots.
- Made the personal profile the default starting point for new design directions; Ember Grid is now an optional darker technical direction.
- Added guidance for adapting shared visual principles to new themes without copying the source compositions.
- Added a behavior case for using personal screenshots across a different project theme.

## 1.8.0
- Reorganized SKILL.md as a concise entry point with task-based routing to focused workflows and references.
- Added config/personality.yaml as an editable home for Zeus's voice, visual signature, and working style, inferred from the existing skill.
- Made Ember Grid a contextual signature for suitable technical products rather than a required house style.
- Scaled discovery, concepts, research, validation, and learning to task scope; avoided mandatory research for focused changes.
- Updated the README and behavioral expectations to explain the new structure and customization points.

## 1.7.1
- Voice: removed the `Zeus a dit:` prefix rule entirely — Core instructions, `config/design-preferences.yaml` (persona/prefix set to `none`), and both test files updated. Speaking stays direct; history entries below record when the prefix was added and are kept as-is.

## 1.7.0
- Assets: added the real-assets rule — fetch actual assets from the internet when the project requires imagery, icons, video, audio, brand logos, or licensed fonts, instead of defaulting to placeholders.
- Added `references/assets.md`: sourcing order (project assets → user-supplied → free-license sources → generated on approval → declared placeholder), curated source table (Google Fonts, Unsplash, Pexels, Pixabay, Iconify, Simple Icons, unDraw, Coverr, Hero Patterns), per-asset license verification, attribution recording, local download/rename/optimization rules, CLS/alt/lazy integration checks, network-failure fallback, paid-stock scraping ban, and an acceptance checklist.
- Workflow: wired the rule into Core rules (rule 13), the Implement step, and progressive references.

## 1.6.0
- Design: added `references/reference-profiles/ember-grid.md`, the Ember Grid house direction derived from the supplied Pinterest/Gcore "Inference at the Edge" reference: warm near-black palette, single ember accent, tight grotesque type, thin glass surfaces, network/system hero, motion rules, copy tone, accessibility guardrails, and a do/don't checklist.
- Config: activated the reference profile and added a `house_direction` entry for technical, AI, infrastructure, developer, data, security, and B2B projects.
- Workflow: wired the profile into `SKILL.md` exploration and progressive references, `references/art-direction.md`, and `templates/design-plan.md`.
- Validation: expanded `scripts/validate_skill.py` to cover the new profile plus the 1.5.0 craft, critique, design-plan, and contrast files.
- Tests: added an Ember Grid acceptance case and regression guardrail.

## 1.5.0
- Design: added `references/craft.md` (subject-first method, domain starting points, typography, color, layout, shape, motion, copy), `references/design-critique.md` (plan review, tells of generated pages, result review, scorecard), `templates/design-plan.md`, and `scripts/contrast.py` (WCAG contrast checker).
- Workflow: wired the new files into Explore, Specify, and Validate steps in `SKILL.md`.

## 1.4.0
- Voice: personified the skill as Zeus — every question or assertion addressed to the user now starts with the exact prefix `Zeus a dit:`, repeated for each statement (code blocks, commands, file contents, and raw data tables excluded).

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
