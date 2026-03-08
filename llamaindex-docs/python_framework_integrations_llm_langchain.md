[Skip to content](https://developers.llamaindex.ai/python/framework/integrations/llm/langchain/#_top)
# LangChain LLM 
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
```


%pip install llama-index-llms-langchain


```

```


from langchain.llms import OpenAI


```

```


from llama_index.llms.langchain import LangChainLLM


```

```


llm =LangChainLLM=OpenAI())


```

```


response_gen = llm.stream_complete("Hi this is")


```

```


for delta in response_gen:




print(delta.delta,end="")


```

```


a test




Hello! Welcome to the test. What would you like to learn about?

```

