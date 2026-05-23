from datetime import date, timedelta
from pathlib import Path

import typer


def current_week_monday(today: date) -> date:
    return today - timedelta(days=today.weekday())


def create_new_week(n: int, repo_root: Path) -> Path:
    template_path = repo_root / "weekly" / "_template.md"
    output_path = repo_root / "weekly" / f"week-{n:02d}.md"

    if output_path.exists():
        typer.echo(f"Error: {output_path.relative_to(repo_root)} already exists", err=True)
        raise SystemExit(1)

    template = template_path.read_text()

    monday = current_week_monday(date.today())
    sunday = monday + timedelta(days=6)
    date_range = f"{monday.isoformat()} to {sunday.isoformat()}"

    content = template.replace("{N}", str(n)).replace("{YYYY-MM-DD to YYYY-MM-DD}", date_range)
    output_path.write_text(content)
    return output_path
