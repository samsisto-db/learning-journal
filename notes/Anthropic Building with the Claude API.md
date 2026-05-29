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
