[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/openai/#_top)
# OpenAI Embedding
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Embed data using OpenAI’s API.
## Configure via UI
[Section titled “Configure via UI”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/openai/#configure-via-ui)
  1. Select `OpenAI Embedding` from the `Embedding Model` dropdown.
  2. Enter your OpenAI API key.
  3. Select your preferred model:


  * `text-embedding-3-small` (Default)
  * `text-similarity-3-large`
  * `text-embedding-ada-002`


## Configure via API / Client
[Section titled “Configure via API / Client”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/openai/#configure-via-api--client)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/openai/#tab-panel-366)
  * [ TypeScript (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/openai/#tab-panel-367)


```


pipeline = client.pipelines.upsert(




name="test-pipeline",




project_id="my-project-id",




data_sink_id=None,# optional




embedding_config={




'type': 'OPENAI_EMBEDDING',




'component': {




'api_key': '<YOUR_API_KEY_HERE>', # editable




'model_name': 'text-embedding-3-small'# editable






llama_parse_parameters={},




transform_config={"mode": "auto", "chunk_overlap": 128, "chunk_size": 1028},



```

```


const pipeline = await client.pipelines.upsert({




name: 'my-first-index',




project_id: 'my-project-id',




data_sink_id: null, // optional




embedding_config: {




'type': 'OPENAI_EMBEDDING',




'component': {




'api_key': '<YOUR_API_KEY_HERE>', // editable




'model_name': 'text-embedding-3-small'// editable






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




'type': 'OPENAI_EMBEDDING',




'component': {




'api_key': '<YOUR_API_KEY_HERE>', # editable




'model_name': 'text-embedding-3-small'# editable






'data_sink_id': data_sink.id






pipeline = client.pipelines.upsert_pipeline(request=pipeline)


```

```


const pipeline = {




'name': 'test-pipeline',




'transform_config': {...},




'embedding_config': {




'type': 'OPENAI_EMBEDDING',




'component': {




'api_key': '<YOUR_API_KEY_HERE>', # editable




'model_name': 'text-embedding-3-small'editable






'dataSinkId': data_sink.id






await client.pipelines.upsertPipeline({



projectId: projectId,


body: pipeline


```

