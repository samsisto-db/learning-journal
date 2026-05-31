Requests to the Anthropic API should not be made directly from client-side code because:
- API requests require a secret API key for authentication and exposing this in client code is a serious risk, anyone could extract the key and make unauthorized requests

Overall flow for a request to Anthropic API from a chat app:
- Request to your server from the client
- Your server requests to Anthropic API
- Anthropic API generates a response (model processing)
- Returns response to your server
- Returns response to the client

Anthropic API:
- Tokenizations: User input is broken out into tokens
- Embedding: Number based definition of a token or a word
- Contextualization: Each embedding is adjusted based on the embedding around it
- Generation: Text actually gets written based on the probability for each next word

Anthropic API and Claude are stateless -> do not store any messages
To have a conversation, need to have:
- manually maintain a list of those messages
- provide that list of messages on each follow up

Prompt engineering - how to write better prompts
Techniques:
- Be clear, direct and specific about what you are looking for
- Guidelines:
	- List qualities that the output should have
	- Provide the steps the model should follow

Prompt evaluation - how to measure the effectiveness of those prompts
- Run your prompt through an evaluation pipeline, you get objective metrics about its performance

Tool use with Claude - when the model has limitations, we can extend its capabilities through tools rather than trying to work around those limitations in prompts
- Tools are the mechanism by which an LLM takes actions beyond text generation
- Claude requests the use of these tools back to the developer server or MCP server, those results are returned back to the LLM

Complete multi-turn workflow with tool calling:
- Send user message to Claude with available tools
- Claude responds with text and/or tool requests
- Execute all requested tools and create result blocks
- Send tool results back as a user message
- Repeat until Claude provides a final answer

When streaming output with tools responses will be sent back to the server in chunks. Anthropic API will validate the chunks but you can also send them back to the server in pieces but you need to be able to handle potentially invalid json

MCP - Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Think of it as a way to shift the burden of tool definitions and execution away from your server to specialized MCP servers.
- Think of MCP as some sort of interface to some outside service. Exposes a set of tools related to some outside service

	- The MCP Python SDK transforms what used to be a complex process of writing tool definitions into something that feels natural for Python developers. You focus on the business logic while the SDK handles the protocol details.

MCP client - allows us to access functionality that exists within the MCP server
![[Pasted image 20260531152404.png|697]]

Resources expose data, tools perform an actions
Resources provide a clean way to make data available to MCP clients, enabling features like document mentions, file browsing, or any scenario where you need to fetch information from your server

Tools, resources and prompts all exposed by MCP servers
Tools - model controlled
Resources - app controlled
Prompts - user controlled