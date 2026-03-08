[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/azure/#_top)
# Azure Embedding
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Embed data using Azure’s API.
## Configure via UI
[Section titled “Configure via UI”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/azure/#configure-via-ui)
  1. Select `Azure Embedding` from the `Embedding Model` dropdown.
  2. Enter your Azure API key, deployment name, endpoint name and API version.


## Configure via API / Client
[Section titled “Configure via API / Client”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/azure/#configure-via-api--client)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/azure/#tab-panel-346)
  * [ TypeScript (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/embedding_models/azure/#tab-panel-347)


```


pipeline = client.pipelines.upsert(




name="test-pipeline",




project_id="my-project-id",




data_sink_id=None,# optional




embedding_config={




'type': 'AZURE_EMBEDDING',




'component': {




'azure_deployment': '<YOUR_DEPLOYMENT_NAME>', # editable




'api_key': '<YOUR_AZUREOPENAI_API_KEY>', # editable




'azure_endpoint': '<YOUR AZURE_ENDPOINT>', # editable




'api_version': '<YOUR AZURE_API_VERSION>', # editable






llama_parse_parameters={},




transform_config={"mode": "auto", "chunk_overlap": 128, "chunk_size": 1028},



```

```


const pipeline = await client.pipelines.upsert({




name: 'my-first-index',




project_id: 'my-project-id',




data_sink_id: null, // optional




embedding_config: {




'type': 'AZURE_EMBEDDING',




'component': {




'deployment_name': '<YOUR_DEPLOYMENT_NAME>', // editable




'api_key': '<YOUR_AZUREOPENAI_API_KEY>', // editable




'azure_endpoint': '<YOUR AZURE_ENDPOINT>', // editable




'api_version': '<YOUR AZURE_API_VERSION>', // editable






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




'type': 'AZURE_EMBEDDING',




'component': {




'azure_deployment': '<YOUR_DEPLOYMENT_NAME>', # editable




'api_key': '<YOUR_AZUREOPENAI_API_KEY>', # editable




'azure_endpoint': '<YOUR AZURE_ENDPOINT>', # editable




'api_version': '<YOUR AZURE_API_VERSION>', # editable






'data_sink_id': data_sink.id






pipeline = client.pipelines.upsert_pipeline(request=pipeline)


```

```


const pipeline = {




'name': 'test-pipeline',




'transform_config': {...},




'embedding_config': {




'type': 'AZURE_EMBEDDING',




'component': {




'deployment_name': '<YOUR_DEPLOYMENT_NAME>', # editable




'api_key': '<YOUR_AZUREOPENAI_API_KEY>', # editable




'azure_endpoint': '<YOUR AZURE_ENDPOINT>', # editable




'api_version': '<YOUR AZURE_API_VERSION>', # editable






'dataSinkId': data_sink.id






await client.pipelines.upsertPipeline({



projectId: projectId,


body: pipeline


```

