[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/qdrant/#_top)
# Qdrant
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Configure your own Qdrant instance as data sink.
## Configure via UI
[Section titled “Configure via UI”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/qdrant/#configure-via-ui)
## Configure via API / Client
[Section titled “Configure via API / Client”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/qdrant/#configure-via-api--client)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/qdrant/#tab-panel-290)
  * [ TypeScript (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/qdrant/#tab-panel-291)


```


from llama_cloud.types.data_sink_create_params import (




CloudQdrantVectorStore,






data_sink = client.data_sinks.create(




name="my-data-sink",




component=CloudQdrantVectorStore(




api_key='<api_key>',




collection_name='<collection_name>',




url='<url>',




max_retries='<max_retries>',# optional




client_kwargs='<client_kwargs>'# optional





sink_type="QDRANT",



```

```


const dataSink = await client.dataSinks.create({




name: 'my-data-sink',




component: {




api_key: '<api_key>',




collection_name: '<collection_name>',




url: '<url>',




max_retries: '<max_retries>'// optional




client_kwargs: '<client_kwargs>'// optional





sink_type: 'QDRANT',



```

```


from llama_cloud.types import CloudQdrantVectorStore





ds = {




'name': '<your-name>',




'sink_type': 'QDRANT',




'component': CloudQdrantVectorStore(




api_key='<api_key>',




collection_name='<collection_name>',




url='<url>',




max_retries='<max_retries>',# optional




client_kwargs='<client_kwargs>'# optional






data_sink = client.data_sinks.create_data_sink(request=ds)


```

```


const ds = {




'name': 'qdrant',




'sinkType': 'QDRANT',




'component': {




'api_key': '<api_key>',




'collection_name': '<collection_name>',




'url': '<url>',




'max_retries': '<max_retries>'// optional




'client_kwargs': '<client_kwargs>'// optional







data_sink =await client.dataSinks.createDataSink({




projectId: projectId,




body: ds



```

