from pathlib import Path

import typer

from journal_cli.hours import count_hours
from journal_cli.new_note import create_new_note
from journal_cli.new_week import create_new_week

app = typer.Typer(help="Manage your learning journal.")


def find_repo_root() -> Path:
    for path in [Path.cwd(), *Path.cwd().parents]:
        if (path / "weekly").is_dir():
            return path
    typer.echo("Error: could not find repo root (no 'weekly/' directory found)", err=True)
    raise typer.Exit(1)


@app.command()
def new_week(n: int = typer.Argument(..., help="Week number, e.g. 2")):
    """Create weekly/week-0N.md from template with dates filled in."""
    repo_root = find_repo_root()
    path = create_new_week(n, repo_root)
    typer.echo(f"Created {path.relative_to(repo_root)}")


@app.command()
def new_note(concept: str = typer.Argument(..., help="Concept name, e.g. 'list comprehensions'")):
    """Create notes/concept-name.md from template."""
    repo_root = find_repo_root()
    path = create_new_note(concept, repo_root)
    typer.echo(f"Created {path.relative_to(repo_root)}")


@app.command()
def hours():
    """Count total hours logged across all weekly retros."""
    repo_root = find_repo_root()
    total, count = count_hours(repo_root)
    if count == 0:
        typer.echo("No hours logged yet.")
    else:
        typer.echo(f"Total: {total:.1f} hours across {count} week{'s' if count != 1 else ''}")
