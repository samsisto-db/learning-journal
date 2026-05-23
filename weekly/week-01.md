# Week 1 — Setup + Python foundations

> Adjust dates to your actual start. Suggested: the Monday after you finish reading this.

---

## Plan

### Theme
Get the floor under Python project hygiene + git fluency. Establish the daily commit cadence. Repo is healthy and you're shipping by Sunday.

### Hours target
10 hours (with 15 as stretch)

### Learning goals
- **Python project hygiene:** virtual environments with `uv`, project layout (`src/` vs flat), `pyproject.toml`, dependency management, packaging basics
- **Pytest fundamentals:** writing tests, fixtures, parametrize, running with `uv run pytest`
- **Type hints:** basic annotations, `Optional`, `list[str]` vs `List[str]`, when to use them
- **Git fundamentals:** init, add, commit, branch, checkout, merge, push, pull, the staging area, what `.gitignore` actually does
- **GitHub workflow:** creating PRs against yourself (yes, on your own repo — practice the workflow)

### Shipping deliverables
- [x] Repo folder structure cleaned up (no nested `mnt/...` path)
- [x] `notes/` and `projects/` exist and are committed (add `.gitkeep` or a real file)
- [x] **`journal-cli`** — a small Python CLI tool that helps manage this repo. Commands:
  - `journal new-week N` → creates `weekly/week-0N.md` from template, fills in dates
  - `journal new-note "concept name"` → creates `notes/concept-name.md` from template
  - `journal hours` → counts hours logged across weekly retros
  - Lives in `projects/journal-cli/` with its own `README.md`, `pyproject.toml`, tests, and works after `uv tool install .`
- [x] At least 5 daily commits across the week
- [ ] Read the Git intro chapters
- [ ] Open one PR against your own `main` branch and merge it (practice the workflow)

### Notes to draft
- `notes/python-project-structure.md` — pyproject.toml, src layout, uv workflow
- `notes/git-cheatsheet.md` — the 20 commands you actually use
- `notes/pytest-basics.md` — fixtures, parametrize, how to think about test scope

### Resources
**Python**
- [uv docs](https://docs.astral.sh/uv/) — the modern Python toolchain. Use this instead of pip/venv/poetry.
- [Real Python: pyproject.toml guide](https://realpython.com/python-pyproject-toml/)
- [Click docs](https://click.palletsprojects.com/) OR [Typer docs](https://typer.tiangolo.com/) — pick one for the CLI. Typer is friendlier; Click is more common in the wild.
- [pytest docs — Getting Started](https://docs.pytest.org/en/stable/getting-started.html)

**Git**
- [Pro Git book, chapters 1–3](https://git-scm.com/book/en/v2) — free, the canonical reference
- [Oh My Git!](https://ohmygit.org/) — game for learning branching/merging visually
- [GitHub Skills: Introduction to GitHub](https://github.com/skills/introduction-to-github) — interactive

**Stretch**
- [Hypermodern Python Cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python) — opinionated example of a well-structured Python project. Worth reading even if you don't use it.

### Rough daily shape
- **Mon (~1 hr):** Clean up repo folder structure. Install `uv` if not already. Skim `uv` docs. Commit the cleanup.
- **Tue (~1 hr):** Pro Git ch. 1–2. Initialize a new project under `projects/journal-cli/` with `uv init`. Set up `pyproject.toml`. Commit.
- **Wed (~1 hr):** Implement first command (`journal new-note`). Write one pytest for it. Commit.
- **Thu (~1 hr):** Pro Git ch. 3 (branching). Make a feature branch for the next command. Implement `journal new-week`. PR against main, merge it.
- **Fri (~1 hr):** Implement `journal hours`. Add tests. Add type hints throughout. Run `uv run pytest`.
- **Sat (~3 hrs):** Polish: write a real `README.md` for the project, add `journal --help`, install it as a `uv tool`, use it to create `notes/python-project-structure.md` as the first real note.
- **Sun (~2 hrs):** Draft remaining two notes. Write this week's retro below. Sketch Week 2 plan in `weekly/week-02.md`. Update `MOC.md` with new notes. Commit.

### Why `journal-cli` for the Week 1 project
- You'll actually use it. Dogfooding = motivation.
- Forces packaging fluency (the most common Python skill gap for analysts/SAs moving to engineering).
- Small enough scope to finish in a week.
- Shows up in your portfolio as "I built a tool to manage my own learning journey," which is a legitimate FDE-flavored signal — building small tools to solve your own problems is half the job.

