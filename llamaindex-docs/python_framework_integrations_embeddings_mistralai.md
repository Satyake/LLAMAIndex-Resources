[Skip to content](https://developers.llamaindex.ai/python/framework/integrations/embeddings/mistralai/#_top)
# MistralAI Embeddings 
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
If you’re opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.
```


%pip install llama-index-embeddings-mistralai


```

```


!pip install llama-index


```

```

# imports



from llama_index.embeddings.mistralai import MistralAIEmbedding


```

```

# get API key and create embeddings



api_key ="YOUR API KEY"




model_name ="mistral-embed"




embed_model =MistralAIEmbedding(model_name=model_name,api_key=api_key)





embeddings = embed_model.get_text_embedding("La Plateforme - The Platform")


```

```


print(f"Dimension of embeddings: (embeddings)}")


```

```

Dimension of embeddings: 1024

```

```


embeddings[:5]


```

```

[-0.0299224853515625,



-0.0028362274169921875,




0.0282745361328125,




-0.034759521484375,




-0.0017366409301757812]


```

