# Week 2 — DE core: Delta, Unity Catalog, Workflows, first DAB

## Learning goals
- Delta Lake: transaction log, ACID, time travel, MERGE, OPTIMIZE/VACUUM
- Unity Catalog: three-level namespace, managed vs external, grants
- Workflows: jobs, tasks, dependencies, triggers
- Medallion: bronze/silver/gold
- DABs end-to-end: databricks.yml, deploy, run

## Ship
- [ ] `projects/medallion-dab/` — DAB that does CSV → bronze → silver → gold Delta tables in UC, orchestrated as a Workflow job, deploys via `databricks bundle deploy --target dev`

## Notes to draft
- `notes/delta-lake.md`
- `notes/unity-catalog.md`
- `notes/medallion-architecture.md`
- `notes/dabs.md`

## Resources
- Delta Lake docs intro
- Unity Catalog overview docs
- Databricks Asset Bundles docs
- github.com/databricks/bundle-examples
- DE Associate prep path on Databricks Academy

## Daily shape
- Mon: Delta docs. Start `delta-lake.md`.
- Tue: UC docs. Create catalog/schema/volume. Upload CSV. Start `unity-catalog.md`.
- Wed: Read bundle-examples. Scaffold `medallion-dab/` with `databricks bundle init`. Deploy empty bundle.
- Thu: Bronze + silver layers.
- Fri: Gold layer + task dependencies. End-to-end run.
- Sat: Write remaining notes. Polish README. Push.
- Sun: Sketch week 3.

Notes 5/23/2026:
**Databricks dev workflow — summary**

- **Three places, one job each:** GitHub = source of truth, Cursor = where you edit, Databricks workspace = where code runs.
- **Edit primarily in Cursor** with Claude Code. Treat the Databricks UI as a read-mostly visitor.
- **Write code as plain `.py` modules** (functions, not notebooks). Avoid `.ipynb` for Git sanity.
- **Standard Git loop:** branch off `main` → edit → commit → push → PR → merge → delete branch. Same loop every time, including for bundle YAML changes.
- **Two ways code reaches the workspace:**
    - **VS Code Databricks extension** = one-off interactive runs against a cluster (no persistence)
    - **`databricks bundle deploy`** = creates real, named jobs in the workspace
- **DABs are YAML in your repo** (`databricks.yml` + `resources/*.yml`) that declaratively define jobs, schedules, clusters. The bundle is version-controlled like everything else.
- **Targets handle environments:** same bundle, different target = different workspace. `--target dev` from your laptop, `--target prod` from GitHub Actions on merge to main.
- **Workspaces don't need GitHub integration.** Git folders are optional and skippable. Deploys are pushed _to_ workspaces from wherever the CLI runs (laptop or CI).
- **Prod auth = service principal**, credentials stored in GitHub Actions (ideally via OIDC, not a long-lived PAT).
- **Guiding principle:** if it's not in the bundle YAML in the repo, it shouldn't exist in the workspace.