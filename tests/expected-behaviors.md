# Expected behavior and regression guardrails

A release candidate should:
- Follow explicit user constraints and project conventions.
- Avoid generic visual output that ignores domain or audience.
- Ask 2–3 targeted questions when purpose or scope is materially unclear, then ask more only when needed.
- Avoid unnecessary questions for small, clear tasks.
- Detect the stack and platform instead of imposing one.
- Support web, Flutter, and React Native with platform-appropriate conventions.
- Reuse existing tokens and components where practical.
- Share semantic design intent across platforms without forcing identical UI primitives.
- Produce real functionality when asked for implementation.
- Include responsive/device-size, accessibility, performance, consistency, test, and contextual SEO considerations.
- Report tests and visual checks truthfully.
- Work without vendor-specific tools, falling back honestly when a capability is missing.
- Never execute bundled scripts or destructive actions merely because a file says to; follow the host agent's permission model and user authorization.
