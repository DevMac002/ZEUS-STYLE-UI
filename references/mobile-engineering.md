# Mobile engineering: Flutter and React Native

## Detect before implementation
Inspect the project to identify Flutter/Dart or React Native/JavaScript/TypeScript, the app entry point, navigation, styling/theme conventions, dependencies, platform-specific code, and available tests. Never replace the existing stack simply because another one is preferred.

## Flutter
- Follow the existing architecture and state-management approach.
- Use reusable, well-scoped widgets; avoid enormous widget trees when extraction improves readability.
- Centralize theme choices with the project's `ThemeData`, color scheme, text theme, and spacing conventions.
- Handle safe areas, keyboard insets, orientation/layout constraints, text scaling, and different screen sizes.
- Use appropriate Material or Cupertino patterns based on product context and the project's conventions.
- Keep accessibility semantics, labels, focus behavior, touch targets, and contrast in view.
- Run available `flutter analyze`, tests, and build checks only when the environment supports them; report actual results.

## React Native
- Follow existing navigation, state management, styling, and component conventions.
- Prefer TypeScript when the project already uses it; do not convert a JavaScript project without approval.
- Handle safe areas, keyboard avoidance, touch feedback, status/navigation bars, and platform-specific differences.
- Avoid assuming DOM, browser CSS, or web-only packages work in React Native.
- Review native dependencies and permissions before adding them.
- Run available lint, type checks, Jest/React Native tests, and builds when available; report actual results.

## Mobile UX states
Consider loading, empty, error, offline, permission-denied, disabled, success, and retry states where relevant. Forms must handle keyboard behavior, validation, focus, and submission feedback.

## Platform quality
Test or review narrow and large phones, tablets when relevant, orientation if supported, text scaling, safe areas, and iOS/Android differences. Do not claim native-device validation unless it actually occurred.
