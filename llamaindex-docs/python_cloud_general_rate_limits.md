[Skip to content](https://developers.llamaindex.ai/python/cloud/general/rate_limits/#_top)
# Rate Limits
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
LlamaCloud implements rate limiting on specific high-traffic endpoints to ensure fair usage and service stability across all customers:
Endpoint | QPS (Queries Per Second) | Window | API Route  
---|---|---|---  
File Upload | 50 | 5 seconds | POST `/api/v1/files`  
Parse Upload | 50 | 10 seconds | POST `/api/v1/parsing/upload`  
These rate limits are applied at different scopes as indicated above and reset at the end of each time window. File upload limits are applied per project, while Parse upload limits are applied per organization.
Free tier organizations have lower rate limits, at 20 requests per minute.
## Rate Limit Response
[Section titled “Rate Limit Response”](https://developers.llamaindex.ai/python/cloud/general/rate_limits/#rate-limit-response)
When you exceed the rate limit, the API will return a `429 Too Many Requests` status code.
