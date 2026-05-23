from datetime import date, timedelta

import pytest

from journal_cli.new_week import create_new_week, current_week_monday


def test_creates_file_at_correct_path(repo):
    path = create_new_week(2, repo)
    assert path == repo / "weekly" / "week-02.md"
    assert path.exists()


def test_zero_pads_single_digit_week(repo):
    path = create_new_week(3, repo)
    assert path.name == "week-03.md"


def test_fills_week_number_in_heading(repo):
    create_new_week(2, repo)
    content = (repo / "weekly" / "week-02.md").read_text()
    assert "# Week 2 —" in content


def test_fills_date_range(repo):
    create_new_week(2, repo)
    content = (repo / "weekly" / "week-02.md").read_text()
    monday = current_week_monday(date.today())
    sunday = monday + timedelta(days=6)
    assert monday.isoformat() in content
    assert sunday.isoformat() in content


def test_placeholder_removed(repo):
    create_new_week(2, repo)
    content = (repo / "weekly" / "week-02.md").read_text()
    assert "{YYYY-MM-DD to YYYY-MM-DD}" not in content
    assert "{N}" not in content


def test_preserves_template_body(repo):
    create_new_week(2, repo)
    content = (repo / "weekly" / "week-02.md").read_text()
    assert "## Plan" in content
    assert "## Retro" in content


def test_errors_if_file_already_exists(repo):
    create_new_week(2, repo)
    with pytest.raises(SystemExit):
        create_new_week(2, repo)


def test_current_week_monday_is_monday():
    monday = current_week_monday(date.today())
    assert monday.weekday() == 0


def test_current_week_monday_when_today_is_monday():
    a_monday = date(2025, 1, 6)
    assert current_week_monday(a_monday) == a_monday
