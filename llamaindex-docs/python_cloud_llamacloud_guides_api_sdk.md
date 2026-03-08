[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#_top)
# Index API & Clients Guide
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
This guide highlights the core workflow for working with Index programmatically.
### App setup
[Section titled “App setup”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#app-setup)


Install API client package
```


pip install llama-cloud>=1.0


```

Import and configure the client (you can use either the sync or async client):
```


from llama_cloud import LlamaCloud, AsyncLlamaCloud





client =LlamaCloud(api_key='<llama-cloud-api-key>')


```

Install API client package
```


npm install @llamaindex/llama-cloud


```

Import and configure the client:
```


import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "<llama-cloud-api-key>",



```

## Create new index
[Section titled “Create new index”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#create-new-index)
### Upload files
[Section titled “Upload files”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#upload-files)


```


file_obj = client.files.create(file="/path/to/doc1.pdf",purpose="user_data")




print(file_obj.id)


```

```


import LlamaCloud from'llama-cloud';




import fs from'fs';





const clientnewLlamaCloud();




// Upload a file



const fileObj = await client.files.create({




file: fs.createReadStream('/path/to/doc1.pdf'),




purpose: "user_data",





const fileIdfileObj.id;





console.log(fileId);


```

### Configure data sources
[Section titled “Configure data sources”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#configure-data-sources)
  * [ TypeScript Client ](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#tab-panel-51)


```


from llama_cloud.types.data_source_create_params import ComponentCloudS3DataSource





data_source =await client.data_sources.create(




name="my-s3-data-source",




component=ComponentCloudS3DataSource(




bucket="my-bucket",




aws_access_id="my-access-id",




prefix="documents/",





source_type="S3",




project_id="my-project-id",



```

```


const dataSource = await client.dataSources.create({




name: 'my-s3-data-source',




component: {




bucket: 'my-bucket',




aws_access_id: 'my-access-id',




prefix: 'documents/',





source_type: 'S3',




project_id: 'my-project-id',






console.log(dataSource.id);


```

### Configure data sinks
[Section titled “Configure data sinks”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#configure-data-sinks)


```


from llama_cloud.types.data_sink_create_params import ComponentCloudPineconeVectorStore





data_sink = client.data_sinks.create(




name="my-pinecone-data-sink",




component=ComponentCloudPineconeVectorStore(




api_key="my-pinecone-api-key",




index_name="my-pinecone-index",





sink_type="PINECONE",






print(data_sink.id)


```

```


const dataSink = await client.dataSinks.create({




name: 'my-pinecone-data-sink',




component: {




api_key: 'my-pinecone-api-key',




index_name: 'my-pinecone-index',





sink_type: 'PINECONE',






console.log(dataSink.id);


```

### Setup transformation and embedding config
[Section titled “Setup transformation and embedding config”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#setup-transformation-and-embedding-config)
```

# Embedding config



embedding_config = {




'type': 'OPENAI_EMBEDDING',




'component': {




'api_key': '<YOUR_API_KEY_HERE>', # editable




'model_name': 'text-embedding-ada-002'# editable






# Transformation auto config



transform_config = {




'mode': 'auto',




'config': {




'chunk_size': 1024, # editable




'chunk_overlap': 20# editable




```

### Create index (i.e. pipeline)
[Section titled “Create index (i.e. pipeline)”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#create-index-ie-pipeline)


```


pipeline = client.pipelines.upsert({




name: 'my-first-index',




project_id: 'my-project-id',




data_sink_id: data_sink.id,




embedding_config: {




"type": 'OPENAI_EMBEDDING',




"component": {




"api_key": 'sk-1234',




"model_name": 'text-embedding-3-small',






llama_parse_parameters: {},




transform_config: {




"mode": 'auto',




"chunk_overlap": 128,




"chunk_size": 1028,







print(pipeline.id);


```

```

const pipeline = await client.pipelines.upsert({



name: 'my-first-index',




project_id: 'my-project-id',




data_sink_id: dataSink.id,




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




});



console.log(pipeline.id);

```

### Add files to index
[Section titled “Add files to index”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#add-files-to-index)


```


files = client.pipelines.files.create(




pipeline_id="some-id",




body=[





"file_id": file_obj.id,




"custom_metadata": {"category": "invoices"},





```

```


const files = await client.pipelines.files.create(pipeline.id, {




body: [





file_id: "1234",




custom_metadata: { source: 'generated' },








console.log(files.length);


```

### Add data sources to index
[Section titled “Add data sources to index”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#add-data-sources-to-index)


```


await client.pipelines.data_sources.update_data_sources(




pipeline_id=pipeline.id,




body=[





"data_source_id": data_source.id,




"sync_interval": 43200.0# Optional, scheduled sync frequency in seconds. In this case, every 12 hours.





```

```


const dataSources = await client.pipelines.dataSources.updateDataSources(pipeline.id, {




body: [





data_source_id: dataSourceId,




sync_interval: 43200.0// Optional, scheduled sync frequency in seconds. In this case, every 12 hours.





```

### Add documents to index
[Section titled “Add documents to index”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#add-documents-to-index)


```


documents =await client.pipelines.documents.create(




pipeline_id=pipeline.id,




body=[





"text": "This is my first document to be indexed.",




"metadata": {"source": "generated"},







print(f"Uploaded (documents)} documents to the index.")


```

```


const documents = await client.pipelines.documents.create(pipeline.id, {




body: [





text: 'This is my first document to be indexed.',




metadata: { source: 'generated' },







console.log(`Uploaded ${documents.length} documents to the index.`);


```

## Observe ingestion status & history
[Section titled “Observe ingestion status & history”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#observe-ingestion-status--history)
### Get index status
[Section titled “Get index status”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#get-index-status)
  * [ Python Sync Client ](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#tab-panel-62)
  * [ TypeScript Client ](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#tab-panel-63)


```

# Wait for indexing to complete



status_resp = client.pipelines.get_status(pipeline_id=pipeline.id)




while status_resp.status notin ("NOT_STARTED", "IN_PROGRESS"):




time.sleep(5)




status_resp = client.pipelines.get_status(pipeline_id=pipeline.id)





print(f"Indexing completed with status: {status_resp.status}")


```

```

// Wait for indexing to complete



let statusResp = await client.pipelines.getStatus(pipeline.id, {});




while (statusResp.status==='NOT_STARTED'|| statusResp.status==='IN_PROGRESS') {




awaitnewPromise((resolve)=>setTimeout(resolve, 5000));




statusResp =await client.pipelines.getStatus(pipeline.id, {});



```

## Run search (i.e. retrieval endpoint)
[Section titled “Run search (i.e. retrieval endpoint)”](https://developers.llamaindex.ai/python/cloud/llamacloud/guides/api_sdk/#run-search-ie-retrieval-endpoint)


```


results =await client.pipelines.retrieve(




pipeline_id=pipeline.id,




query="Some query",




dense_similarity_top_k=20,




sparse_similarity_top_k=20,




alpha=0.5,




enable_reranking=True,




rerank_top_n=5,






forin results.retrieval_nodes:




print(f"Score: {n.score}, Text: {n.node.text}")


```

```


const results = await client.pipelines.retrieve('your-existing-pipeline-id', {




query: 'Some query',




dense_similarity_top_k: 20,




sparse_similarity_top_k: 20,




alpha: 0.5,




enable_reranking: true,




rerank_top_n: 5,






for (const nof results.retrieval_nodes|| []) {




console.log(`Score: ${n.score}, Text: ${n.node?.text}`);



```

