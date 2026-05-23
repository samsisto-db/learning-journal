from datetime import date

import pytest

from journal_cli.new_note import create_new_note, slugify


def test_slugify_spaces():
    assert slugify("list comprehensions") == "list-comprehensions"


def test_slugify_mixed_case():
    assert slugify("Python Project Structure") == "python-project-structure"


def test_slugify_special_chars():
    assert slugify("async/await") == "async-await"


def test_creates_file_at_correct_path(repo):
    path = create_new_note("list comprehensions", repo)
    assert path == repo / "notes" / "list-comprehensions.md"
    assert path.exists()


def test_fills_concept_name_in_heading(repo):
    create_new_note("list comprehensions", repo)
    content = (repo / "notes" / "list-comprehensions.md").read_text()
    assert "# list comprehensions" in content


def test_fills_today_date(repo):
    create_new_note("list comprehensions", repo)
    content = (repo / "notes" / "list-comprehensions.md").read_text()
    assert date.today().isoformat() in content


def test_placeholder_removed(repo):
    create_new_note("list comprehensions", repo)
    content = (repo / "notes" / "list-comprehensions.md").read_text()
    assert "YYYY-MM-DD" not in content
    assert "{Concept name}" not in content


def test_preserves_mixed_case_in_heading(repo):
    path = create_new_note("Python Project Structure", repo)
    content = path.read_text()
    assert "# Python Project Structure" in content


def test_slug_is_lowercase(repo):
    path = create_new_note("Python Project Structure", repo)
    assert path.name == "python-project-structure.md"


def test_errors_if_file_already_exists(repo):
    create_new_note("list comprehensions", repo)
    with pytest.raises(SystemExit):
        create_new_note("list comprehensions", repo)
