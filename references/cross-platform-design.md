# Cross-platform design systems

## Shared principles, platform-specific execution
Keep the product identity, semantic design tokens, content hierarchy, interaction intent, and accessibility requirements consistent. Do not force identical controls or navigation on platforms with different conventions.

## Token model
Where appropriate, define shared semantic tokens for:
- Brand and semantic colors.
- Typography roles and scale.
- Spacing, layout, and density.
- Shape, elevation, borders, and shadows.
- Motion and reduced-motion behavior.
- Focus, selected, disabled, error, and success states.

Map tokens into each implementation idiom:
- CSS custom properties or the project's existing theme system on web.
- `ThemeData`/theme extensions or established theming in Flutter.
- Existing theme/styling solution in React Native.

Do not create separate competing token sets without a clear reason. Document platform-specific exceptions.

## Platform conventions
- Web: responsive navigation, pointer and keyboard interaction, browser semantics, URLs, focus management.
- iOS: safe areas, native-feeling navigation and controls where appropriate, dynamic type, system appearance.
- Android: system bars, back navigation, touch feedback, font scaling, Material conventions where appropriate.
- Tablets/foldables: adapt information density and layout instead of simply scaling a phone screen.

## Shared components
Share a component only when behavior, accessibility semantics, and maintenance benefit justify it. A shared design language does not require a shared implementation component across web and native platforms.
