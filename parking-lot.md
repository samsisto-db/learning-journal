5/28/2026
- good work on system prompt and context window. Left off at KV cache, prompt caching and transformer architecture

5/27/2026
- Baseten: https://www.baseten.co/products/dedicated-inference/
	- SA job posting: https://jobs.ashbyhq.com/baseten/c64515f9-a8f7-4633-9340-17cda56b1ef0?utm_source=worNde4l4L
- ClickHouse

5/26/2026
- Reviewed and calcified Neon's Lakebase architecture

5/23/2026
- Ran through a pretty involved DABs example; Let's pivot to some of the data engineering fundamentals and training there to nail some of that down. I think there is likely a good DABs example in that training that might help to visit
- DE fundamentals -> revisit DABs, practice with fundamentals -> AI / ML fundamentals, look at FDE like positions -> GenAI, MCP, etc.

5/23/2026
- Read Git chapters intro
- flesh out a plan for ML / AI / GenAI study


## Certs
- Databricks data engineering
- Anthropic Building with the Claude API: https://anthropic.skilljar.com/claude-with-the-anthropic-api
	- ~10 hours
	- Interpret how the messaging example here aligns with the chatbot/lakebase set up that you deployed previously
- NVIDIA Generative AI Associate: https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/
	- ~32 hours
	- Look at study guide in the PDF with recommended readings
	- Skillcertpro practice test
	- Timeline for cert completion


## Running list of open items to dig into

- **Need to develop framework on overall learning on AI / GenAI / ML etc.**
	- Actually build something?
	- Something with document processing
- Stanford Online videos: https://www.youtube.com/watch?v=_NLHFoVNlbg&list=PLoROMvodv4rNRRGdS0rBbXOUGA0wjdh1X

- KV cache - transformer architecture is a "next token predictor". To do that prediction, you need to understand how each token relates to all the tokens around it (Q, K, V). Instead of recomputing that key and value for each token, it's stored in the GPU's memory as the model computes the next tokens.
- Transformer architecture
- Prompt caching

- Review chatbot and lakebase integration that you deployed in SLED azure env.

- Lakebase branching
- Lakebase to save the state of an agent vs. using an .md file
- MCP servers 
- Agentic set up and configurations
- Google FDE requirements:
	- Python, PyTorch
	- Multi-agent systems (LangGraph, CrewAI, ADK)
	- Complex patterns (ReAct, self-reflection, hierarchical delegation)
	- LLM-native metrics (tokens/sec, cost-per-request), optimizing state management
- Reyden
- Chain of thought reasoning