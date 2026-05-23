from journal_cli.hours import count_hours


def test_sums_hours_from_multiple_files(repo):
    (repo / "weekly" / "week-01.md").write_text("## Retro\n\n### Hours logged\n~10 hours\n")
    (repo / "weekly" / "week-02.md").write_text("## Retro\n\n### Hours logged\n~8 hours\n")
    total, count = count_hours(repo)
    assert total == 18.0
    assert count == 2


def test_skips_unfilled_placeholder(repo):
    (repo / "weekly" / "week-01.md").write_text("## Retro\n\n### Hours logged\n~X hours\n")
    total, count = count_hours(repo)
    assert total == 0.0
    assert count == 0


def test_returns_zero_when_no_weekly_files(repo):
    total, count = count_hours(repo)
    assert total == 0.0
    assert count == 0


def test_handles_decimal_hours(repo):
    (repo / "weekly" / "week-01.md").write_text("## Retro\n\n### Hours logged\n~1.5 hours\n")
    total, count = count_hours(repo)
    assert total == 1.5
    assert count == 1


def test_ignores_hours_target_in_plan_section(repo):
    (repo / "weekly" / "week-01.md").write_text(
        "## Plan\n\n### Hours target\n~15 hours\n\n## Retro\n\n### Hours logged\n~8 hours\n"
    )
    total, count = count_hours(repo)
    assert total == 8.0
    assert count == 1


def test_skips_file_with_no_retro_section(repo):
    (repo / "weekly" / "week-01.md").write_text("## Plan\n\n### Hours target\n~10 hours\n")
    total, count = count_hours(repo)
    assert total == 0.0
    assert count == 0
