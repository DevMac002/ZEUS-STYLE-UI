# Zeus — Web and product design

Zeus is a portable skill for designing and building context-aware web and mobile interfaces. It combines a concise workflow with focused references, practical templates, and optional validation helpers.

## Start here

1. Read SKILL.md — the short entry point and routing guide.
2. Edit config/personality.yaml — name, voice, visual signature, and working style.
3. Adjust config/defaults.yaml for workflow preferences.
4. Adjust config/design-preferences.yaml for visual exploration.
5. Adjust config/platform-preferences.yaml and config/quality-gates.yaml only if you need different platform or review defaults.

The personality profile is based on your screenshots: light, spacious, product-led layouts with layered panels and theme-dependent color. Ember Grid remains an optional darker technical direction.

## Folder map

- SKILL.md: purpose, core behavior, and links to relevant material.
- config/: personal identity and task defaults.
- workflows/: optional paths for new projects, existing products, redesigns, components, mobile, and cross-platform work.
- references/: detailed guidance loaded only when relevant, including the full art direction workflow.
- references/reference-profiles/: reusable visual directions; Esteve visual signature is the personal default, with Ember Grid as an optional alternative.
- templates/: optional briefs, plans, and reports.
- scripts/: contrast calculator and structural validator.
- tests/: manual behavior scenarios and regression expectations.
- CHANGELOG.md: notable changes over time.

## Working principles

- Follow the user's current request and the project's conventions.
- Scale process and research to the size and uncertainty of the task.
- Preserve what already works; make the smallest complete change for focused requests.
- Use the personal visual profile as a starting point; adapt it to each project theme and brand.
- Be clear about assumptions and evidence. Do not claim checks that were not run.

## Validate the package

Run the structural validator from this folder:

~~~sh
python scripts/validate_skill.py
~~~

It checks required files, frontmatter, and local links. It does not judge design decisions or guarantee compatibility with every agent.

## Installation

Place this folder in a skills directory supported by your agent. Discovery and installation paths vary between tools; check the target agent's current documentation.
