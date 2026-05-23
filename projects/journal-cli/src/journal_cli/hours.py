import re
from pathlib import Path


def count_hours(repo_root: Path) -> tuple[float, int]:
    total = 0.0
    counted = 0

    for week_file in sorted((repo_root / "weekly").glob("week-*.md")):
        content = week_file.read_text()
        retro_match = re.search(r"## Retro(.*)", content, re.DOTALL)
        if not retro_match:
            continue
        retro_section = retro_match.group(1)
        hours_match = re.search(r"~(\d+(?:\.\d+)?)\s+hours", retro_section)
        if hours_match:
            total += float(hours_match.group(1))
            counted += 1

    return total, counted
