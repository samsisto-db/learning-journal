# CLAUDE.md

Guidance for Claude Code working in this repository.

## What this repo is

A 6-month learning track for transitioning from Solutions Architect toward Forward Deployed Engineer work, with a spike in data engineering and AI/ML/GenAI on Databricks. It is both an **Obsidian vault** (notes, weekly retros, roadmap) and a **code monorepo** (small Python projects under `/projects/`).

The point of this repo is **learning**, not shipping production software. Optimize for my understanding, not for finished output.

## Repo layout

```
/
├── roadmap.md              # Living plan, updated weekly
├── MOC.md                  # Map of content (note index)
├── notes/                  # Concept notes (one topic per file)
├── weekly/                 # Weekly plans + retros (week-01.md, ...)
└── projects/               # Python projects, each with its own pyproject.toml
    └── journal-cli/        # Week 1 project
```

Notes are written in Obsidian-flavored markdown (wiki links `[[like-this]]` are fine). Treat the vault and the code as one repo—they evolve together.

## Working style (most important section)

The goal of this repo is for me to **learn and internalize concepts**, not to write every line by hand. You're doing the building; I'm learning by reading, asking, and reviewing.

**Lean toward a brief explanation before non-trivial work.** A short paragraph on the approach—what you're going to do and why—before you write the code. Not a full lesson, not a gate that waits for my approval. Just enough that I understand the shape of what's about to happen.

**Explain your choices inline.** If you reach for a library, pattern, or flag, say one sentence about why. "Using `typer` because it generates `--help` from type hints" is enough. I'd rather a 20-second explanation than a mystery import.

**Small, reviewable commits.** One logical change per commit. Good commit messages (imperative mood, explains *why* not just *what*). If a change touches more than one concern, split it.

**Don't silently refactor.** If you notice something broken or stylistically off elsewhere in the repo, mention it and let me decide. Don't fix things I didn't ask you to fix.

**Ask when ambiguous.** "Should this go in `notes/` or `projects/<name>/README.md`?" is a fine question. Guessing wrong wastes more time than asking.

## Python conventions

- **`uv` for everything**: environments, dependencies, running scripts, Python version management. No `pip install` directly, no `python -m venv`, no `poetry`.
- Each project under `/projects/` has its own `pyproject.toml` and its own `.venv`. We are *not* using a uv workspace yet—revisit if cross-project shared code emerges.
- Python version pinned per-project via `.python-version`.
- `pytest` for tests. Tests live in `tests/` alongside `src/` inside each project.
- `ruff` for linting and formatting (once introduced—probably Week 2 or 3).
- Type hints on all function signatures in project code. Notes/scratch can be looser.

## Git conventions

- Branch per feature, even on solo work (`week-01/journal-cli-init`, not commits straight to `main`).
- Open PRs against my own `main` and self-review the diff before merging. This is intentional muscle memory, not theater—don't suggest skipping it.
- `.gitignore` should cover `.venv/`, `__pycache__/`, `.DS_Store`, `*.pyc`, Obsidian's `.obsidian/workspace*` files.

## What's coming (so you have context)

Later weeks will introduce: Databricks Asset Bundles (DABs), Delta Lake / Unity Catalog, MLflow, Vector Search, and the Mosaic AI Agent Framework. When we get there, lean a bit heavier on the explanation—DAB YAML and Unity Catalog concepts especially are things I want to understand structurally, not just have working.

## Things to avoid

- Installing dependencies without naming them and explaining what they do.
- Generating boilerplate from memory when the canonical command (`uv init`, `uv add`, etc.) would produce it correctly and teach me the tool.
- Multi-file changes presented as one undifferentiated blob. Walk me through file-by-file.
- Editing notes in `notes/` or `weekly/` unless I explicitly ask—those are mine to write.

## When in doubt

Ask. The cost of one clarifying question is much lower than the cost of doing the wrong thing well.
