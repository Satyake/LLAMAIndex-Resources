[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/managed/#_top)
# Managed Data Sink
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Use LlamaCloud managed index as data sink.
## Configure via UI
[Section titled “Configure via UI”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/managed/#configure-via-ui)
## Configure via API / Client
[Section titled “Configure via API / Client”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/managed/#configure-via-api--client)
Simply set `data_sink_id` to None when creating a pipeline


```


from llama_cloud import AsyncLlamaCloud, LlamaCloud




from llama_cloud.types.pipeline_create_params import (




EmbeddingConfigOpenAIEmbeddingConfig,




EmbeddingConfigOpenAIEmbeddingConfigComponent,





client =LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])





pipeline = client.pipelines.create(




name="my-first-index",




project_id="my-project-id",




data_sink_id=None,# Use managed data sink




embedding_config=EmbeddingConfigOpenAIEmbeddingConfig(




component=EmbeddingConfigOpenAIEmbeddingConfigComponent(




api_key="sk-1234",




model_name="text-embedding-3-small",





type="OPENAI_EMBEDDING",





llama_parse_parameters={"parse_mode": "parse_document_with_agent", "model": "openai-gpt-4-1-mini"},




transform_config={"mode": "auto", "chunk_overlap": 128, "chunk_size": 1028},



```

```


const pipeline = await client.pipelines.upsert({




name: 'my-first-index',




project_id: 'my-project-id',




data_sink_id: null, // Use managed data sink




embedding_config: {




type: 'OPENAI_EMBEDDING',




component: {




api_key: 'sk-1234',




model_name: 'text-embedding-3-small',






llama_parse_parameters: {},




transform_config: {




mode: 'auto',




chunk_overlap: 128,




chunk_size: 1028,




```

