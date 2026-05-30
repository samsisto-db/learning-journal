# AI / ML / GenAI learning framework

A mental model for organizing what you learn across the AI landscape, so you build a foundation with depth instead of a linear list of topics.

## How to use this

Two axes:

- **Paradigm** (rows) — which family of approaches you're reaching for
- **Lifecycle stage** (columns) — where in the workflow you're operating

Any new concept gets placed somewhere on the grid before you commit time to it. Cells you can't fill are your thin spots. The act of placing a concept into a cell *is* the learning step — if you can't place it, you don't yet understand it.

The goal isn't to master every cell. The goal is to know enough in each one to articulate **when not to use what's in it**. That's the FDE bar — knowing what to reach for, not just how each thing works.

---

## Paradigms (rows)

### Classical / statistical ML

Models grounded in statistics and discrete algorithms — linear/logistic regression, decision trees, gradient-boosted ensembles (XGBoost, LightGBM, CatBoost), clustering, dimensionality reduction. Still the right answer for most tabular, structured problems. Interpretable, cheap to train, well-understood failure modes. Don't skip this row because it feels "old" — it's the majority of what actually gets deployed at scale, and it's what most customer problems still look like.

### Deep learning

Neural networks with many layers, trained via backpropagation. Convolutional nets for images, recurrent and transformer architectures for sequences, embeddings for almost everything else. You probably won't train one from scratch often, but you need to understand what's happening — because deep learning is the substrate under foundation models, and the vocabulary of fine-tuning, embeddings, gradients, and loss functions all comes from here. Knowing this row is how you debug the row above it.

### Foundation models / GenAI

Pretrained models (LLMs, vision-language models, embedding models) that you adapt rather than train. The fundamental shift is leveraging someone else's billion-dollar training run via prompting, retrieval (RAG), fine-tuning, or agentic orchestration. Completely different cost, latency, and evaluation profile than classical ML — and consequently a different ops discipline (LLMOps). This is where most new shipping work happens today.

### A note on what's NOT a row

- **Reinforcement learning** is the most defensible fourth row. Add it if your work pulls you toward agents that learn from feedback (RLHF, bandits for ranking, MAB for experimentation). For most FDE work that ships, it's adjacent — keep it as an optional row to add later if needed.
- **Multimodal, agents, time series, recommender systems** are *problem types* that cut across paradigms. A recommender can be classical (matrix factorization), DL (two-tower), or GenAI (semantic search + LLM reranker). Treat them as topics, not rows — otherwise the grid stops doing its job.
- **Causal inference / experimentation** is its own discipline (A/B testing, uplift modeling, causal forests). Critical for "did the thing actually work" but lives mostly in classical-row methods.

---

## Lifecycle stages (columns)

### Data

Everything before a model exists: ingestion, cleaning, governance, feature engineering, tokenization, chunking, embedding, vector indexing. The unglamorous 60–70% of any ML project. The shape of your data layer determines what models you can train and what production systems you can actually ship. Most "the model isn't working" problems are really data problems.

### Modeling

The actual fitting, training, or adapting. For classical ML, this is `model.fit()` plus hyperparameter tuning. For deep learning, training loops, learning rate schedules, and architectural choices. For GenAI, this is prompting, retrieval architecture, fine-tuning, and agent design. Often less time than data prep, but where the conceptual richness of each paradigm lives.

### Eval

How you know the thing works. Cross-validation and AUC for classical, held-out test sets and benchmark suites for DL, eval harnesses + LLM-as-judge + golden datasets for GenAI. The hardest and most underrated step at every level. Most production failures trace back to bad eval, not bad models — you shipped something that scored well on a metric that didn't reflect reality.

### Serving

Getting the model to do work in production. Batch scoring for offline use, REST endpoints for synchronous calls, streaming for LLMs, GPU inference for large models. The concerns shift by row: classical is usually about throughput and integration, DL adds GPU economics, GenAI adds token costs, latency budgets (TTFT vs. throughput), and context window management.

### Ops

The lifecycle of a deployed system: monitoring, versioning, drift detection, retraining triggers, observability. MLOps for classical/DL, LLMOps for GenAI — they share concepts but differ in what you monitor (input drift vs. prompt drift, accuracy decay vs. eval regression, model performance vs. cost regression).

---

## Cross-cutting concerns

These apply to every cell of the matrix and are usually where production systems actually break:

- **Evaluation methodology** — how you measure correctness, including the gap between offline metrics and online behavior
- **Cost & latency** — what an inference costs and how fast it returns; varies by 1000× across rows
- **Safety / governance** — access control, PII handling, output safety, audit
- **Build vs. buy vs. wrap an API** — the most important strategic question; affects every cell and is the FDE judgment call

---

## The matrix (compressed view)

|                        | Data                                 | Modeling                                                                    | Eval                       | Serving                                                                         | Ops                        |
| ---------------------- | ------------------------------------ | --------------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------- | -------------------------- |
| **Classical ML**       | Feature stores, tabular pipelines    | XGBoost, scikit-learn                                                       | CV, AUC, F1, confusion mtx | Batch scoring, REST endpoints                                                   | MLflow, drift detection    |
| **Deep learning**      | Embeddings, augmentation             | PyTorch, fine-tuning, transformer architecture, attention mechanism (Q/K/V) | Held-out tests, ablations  | GPU inference, quantization                                                     | Versioning, GPU monitoring |
| **Foundation / GenAI** | Vector search, chunking, RAG corpora | Prompting, RAG, agents, DSPy, system prompts, context engineering           | LLM-as-judge, eval suites  | LLM endpoints, streaming, token costs, context window, KV cache, prompt caching | Prompt mgmt, tracing       |

---

## Topic backlog (starter)

A seed list per cell. Add to these as you encounter new concepts. Don't try to make this exhaustive — the field moves too fast and the curation effort isn't the learning. The goal is to keep a running list of *what you don't yet know* so it's hard to forget.

### Classical ML × Data
- Feature engineering (scaling, encoding, interactions)
- Feature stores (Databricks Feature Engineering in UC, Feast)
- Train / test / validation splits, stratified sampling
- Time-based splits for temporal data
- Data leakage
- SMOTE, class imbalance handling
- Outlier detection, robust scaling

### Classical ML × Modeling
- Linear & logistic regression
- Decision trees, random forests
- Gradient boosting (XGBoost, LightGBM, CatBoost)
- Clustering (k-means, DBSCAN, hierarchical)
- Dimensionality reduction (PCA, t-SNE, UMAP)
- Hyperparameter search (grid, random, Bayesian; Optuna, Hyperopt)
- Ensembling and stacking

### Classical ML × Eval
- Cross-validation strategies (k-fold, stratified, time-series)
- AUC, precision / recall, F1
- Confusion matrices, classification reports
- Regression metrics (MAE, MSE, RMSE, R²)
- Calibration (Brier score, reliability diagrams)
- Lift curves, cumulative gain
- Group fairness metrics

### Classical ML × Serving
- Batch scoring patterns (Databricks Workflows, DLT)
- Real-time endpoints (Mosaic AI Model Serving)
- Edge deployment
- Model formats (ONNX, PMML, pickle, MLflow model flavor)
- A/B serving and shadow deployments

### Classical ML × Ops
- MLflow tracking, registry, model versioning in Unity Catalog
- Feature drift, target drift, concept drift
- Lakehouse Monitoring
- Retraining triggers and cadence
- Champion / challenger patterns
- Model lineage and reproducibility

### Deep learning × Data
- Embeddings (word, sentence, image, multimodal)
- Tokenization (BPE, WordPiece, SentencePiece)
- Data augmentation
- Tensor pipelines, batching, padding, collation
- Synthetic data generation
- Active learning

### Deep learning × Modeling
- PyTorch, TensorFlow / Keras
- Convolutional networks (ResNet, EfficientNet)
- Transformers, attention mechanism
- Transfer learning, full fine-tuning
- Parameter-efficient fine-tuning: LoRA, QLoRA, PEFT
- Loss functions, optimizers (Adam, AdamW, SGD)
- Learning rate schedules, warmup
- Distributed training (DDP, FSDP, DeepSpeed)

### Deep learning × Eval
- Held-out test sets
- Benchmarks (ImageNet, GLUE, SuperGLUE, MMLU)
- Ablation studies
- Loss curves, train / val divergence
- Per-class diagnostics
- Robustness testing

### Deep learning × Serving
- GPU inference, dynamic batching
- Quantization (INT8, INT4, GGUF)
- Model distillation
- ONNX Runtime, TensorRT, vLLM
- Mosaic AI Model Serving (GPU endpoints)

### Deep learning × Ops
- Experiment tracking (MLflow, W&B)
- GPU utilization monitoring
- Distributed training observability
- Model versioning at scale
- Checkpoint management

### Foundation models × Data
- Vector search (Databricks Vector Search, pgvector, FAISS)
- Embedding models (OpenAI, Cohere, BGE, E5, voyage)
- Chunking strategies (fixed, recursive, semantic, hierarchical)
- Document parsing (PDF, HTML, tables, images)
- Unity Catalog for unstructured data, volumes
- RAG corpus curation and refresh
- Reranking (BGE reranker, Cohere rerank)

### Foundation models × Modeling
- Prompt engineering (zero-shot, few-shot, chain-of-thought)
- RAG patterns (naive, advanced, agentic, GraphRAG)
- Agent frameworks (Mosaic AI Agent Framework, LangGraph)
- Tool use / function calling / structured outputs
- DSPy (program-of-prompts, compilation)
- Fine-tuning (SFT, instruction tuning, RLHF basics)
- Multi-agent orchestration
- Routing across models (cost / capability tiers)
- Context management, prompt caching
- Agents - In the case of generative AI, agents are a class of intelligent agents that can pursue goals, use tools and take actions with varying degrees of autonomy. 
	- Anthropic - software that can interact with its environment and perform actions to complete a defined goal.
	- Agentic loop: gather context -> take action -> verify results
	- Context window: the amount of space an agent can hold in its memory. Once context window fills up, then it is compacted down to free up space
	- [CLAUDE.md](http://claude.md) file - gives Claude Code persistent memory about your project
	- MCP servers add tool definitions to your context window, even when you’re not using them. If you have lots enabled, that can eat into your available context
	- Hooks give you a deterministic control over CC’s behavior -> if you need something to happen every time without fail
- System prompt - the instruction block that a lab or a developer injects ahead of user's messages to set the models persona, capabilities, tools, formatting rules and safety boundaries. Is now the top of the *instruction hierarchy*
	- System prompt is the fast patch layer - does not require re-training
	- An agent like Claude Code or Codex is the model _plus_ a carefully engineered system prompt, _plus_ a set of tool definitions, _plus_ the harness that runs the tool-use loop.
		- Agent design = model + system prompt + tools + harness
	- Consumes context on every turn
- Context window - The amount of space a model can hold in its memory. All the text a language model can reference when generating a response. Think of this as the "working memory" of the model
	- Server side compaction - recommended strategy for handling long context windows and managing context in long-running conversations and agentic workflows
	- A constraint in serving that shapes your modeling decisions
- Context engineering - deciding *what* goes into the context window

### Foundation models × Eval
- LLM-as-judge (pairwise, scoring)
- Eval suites (Databricks Agent Evaluation, OpenAI Evals, Inspect)
- Golden datasets / ground truth construction
- Hallucination measurement, groundedness
- Benchmarks (MMLU, HumanEval, MT-Bench, GAIA)
- Pairwise preference evaluation
- Eval in CI / regression suites

### Foundation models × Serving
- LLM endpoints (Databricks Model Serving, OpenAI, Anthropic, Bedrock)
- Streaming responses
- Token economics, context windows, prompt caching
- Latency: TTFT (time to first token), throughput, P95
- Provisioned throughput vs. pay-per-token
- Multi-region failover, fallback chains
- Cost monitoring per request

### Foundation models × Ops
- Prompt versioning and management
- Trace observability (MLflow 3 traces, LangSmith, Langfuse)
- LLM cost and usage monitoring
- Eval regressions in CI / CD
- Production prompt drift, data drift on inputs
- Guardrails (input / output filtering, PII redaction)
- Agent observability (tool call traces, latency per step)

### Cross-cutting topics
- Privacy / PII detection and handling
- Bias and fairness across protected attributes
- Adversarial robustness
- Prompt injection, jailbreaks
- Output safety / content moderation (Llama Guard, Anthropic safety)
- Cost modeling at scale
- Latency budgets and SLOs
- Build vs. buy vs. wrap an API decision-making
- Reproducibility and lineage
- Regulatory considerations (EU AI Act, sector-specific)

---

## How to grow the backlog

- **Capture before classifying.** When you encounter a new term, add it to the cell that best fits. If you can't pick a cell, that's the most important note — it means you don't yet understand what category of thing it is.
- **Prune occasionally.** Some topics turn out to be aliases or marketing names for things already in the list. Merge them.
- **Don't aim for exhaustive.** Aim for *current*. The list should reflect what's worth knowing now, not every term that ever existed.
- **Tag topics you've actually used.** Distinguish "I've heard of this" from "I've shipped this." The second category is what builds the FDE muscle.
