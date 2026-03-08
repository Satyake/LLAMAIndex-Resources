[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/huggingface/#_top)
# HuggingFace Embedding
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Embed data using HuggingFace’s Inference API.
## Configure via UI
[Section titled “Configure via UI”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/huggingface/#configure-via-ui)
  1. Select `HuggingFace Embedding` from the `Embedding Model` dropdown.
  2. Enter your HuggingFace API key.
  3. Enter your HuggingFace model name or URL, e.g. `BAAI/bge-small-en-v1.5`.


## Configure via API / Client
[Section titled “Configure via API / Client”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/huggingface/#configure-via-api--client)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/huggingface/#tab-panel-362)
  * [ TypeScript (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/huggingface/#tab-panel-363)


```


pipeline = client.pipelines.upsert(




name="test-pipeline",




project_id="my-project-id",




data_sink_id=None,# optional




embedding_config={




'type': 'HUGGINGFACE_API_EMBEDDING',




'component': {




'token': 'hf_...',




'model_name': 'BAAI/bge-small-en-v1.5',






llama_parse_parameters={},




transform_config={"mode": "auto", "chunk_overlap": 128, "chunk_size": 1028},



```

```


const pipeline = await client.pipelines.upsert({




name: 'my-first-index',




project_id: 'my-project-id',




data_sink_id: null, // optional




embedding_config: {




'type': 'HUGGINGFACE_API_EMBEDDING',




'component': {




'token': 'hf_...',




'model_name': 'BAAI/bge-small-en-v1.5',






llama_parse_parameters: {},




transform_config: {




mode: 'auto',




chunk_overlap: 128,




chunk_size: 1028,




```

```


pipeline = {




'name': 'test-pipeline',




'transform_config': {...},




'embedding_config': {




'type': 'HUGGINGFACE_API_EMBEDDING',




'component': {




'token': 'hf_...',




'model_name': 'BAAI/bge-small-en-v1.5',






'data_sink_id': data_sink.id






pipeline = client.pipelines.upsert_pipeline(request=pipeline)


```

```


const pipeline = {




'name': 'test-pipeline',




'transform_config': {...},




'embedding_config': {




'type': 'HUGGINGFACE_API_EMBEDDING',




'component': {




'token': 'hf_...',




'model_name': 'BAAI/bge-small-en-v1.5',






'dataSinkId': data_sink.id






await client.pipelines.upsertPipeline({



projectId: projectId,


body: pipeline


```

