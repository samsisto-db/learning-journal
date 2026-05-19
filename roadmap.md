# Roadmap

> Living document. Update weekly. Course-correct without guilt — log decisions in the Decision Log at the bottom.

---

## North Star

Level up from Solutions Architect → more FDE-like over ~6 months. Spike in **data engineering + AI/ML/GenAI**, rooted in Databricks but aware of the broader market. The output is not certifications or notes — it's **shipped artifacts** (DABs, accelerators, agents, reference implementations) and the ability to teach what I've built.

## Operating principles

- **Hours:** 10/week floor, 20/week ceiling. 1+ hr each weekday, ~5 hrs on weekends.
- **Cadence:** commit something every day I study. Weekly retro every Sunday.
- **Default to shipping:** if a week ends with no commit, that's the anti-signal.
- **Certs are checkpoints, not goals.** Pass the cert AND be able to build a representative project from scratch.
- **Flexibility is a feature.** Pivot when the data says so. Log the pivot.

## Phase map

| Phase | Weeks | Theme |
|---|---|---|
| 1. Foundation + breadth sampling | 1–6 | Floor under Python + Databricks fundamentals, sample each area, establish shipping cadence |
| 2. Depth + shipping | 7–16 | Commit to a primary spike, build a substantial accelerator, complete DE Associate recert |
| 3. Consolidation | 17–22 | Polish a stretch artifact, ship a public-facing piece, ML Associate recert |
| 4. Integration | 23–24 | Final retro, optional Pro cert stretch, plan next 6 months |

---

## Phase 1 — Foundation (Weeks 1–6)

Each week: theme → study → ship → notes.

### Week 1 — Setup + Python foundations
- **Study:** Python — typing, modules/packages, virtual environments (`uv` or `venv`), pytest basics. Git fundamentals (init, add, commit, branch, push, pull, merge).
- **Ship:** Repo skeleton pushed to GitHub. One trivial Python package with tests that pass.
- **Notes:** `python-project-structure.md`, `git-cheatsheet.md`.

### Week 2 — Python depth + finish GenAI Associate
- **Study:** Classes, decorators, async basics. Read other people's code (pick a small open-source library). Cert review.
- **Ship:** Pass GenAI Engineer Associate. One small CLI tool that calls an LLM API and does something useful (committed under `/projects/`).
- **Notes:** Cert-prep concept 1-pagers in `/notes/`.

### Week 3 — Data engineering core
- **Study:** Delta Lake, Unity Catalog, DLT, Workflows, medallion architecture. Start DE Associate prep.
- **Ship:** A small ETL pipeline as a **Databricks Asset Bundle** — raw CSV → bronze/silver/gold Delta tables, scheduled via Workflow. The DAB itself is the point; learn the bundle structure end-to-end.
- **Notes:** `delta-lake.md`, `unity-catalog.md`, `dabs.md`, `medallion-architecture.md`.

### Week 4 — MLOps fundamentals
- **Study:** MLflow 3 (tracking, registry, model serving), feature store basics.
- **Ship:** Extend Week 3's DAB — train a simple model on the gold table, register it in Unity Catalog, deploy a serving endpoint. Doesn't need to be a good model; needs to be a working loop.
- **Notes:** `mlflow.md`, `model-serving.md`.

### Week 5 — GenAI on Databricks
- **Study:** Vector Search, RAG patterns, Mosaic AI Agent Framework.
- **Ship:** A RAG app or simple agent built as a DAB.
- **Notes:** `vector-search.md`, `rag-vs-agents.md`, `agent-framework.md`.

### Week 6 — SWE foundations + retro
- **Study:** GitHub Actions for CI, pytest for the projects, DAB testing patterns.
- **Ship:** CI workflow that lints + tests the projects on every push.
- **Retro:** Hard self-assessment. Re-rate Python/DE/ML/GenAI/SWE. Look at what shipped. **Decide Phase 2 primary spike.**

---

## Phase 2 — Depth + shipping (Weeks 7–16, sketched)

- Commit to **one primary spike** (DE or GenAI) based on Week 6 retro; the other stays secondary.
- Pass **DE Associate** recert in this window.
- Build **one substantial accelerator** — something forkable, README'd, with tests. E.g. "RAG-over-internal-docs starter kit" or "incremental ingestion + DQ framework as a DAB."
- Start **ML Associate** prep toward the end of this phase.

Detailed weekly breakdown TBD at Week 6 retro.

## Phase 3 — Consolidation (Weeks 17–22, sketched)

- Pass **ML Associate** recert.
- Polish a **stretch artifact** — more ambitious accelerator.
- Ship a **public-facing piece**: blog post, internal Databricks tech share, OSS contribution, or a talk. Non-negotiable — teaching is the retention test.

## Phase 4 — Integration (Weeks 23–24, sketched)

- Final retro across all phases.
- Optional: attempt a **Pro-level cert** (DE Pro or ML Pro) as a stretch.
- Plan the next 6 months. Decide FDE flavor with real data.

---

## Progress measurement

**Weekly**
- Commits to the repo (count + substance)
- One-paragraph retro in `/weekly/`
- Self-rating 1–5 on: Python, DE, ML/MLOps, GenAI, SWE foundations

**Monthly**
- Certs cleared
- Projects shipped under `/projects/`
- Notes that pass the "teach it cold" test — pick a random note, explain it out loud without looking. If you can't, status goes back to `#status/working`.

**Months 3 and 6**
- External signal: written piece, talk, internal tech share, or OSS PR.

**Anti-signals (course-correct trigger)**
- Cert passed but no project shipped from that area
- Notes pile up but `/projects/` is quiet
- Repo silent for 2+ weeks
- Self-ratings flat for 4+ weeks

---

## Open items / parking lot

- System prompts
- KV cache
- Transformer architecture
- Lakebase branching
- Lakebase to save the state of an agent vs. using an .md file

### Databricks deep dive
- DAB patterns: multi-env (dev/staging/prod), variables, includes, complex bundles shipping to customers
- DLT vs Workflows — decision criteria, when to use each
- Spark execution model + performance tuning (AQE, broadcast joins, partition sizing, skew)
- Structured Streaming + CDC patterns (Auto Loader, DLT streaming tables)
- Unity Catalog deep dive — governance, lineage, ABAC, fine-grained access, attribute-based access
- Lakehouse Federation
- Genie / AI/BI — what's actually shippable to customers today
- Photon internals — when it helps, when it doesn't
- Liquid clustering, predictive optimization, deletion vectors
- Serverless compute trade-offs

### GenAI / agents
- Mosaic AI Agent Framework — patterns, evals, tracing
- Model Context Protocol (MCP) — what it is, where it fits, build a server
- DSPy — prompt programming, when it beats hand-tuned prompts
- LangChain / LangGraph awareness — pros/cons vs native Databricks
- Advanced RAG — hybrid search, reranking, chunking strategies, query rewriting
- Evals — LLM-as-judge, agent evals, regression test suites, MLflow eval
- Fine-tuning on Databricks — when it's worth it vs. just better prompts/RAG
- Multi-agent patterns — orchestration, handoff, shared memory
- Function calling / tool use patterns across providers
- Anthropic Claude API specifics (extended thinking, prompt caching, MCP)
- OpenAI API specifics (Responses API, structured outputs)

### MLOps
- Feature store patterns — offline vs online, point-in-time correctness
- Model serving patterns — batch vs real-time vs streaming inference
- Drift detection, monitoring, retraining triggers
- MLflow 3 new features (deep dive)

### Adjacent tech / market awareness
- Terraform basics — for Databricks workspace IaC
- dbt — what it does, when customers use it alongside Databricks
- Snowflake awareness — know the competition's positioning
- Kafka / Kinesis — streaming sources
- Iceberg vs Delta — the open table format conversation
- Lakehouse vs warehouse vs lakehouse-federated — vocabulary fluency

### Python / SWE foundations
- `uv` for env + dependency management
- pytest patterns — fixtures, parametrization, marks
- Type checking with mypy or pyright
- GitHub Actions — beyond basic CI
- Pre-commit hooks (ruff, black, mypy)
- Async Python — when it matters
- Python packaging — building installable libraries
- Logging done well (structured logs)

### FDE-adjacent skills
- Customer discovery / requirements gathering for technical solutions
- Writing technical design docs
- Reading customer code under time pressure
- Demo skills — building credible demos fast
- Solution accelerator authoring patterns (how Databricks publishes its own)

### To explore / read
- (drop links and half-thoughts here, promote to a note when worth it)

---

## Decision log

When you change course, write one line here with the date and why. This is how flexibility actually works without becoming drift.

- `YYYY-MM-DD` — example: switched Week 5 from agents to advanced RAG because customer engagement X came up.
