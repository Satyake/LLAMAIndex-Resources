[Skip to content](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#_top)
# API/SDK Usage
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
## Quickstart
[Section titled “Quickstart”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#quickstart)
### Upload a document
[Section titled “Upload a document”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#upload-a-document)
First, upload a PDF using the [Files API](https://developers.llamaindex.ai/cloud-api-reference/upload-file-api-v-1-files-post).


Install the Python SDK if you haven’t already:
Terminal window```


pipinstallllama-cloud=1.0


```

Then upload your file:
```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





file_obj = client.files.create(file="path/to/your/file.pdf",purpose="split")




print(file_obj.id)


```

Install the TypeScript SDK if you haven’t already:
Terminal window```


npminstall@llamaindex/llama-cloud


```

Then upload your file:
```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const fileObj = await client.files.create({




file: fs.createReadStream('path/to/your/file.pdf'),




purpose: 'split',





console.log(fileObj.id);


```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/files'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-F'upload_file=@/path/to/your/file.pdf;type=application/pdf'


```

Save the returned `id` as your `FILE_ID`.
### Create a split job
[Section titled “Create a split job”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#create-a-split-job)
Create a split job with your file ID and category definitions:


```


job =await client.beta.split.create(




categories=[





"name": "invoice",




"description": "A commercial document requesting payment for goods or services, typically containing line items, totals, and payment terms"






"name": "contract",




"description": "A legal agreement between parties outlining terms, conditions, obligations, and signatures"






document_input={"type": "file_id", "value": file_id},



```

```


const job = await client.beta.split.create({




categories: [





name: "invoice",




description: "A commercial document requesting payment for goods or services, typically containing line items, totals, and payment terms"






name: "contract",




description: "A legal agreement between parties outlining terms, conditions, obligations, and signatures"






document_input: { type: "file_id", value: fileId },



```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs'\




-H'accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\





"document_input": {




"type": "file_id",




"value": "YOUR_FILE_ID"





"categories": [





"name": "invoice",




"description": "A commercial document requesting payment for goods or services, typically containing line items, totals, and payment terms"






"name": "contract",




"description": "A legal agreement between parties outlining terms, conditions, obligations, and signatures"





```

The response includes the job ID and initial status:
```



"id": "spl-abc123...",




"status": "pending"



```

### Poll for job completion
[Section titled “Poll for job completion”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#poll-for-job-completion)
Jobs are processed asynchronously. Poll the status until it reaches `completed` or `failed`:


```


completed_job =await client.beta.split.wait_for_completion(




job.id,




polling_interval=1.0,




verbose=True,



```

```


const completedJob = await client.beta.split.waitForCompletion(




job.id,




{ pollingInterval: 1.0, verbose: true, }



```

Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs/YOUR_JOB_ID'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

### Get the results
[Section titled “Get the results”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#get-the-results)
When the job completes successfully, the response includes the segmentation results:
```



"id": "spl-abc123...",




"status": "completed",




"result": {




"segments": [





"category": "invoice",




"pages": [1, 2, 3],




"confidence_category": "high"






"category": "contract",




"pages": [4, 5, 6, 7, 8],




"confidence_category": "high"






```

Each segment contains:
  * `category`: The assigned category name
  * `pages`: Array of page numbers (1-indexed) belonging to this segment
  * `confidence_category`: Confidence level (`high`, `medium`, or `low`)


## Advanced Options
[Section titled “Advanced Options”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#advanced-options)
### Allow uncategorized pages
[Section titled “Allow uncategorized pages”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#allow-uncategorized-pages)
By default, all pages must be assigned to one of your defined categories. To allow pages that don’t match any category to be grouped as `uncategorized`, use the `splitting_strategy` option:


```


job =await client.beta.split.create(




categories=[





"name": "invoice",




"description": "A commercial document requesting payment for goods or services"






document_input={"type": "file_id", "value": file_id},




splitting_strategy={"allow_uncategorized": True}



```

```


const job = await client.beta.split.create({




categories: [





name: "invoice",




description: "A commercial document requesting payment for goods or services"






document_input: { type: "file_id", value: fileId },




splitting_strategy: { allow_uncategorized: true }



```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs'\




-H'accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\





"document_input": {




"type": "file_id",




"value": "YOUR_FILE_ID"





"categories": [





"name": "invoice",




"description": "A commercial document requesting payment for goods or services"






"splitting_strategy": {




"allow_uncategorized": true




```

With this option, pages that don’t match `invoice` will be grouped into segments with `category: "uncategorized"`.
### Using project IDs
[Section titled “Using project IDs”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#using-project-ids)
If you’re working within a specific project, include the `project_id` query parameter:


```


job =await client.beta.split.create(




...,




project_id="YOUR_PROJECT_ID"



```

```


const job = await client.beta.split.create({




...,




project_id: "YOUR_PROJECT_ID"



```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/beta/split/jobs?project_id=YOUR_PROJECT_ID'\



```

## Full API Documentation
[Section titled “Full API Documentation”](https://developers.llamaindex.ai/python/cloud/split/getting_started/api/#full-api-documentation)
This is a subset of the available endpoints to help you get started.
You can see all available endpoints in our [full API documentation](https://developers.llamaindex.ai/cloud-api-reference/category/split).
