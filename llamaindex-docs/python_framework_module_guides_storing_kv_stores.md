[Skip to content](https://developers.llamaindex.ai/python/framework/module_guides/storing/kv_stores/#_top)
# Key-Value Stores
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Key-Value stores are the underlying storage abstractions that power our [Document Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/docstores) and [Index Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/index_stores).
We provide the following key-value stores:
  * **Simple Key-Value Store** : An in-memory KV store. The user can choose to call `persist` on this kv store to persist data to disk.
  * **MongoDB Key-Value Store** : A MongoDB KV store.
  * **Tablestore Key-Value Store** : A Tablestore KV store.


See the [API Reference](https://developers.llamaindex.ai/python/framework-api-reference/storage/kvstore) for more details.
Note: At the moment, these storage abstractions are not externally facing.
