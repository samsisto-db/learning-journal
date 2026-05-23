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