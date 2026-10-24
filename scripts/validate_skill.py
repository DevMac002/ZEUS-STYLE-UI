#!/usr/bin/env python3
"""Lightweight, dependency-free structural validator for Web Design Engine."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FOLDER_IS_SKILL_SLUG = re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ROOT.name) is not None
REQUIRED = [
    "SKILL.md", "README.md", "LICENSE",
    "config/defaults.yaml", "config/personality.yaml", "config/design-preferences.yaml", "config/quality-gates.yaml", "config/platform-preferences.yaml",
    "references/discovery-and-briefing.md", "references/art-direction.md",
    "references/visual-research.md", "references/continuous-learning.md",
    "references/ux-and-information-architecture.md", "references/design-systems.md",
    "references/frontend-engineering.md", "references/accessibility.md",
    "references/responsive-design.md", "references/quality-assurance.md", "references/mobile-engineering.md", "references/cross-platform-design.md",
    "references/craft.md", "references/design-critique.md",
    "references/reference-profiles/ember-grid.md", "references/reference-profiles/esteve-visual-signature.md",
    "workflows/new-project.md", "workflows/existing-project.md",
    "workflows/redesign.md", "workflows/component-only.md", "workflows/mobile-app.md", "workflows/cross-platform-product.md",
    "templates/design-brief.md", "templates/design-direction.md", "templates/design-plan.md",
    "templates/quality-report.md", "templates/session-report.md",
    "scripts/contrast.py",
    "tests/test-cases.md", "tests/expected-behaviors.md",
]

errors = []
for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

skill_path = ROOT / "SKILL.md"
if skill_path.exists():
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter (---).")
    else:
        parts = text.split("---", 2)
        if len(parts) < 3:
            errors.append("SKILL.md frontmatter is not closed.")
        else:
            front = parts[1]
            name = re.search(r"(?m)^name:\s*([^\s#]+)\s*$", front)
            desc = re.search(r"(?m)^description:\s*(.+)$", front)
            if not name:
                errors.append("Frontmatter missing name.")
            elif name.group(1) != ROOT.name and FOLDER_IS_SKILL_SLUG:
                # Enforce the install-folder rule only when the folder itself is a valid skill slug.
                errors.append(f"Skill name '{name.group(1)}' must match folder '{ROOT.name}'.")
            elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)):
                errors.append("Skill name must be lowercase alphanumeric words separated by single hyphens.")
            if not desc:
                errors.append("Frontmatter missing description.")
            elif len(desc.group(1)) > 1024:
                errors.append("Description exceeds 1024 characters.")
            if len(text.splitlines()) > 500:
                errors.append("SKILL.md exceeds the recommended 500-line limit.")

    # Check local markdown references in SKILL.md.
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (ROOT / target).exists():
            errors.append(f"Broken local link in SKILL.md: {target}")

if errors:
    print("VALIDATION FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print(f"VALIDATION PASSED: {len(REQUIRED)} required files found.")
print("Note: this is a structural check, not official Agent Skills conformance or a design-quality test.")
