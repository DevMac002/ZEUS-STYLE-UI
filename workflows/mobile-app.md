# Workflow: mobile app

1. Establish the user problem, audience, primary flows, target platforms, brand, and device constraints.
2. Ask concise questions only when an unknown could change the design or architecture.
3. Inspect the Flutter or React Native structure, navigation, state, theme, dependencies, and tests.
4. Follow [references/art-direction.md](../references/art-direction.md) to choose a theme-appropriate visual direction, then translate it into native layouts, controls, and tokens. Explore options internally and recommend one strong direction by default.
5. Define key screens, navigation, states, responsive-to-device-size behavior, and platform differences.
6. Implement functional screens using project conventions; keep safe areas, text scaling, keyboard, loading/error/empty states, and touch ergonomics in mind.
7. Check device or simulator behavior only when actually available; run relevant analyzers, lint, types, tests, or builds and report results honestly.
8. Summarize changed files, decisions, platform differences, checks, and remaining work.
