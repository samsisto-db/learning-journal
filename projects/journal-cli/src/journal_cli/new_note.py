import re
from datetime import date
from pathlib import Path

import typer


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def create_new_note(concept: str, repo_root: Path) -> Path:
    slug = slugify(concept)
    output_path = repo_root / "notes" / f"{slug}.md"
    template_path = repo_root / "notes" / "_template.md"

    if output_path.exists():
        typer.echo(f"Error: {output_path.relative_to(repo_root)} already exists", err=True)
        raise SystemExit(1)

    template = template_path.read_text()
    content = template.replace("{Concept name}", concept).replace("YYYY-MM-DD", date.today().isoformat())
    output_path.write_text(content)
    return output_path
