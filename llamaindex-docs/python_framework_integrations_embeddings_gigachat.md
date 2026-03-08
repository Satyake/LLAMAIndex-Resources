[Skip to content](https://developers.llamaindex.ai/python/framework/integrations/embeddings/gigachat/#_top)
# GigaChat 
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
```


%pip install llama-index-embeddings-gigachat


```

```


!pip install llama-index


```

```


from llama_index.embeddings.gigachat import GigaChatEmbedding





gigachat_embedding =GigaChatEmbedding(




auth_data="your-auth-data",




scope="your-scope",# Set scope 'GIGACHAT_API_PERS' for personal use or 'GIGACHAT_API_CORP' for corporate use.






queries_embedding = gigachat_embedding._get_query_embeddings(




["This is a passage!", "This is another passage"]





print(queries_embedding)





text_embedding = gigachat_embedding._get_text_embedding("Where is blue?")




print(text_embedding)


```

