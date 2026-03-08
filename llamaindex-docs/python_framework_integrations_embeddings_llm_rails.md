[Skip to content](https://developers.llamaindex.ai/python/framework/integrations/embeddings/llm_rails/#_top)
# LLMRails Embeddings 
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
If you’re opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.
```


%pip install llama-index-embeddings-llm-rails


```

```


!pip install llama-index


```

```

# imports




from llama_index.embeddings.llm_rails import LLMRailsEmbedding


```

```

# get credentials and create embeddings




import os





api_key = os.environ.get("API_KEY","your-api-key")




model_id = os.environ.get("MODEL_ID","your-model-id")






embed_model =LLMRailsEmbedding(model_id=model_id,api_key=api_key)





embeddings = embed_model.get_text_embedding(




"It is raining cats and dogs here!"



```

