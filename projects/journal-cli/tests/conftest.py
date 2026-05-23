import pytest


@pytest.fixture
def repo(tmp_path):
    weekly = tmp_path / "weekly"
    notes = tmp_path / "notes"
    weekly.mkdir()
    notes.mkdir()

    (weekly / "_template.md").write_text(
        "# Week {N} — {YYYY-MM-DD to YYYY-MM-DD}\n\n"
        "> Write the **Plan** section before the week starts.\n\n"
        "---\n\n## Plan\n\n### Hours target\n~X hours\n\n"
        "---\n\n## Retro\n\n### Hours logged\n~X hours\n"
    )
    (notes / "_template.md").write_text(
        "# {Concept name}\n\n"
        "**Last reviewed:** YYYY-MM-DD\n\n"
        "## What it is\n_1–3 sentences._\n"
    )
    return tmp_path
