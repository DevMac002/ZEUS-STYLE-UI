# Acceptance test suite

Use these scenarios to evaluate behavior across compatible agents. These are behavioral tests, not a guarantee that every tool is available.

## Case 1 — Unfamiliar landing page
Prompt: "Design a landing page for a climate-risk analytics product for municipal planners."
Expected: asks only material questions or states assumptions; offers distinct directions when useful; avoids invented metrics and endorsements.

## Case 2 — Data-heavy dashboard
Prompt: "Create a dashboard for monitoring warehouse inventory in this existing repo."
Expected: inspects stack and components; prioritizes data scanning, filtering, empty/error/loading states; avoids gratuitous decoration.

## Case 3 — Existing component change
Prompt: "Improve the spacing and mobile behavior of this navigation component."
Expected: focused change; no unnecessary redesign; responsive and keyboard checks where possible.

## Case 4 — Reference screenshot
Prompt: "Use this screenshot as inspiration for a new editorial website."
Expected: extracts principles, separates observation from inference, respects asset rights.

## Case 5 — Existing design system
Prompt: "Add a settings page to this app."
Expected: reuses existing tokens and components; does not create a competing design system.

## Case 6 — No browser access
Expected: does not claim screenshot inspection; uses fallback checks and reports visual validation as not run.

## Case 7 — Dependency pressure
Prompt: "Add a new animation library for a subtle hover effect."
Expected: considers built-in options and dependency cost; asks before substantial additions.

## Case 8 — Flutter mobile app
Prompt: "Add an account settings screen to this Flutter app."
Expected: inspects Dart/widgets/theme/navigation; handles safe areas, text scaling, keyboard and states; uses idiomatic Flutter; reports actual `flutter analyze` and tests only if run.

## Case 9 — React Native screen
Prompt: "Create an onboarding flow in this React Native project."
Expected: inspects navigation and styling; accounts for iOS/Android differences, keyboard, safe areas, touch targets, and native dependencies.

## Case 10 — Shared web and mobile product
Prompt: "Build a consistent account experience for Next.js and Flutter."
Expected: shares product intent and semantic tokens while allowing platform-native UI patterns; tests/report each target independently.

## Case 11 — Ambiguous brief
Prompt: "Make me an app for my business."
Expected: asks 2–3 concise questions about business, users, purpose, and key workflow, then asks more only if ambiguity remains material.

## Case 12 — Clear brief
Prompt: "In this existing React component, change the button spacing from 12px to 16px and run the relevant tests."
Expected: does not ask broad discovery questions; makes the focused change and reports actual tests.

## Case 13 — Quality report
Expected: runs available checks, reports evidence and unrun checks, and does not equate a successful build with full production readiness.

## Case 14 — Visual research for a new project
Prompt: "Design a landing page for an artisan coffee subscription service."
Expected: consults several accessible reference sources fitting the theme, compares multiple approaches, provides direct links with brief notes, never claims to have inspected an inaccessible page, and never invents URLs.

## Case 15 — Inaccessible reference
Prompt: "Use this Pinterest board as inspiration" (link fails to load).
Expected: says the source could not be opened, tries another accessible source or asks the user for a screenshot, and does not fabricate visual details.

## Case 16 — Continuous learning integration
Prompt after a completed design cycle: "Integrate what you learned into the skill."
Expected: proposes changes justified by sources or observed problems, deduplicates existing rules, keeps project preferences out of global defaults, updates `CHANGELOG.md`, and runs the structural validator.

## Case 17 — Contrast claim
Prompt: "Confirm this palette passes WCAG AA."
Expected: calculates or verifies ratios before claiming compliance, reports normal-text and large-text thresholds separately, and states what could not be verified.

## Case 18 — WCAG 2.2 review
Prompt: "Audit this page against WCAG 2.2 AA."
Expected: checks the 2.2 additions (focus not obscured, dragging alternatives, 24×24 CSS px targets, consistent help, redundant entry, accessible authentication) in addition to 2.1 criteria; does not claim conformance without evidence.

## Case 19 — Form validation UX
Prompt: "Add validation to this signup form."
Expected: avoids premature inline errors, removes messages when corrected, provides an error summary plus per-field messages on submit, states what to fix in plain language, and does not rely on a disabled submit button as the only mechanism.

## Scoring
Score each dimension 0–2:
- Context adaptation
- Visual distinctiveness
- UX clarity
- Code/project fit
- Guided decision behavior
- Responsive/accessibility awareness
- Platform awareness
- Verification honesty
- Reference research quality
- Learning integration discipline

0 = absent or harmful; 1 = partial; 2 = clear and appropriate. Compare across agents and iterate on repeated failures.
