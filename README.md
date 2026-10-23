# Web Design Engine

A vendor-neutral Agent Skill for context-sensitive web and mobile design, UX, frontend implementation, design systems, and quality assurance.

## What it does

- Understands the project and audience before designing.
- Uses a hybrid design strategy: context + brand + references + creative exploration.
- Adapts the number of art directions to project ambiguity and scope.
- Detects the existing stack instead of imposing one.
- Supports HTML/CSS/JavaScript, React, Next.js, Vue, Nuxt, Svelte, Flutter, and React Native.
- Asks 2–3 targeted discovery questions when purpose or scope is materially unclear.
- Works in guided mode with approval gates for consequential decisions.
- Supports analysis, concepts, design-system work, implementation, and test reporting.
- Encourages responsive behavior, accessibility, performance, visual consistency, tests, and relevant SEO.
- Reports what was actually verified versus what could not be tested.

## Package structure

- `SKILL.md`: core instructions and workflow.
- `config/`: editable default behavior, platform preferences, visual preferences, and quality gates.
- `references/`: focused domain guidance loaded as needed.
- `workflows/`: task-specific procedures.
- `templates/`: optional project artifacts.
- `scripts/`: optional validation helpers.
- `tests/`: manual acceptance scenarios.

## Install

This folder follows the open Agent Skills folder convention. Install it in a directory recognized by your compatible agent. A common project-level location is:

```text
.agents/skills/web-design-engine/
```

Some tools use a different skill directory or require a client-specific adapter. Consult the target tool's current documentation; the contents of the skill are vendor-neutral, but discovery paths and tool access are not universal.

For a shared repository:
1. Commit this folder to Git.
2. Add it to the project or publish the repository.
3. Copy/link the skill folder into the agent's supported skills directory.
4. Restart or refresh the agent if required.
5. Ask the agent to use `web-design-engine` on a small task and verify that it reads `SKILL.md`.

If your agent supports the community `skills` CLI, follow that CLI's current documentation for installing a skill from a repository. Do not assume every agent supports the same command.

## Customize

Edit:
- `config/defaults.yaml` for workflow and general behavior.
- `config/design-preferences.yaml` for visual preferences and concept selection.
- `config/quality-gates.yaml` for validation requirements.

Project-level requirements and the current user request take precedence over defaults. See `references/configuration.md`.

## Validate the package

Run:

```bash
python scripts/validate_skill.py
```

This script checks the expected files, basic frontmatter requirements, and references to local resources. It does not prove compatibility with every agent or validate design quality.

## Security

Review the skill and any scripts before using them in sensitive repositories. Scripts are optional and should be run only in a trusted environment. The core skill does not need network access and does not collect or transmit project data.

## Version

1.0.0
