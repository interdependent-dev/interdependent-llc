#!/usr/bin/env python3
"""
Build script for interdependent.llc.

Reads `content.md` (YAML frontmatter + markdown body sections) and
renders `_template/index.html.j2` into `index.html`.

Run locally:    python3 build.py
Run in CI:      see .github/workflows/build.yml

Body sections in content.md are delimited by `# section-id` headings.
Currently the template expects six body sections:
  - about-body       → about.body_paragraphs (list of paragraphs)
  - focus-body       → focus.body_paragraphs (list of paragraphs)
  - segments-body    → segments.body_paragraphs (list of paragraphs)
  - governance-body  → governance.body_paragraphs (list of paragraphs)
  - pictures-body    → pictures.body_paragraphs (list of paragraphs)
  - leadership-bio   → leadership.bio (string)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).parent
CONTENT = ROOT / "content.md"
TEMPLATE_DIR = ROOT / "_template"

# Pages to render: each is (template filename, output filename).
# All four pages share the YAML frontmatter from content.md and use the
# shared _header.html.j2 / _footer.html.j2 partials so the nav can't
# drift between pages.
PAGES = [
    ("index.html.j2",   "index.html"),
    ("privacy.html.j2", "privacy.html"),
    ("terms.html.j2",   "terms.html"),
    ("404.html.j2",     "404.html"),
]


def parse_content(text: str) -> tuple[dict, dict[str, str]]:
    """Split content.md into (frontmatter_dict, body_sections_dict)."""
    if not text.startswith("---"):
        raise SystemExit("content.md must start with a YAML frontmatter block (---).")

    # Find the end of the frontmatter block (second --- on its own line).
    parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        raise SystemExit("content.md frontmatter is not closed with a --- line.")

    _, frontmatter_text, body_text = parts
    frontmatter = yaml.safe_load(frontmatter_text) or {}

    # Split body into sections delimited by `# section-id` lines.
    sections: dict[str, str] = {}
    current_id: str | None = None
    current_lines: list[str] = []
    for line in body_text.splitlines():
        m = re.match(r"^#\s+([\w-]+)\s*$", line)
        if m:
            if current_id is not None:
                sections[current_id] = "\n".join(current_lines).strip()
            current_id = m.group(1)
            current_lines = []
        else:
            current_lines.append(line)
    if current_id is not None:
        sections[current_id] = "\n".join(current_lines).strip()

    return frontmatter, sections


def paragraphs(text: str) -> list[str]:
    """Split a block of prose into paragraphs (separated by blank lines)."""
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def main() -> int:
    text = CONTENT.read_text(encoding="utf-8")
    data, sections = parse_content(text)

    # Wire body sections into the data tree the template expects.
    data.setdefault("about", {})["body_paragraphs"] = paragraphs(
        sections.get("about-body", "")
    )
    data.setdefault("focus", {})["body_paragraphs"] = paragraphs(
        sections.get("focus-body", "")
    )
    data.setdefault("segments", {})["body_paragraphs"] = paragraphs(
        sections.get("segments-body", "")
    )
    data.setdefault("governance", {})["body_paragraphs"] = paragraphs(
        sections.get("governance-body", "")
    )
    data.setdefault("pictures", {})["body_paragraphs"] = paragraphs(
        sections.get("pictures-body", "")
    )
    data.setdefault("leadership", {})["bio"] = sections.get("leadership-bio", "").strip()

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=False,  # we control all output; HTML in fields is intentional
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )

    for template_name, output_name in PAGES:
        tpl = env.get_template(template_name)
        rendered = tpl.render(**data)
        output_path = ROOT / output_name
        output_path.write_text(rendered, encoding="utf-8")
        print(f"wrote {output_path.relative_to(ROOT)} ({len(rendered):,} bytes)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
