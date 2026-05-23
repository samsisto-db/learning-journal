# journal-cli

A small CLI tool for managing the learning journal repo.

## Install

```bash
uv tool install ./projects/journal-cli
```

Run from anywhere inside the repo.

## Commands

```bash
journal new-week 2          # creates weekly/week-02.md with dates filled in
journal new-note "concept"  # creates notes/concept.md with today's date
journal hours               # totals hours logged across all weekly retros
journal --help
```

## Development

```bash
cd projects/journal-cli
uv run pytest
```
