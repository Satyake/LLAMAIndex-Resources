[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/milvus/#_top)
# Milvus
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Configure your own Milvus Vector DB instance as data sink.
## Configure via UI
[Section titled “Configure via UI”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/milvus/#configure-via-ui)
## Configure via API / Client
[Section titled “Configure via API / Client”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/milvus/#configure-via-api--client)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/milvus/#tab-panel-276)
  * [ TypeScript (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sinks/milvus/#tab-panel-277)


```


from llama_cloud.types.data_sink_create_params import (




CloudMilvusVectorStore,






data_sink = client.data_sinks.create(




name="my-data-sink",




component=CloudMilvusVectorStore(




uri='<uri>',




collection_name='<collection_name>',




token='<token>',# optional




# embedding dimension




dim='<dim>'# optional





sink_type="MILVUS",



```

```


const dataSink = await client.dataSinks.create({




name: 'my-data-sink',




component: {




uri: '<uri>',




collection_name: '<collection_name>',




token: '<token>'// optional




// embedding dimension




dim: '<dim>'// optional





sink_type: 'MILVUS',



```

```


from llama_cloud.types import CloudMilvusVectorStore






'name': '<your-name>',




'sink_type': 'MILVUS',




'component': CloudMilvusVectorStore(




uri='<uri>',




collection_name='<collection_name>',




token='<token>',# optional




# embedding dimension




dim='<dim>'# optional






data_sink = client.data_sinks.create_data_sink(request=ds)


```

```


const ds = {




'name': 'milvus',




'sinkType': 'MILVUS',




'component': {




'uri': '<uri>',




'collection_name': '<collection_name>',




'token': '<token>'// optional




// embedding dimension




'dim': '<dim>'// optional







data_sink =await client.dataSinks.createDataSink({




projectId: projectId,




body: ds



```

