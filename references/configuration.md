# Configuration and precedence

Configuration files are simple, editable defaults. Do not assume every agent can parse YAML programmatically. If it cannot, read the file as text and apply the intent.

## Precedence

1. Explicit instructions in the current user request.
2. Existing project architecture, conventions, and constraints.
3. User/project-specific configuration.
4. Web Design Engine defaults.
5. Low-risk professional judgment.

If two high-priority constraints conflict, explain the conflict and ask a focused question.

## Practical overrides

A user can request a one-off mode such as:
- "Skip concepts and implement the approved design."
- "Use only CSS, no new dependencies."
- "Give me three radically different art directions."
- "Do not edit files; only audit the design."
- "Run autonomously within this component."

Apply the override to the current task without permanently changing configuration unless explicitly requested.

## Keep customization portable

Prefer plain-language values and common concepts. Do not add vendor-specific API names, tool schemas, or hard-coded filesystem paths to the core configuration. Put client-specific installation notes in a separate adapter/documentation layer if needed.
