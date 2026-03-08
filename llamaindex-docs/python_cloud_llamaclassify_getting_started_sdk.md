[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaclassify/getting_started/sdk/#_top)
# Classify SDK
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
This guide shows how to classify documents using the SDK. You will:
  * Create classification rules
  * Upload files
  * Submit a classify job
  * Read predictions (type, confidence, reasoning)


The SDK is available in [llama-cloud-py](https://github.com/run-llama/llama-cloud-py) or [llama-cloud-ts](https://github.com/run-llama/llama-cloud-ts).
## Setup
[Section titled “Setup”](https://developers.llamaindex.ai/python/cloud/llamaclassify/getting_started/sdk/#setup)
First, [get an API key](https://developers.llamaindex.ai/python/cloud/general/api_key) and record it for safe keeping.
You can set this as an environment variable `LLAMA_CLOUD_API_KEY` or pass it directly to the SDK at runtime.
Then, install dependencies:


Terminal window```


pipinstallllama-cloud=1.0


```

Terminal window```


npminstall@llamaindex/llama-cloud


```

Terminal window```


pipinstallllama-cloud-services


```

## Quick start
[Section titled “Quick start”](https://developers.llamaindex.ai/python/cloud/llamaclassify/getting_started/sdk/#quick-start)
Using the classify API consists of a few main steps
  1. Uploading a file and getting a `file_id`
  2. Creating a classify job
  3. Waiting for the job to finish
  4. Fetching the final result


The SDK will contain both a helper method to automate these steps:
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamaclassify/getting_started/sdk/#tab-panel-43)


```


import os




from llama_cloud import LlamaCloud, AsyncLlamaCloud




# For async usage, use `AsyncLlamaCloud()`



client =LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])




# Upload a file



file_obj = client.files.create(file="/path/to/doc1.pdf",purpose="classify")




file_id = file_obj.id




# Upload and wait for completion



result = client.classifier.classify(




file_ids=[file_id],




rules=[





"type": "invoice",




"description": "Documents that contain an invoice number, invoice date, bill-to section, and line items with totals.",






"type": "receipt",




"description": "Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page.",






parsing_configuration={




"lang": "en",




"max_pages": 5# optional, parse at most 5 pages




# "target_pages": [1],     # optional, parse only specific pages (1-indexed), can't be used with max_pages





mode="FAST",# or "MULTIMODAL"





# Print the classification results



for item in result.items:




assert item.result isnotNone




print(f"Classified type: {item.result.type}")




print(f"Confidence: {item.result.confidence}")




print(f"Reasoning: {item.result.reasoning}")


```

```


import LlamaCloud from'@llamaindex/llama-cloud';




import fs from'fs';





const clientnewLlamaCloud();




// Upload a file



const fileObj = await client.files.create({




file: fs.createReadStream('/path/to/doc1.pdf'),




purpose: "classify",





const fileIdfileObj.id;




// Upload and wait for completion



const result = await client.classifier.classify({




file_ids: [fileId],




rules: [





type: 'invoice',




description: 'Documents that contain an invoice number, invoice date, bill-to section, and line items with totals.',






type: 'receipt',




description: 'Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page.',






parsing_configuration: {




lang: 'en',




max_pages: 5,




// target_pages: [1],  // Optional: specify particular pages to parse, cannot be used with max_pages





mode: 'FAST'// or 'MULTIMODAL'





// Print the classification results



for (const itemof result.items) {




if (item.result) {




console.log(`Classified type: ${item.result.type}`);




console.log(`Confidence: ${item.result.confidence}`);




console.log(`Reasoning: ${item.result.reasoning}`);




```

```


import os




from llama_cloud.client import AsyncLlamaCloud




from llama_cloud.types import ClassifierRule, ClassifyParsingConfiguration, ParserLanguages




from llama_cloud_services.beta.classifier.client import LlamaClassify  # helper wrapper





client =AsyncLlamaCloud(token=os.environ["LLAMA_CLOUD_API_KEY"])




project_id ="your-project-id"




classifier =LlamaClassify(client,project_id=project_id)





rules =[




ClassifierRule(




type="invoice",




description="Documents that contain an invoice number, invoice date, bill-to section, and line items with totals."





ClassifierRule(




type="receipt",




description="Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page."







parsing =ClassifyParsingConfiguration(




lang=ParserLanguages.EN,




max_pages=5,# optional, parse at most 5 pages




# target_pages=[1]        # optional, parse only specific pages (1-indexed), can't be used with max_pages






# for async usage, use `await classifier.aclassify(...)`




results = classifier.classify(




rules=rules,




files=[




"/path/to/doc1.pdf",




"/path/to/doc2.pdf",





parsing_configuration=parsing,




mode="FAST",# or "MULTIMODAL"






for item in results.items:




# in cases of partial success, some of the items may not have a result




if item.result isNone:




print(f"Classification job {item.classify_job_id} error-ed on file {item.file_id}")




continue




print(item.file_id, item.result.type, item.result.confidence)




print(item.result.reasoning)


```

Or you can run each step individually:


```


import os




from llama_cloud import LlamaCloud, AsyncLlamaCloud




# For async usage, use `AsyncLlamaCloud()`



client =LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])




# Upload a file



file_obj = client.files.create(file="/path/to/doc1.pdf",purpose="classify")




file_id = file_obj.id




# Upload to create a job



job = client.classifier.jobs.create(




file_ids=[file_id],




rules=[





"type": "invoice",




"description": "Documents that contain an invoice number, invoice date, bill-to section, and line items with totals.",






"type": "receipt",




"description": "Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page.",






parsing_configuration={




"lang": "en",




"max_pages": 5# optional, parse at most 5 pages




# "target_pages": [1],     # optional, parse only specific pages (1-indexed), can't be used with max_pages





mode="FAST",# or "MULTIMODAL"





# Poll for job completion



status = client.classifier.jobs.get(classify_job_id=job.id)




while status.status =="PENDING":




time.sleep(2)




status = client.classifier.jobs.get(classify_job_id=job.id)





result = client.classifier.jobs.get_results(classify_job_id=job.id)




# Print the classification results



for item in result.items:




assert item.result isnotNone




print(f"Classified type: {item.result.type}")




print(f"Confidence: {item.result.confidence}")




print(f"Reasoning: {item.result.reasoning}")


```

```


import LlamaCloud from'llama-cloud';




import fs from'fs';





const clientnewLlamaCloud();




// Upload a file



const fileObj = await client.files.create({




file: fs.createReadStream('/path/to/doc1.pdf'),




purpose: "classify",





const fileIdfileObj.id;




// Upload and wait for completion



const job = await client.classifier.jobs.create({




file_ids: [fileId],




rules: [





type: 'invoice',




description: 'Documents that contain an invoice number, invoice date, bill-to section, and line items with totals.',






type: 'receipt',




description: 'Short purchase receipts, typically from POS systems, with merchant, items and total, often a single page.',






parsing_configuration: {




lang: 'en',




max_pages: 5,




// target_pages: [1],  // Optional: specify particular pages to parse, cannot be used with max_pages





mode: 'FAST'// or 'MULTIMODAL'





// Poll for job completion



let status = await client.classifier.jobs.get({ classify_job_id: job.id });




while (status.status==='PENDING') {




awaitnewPromise((resolve)=>setTimeout(resolve, 2000));




status =await client.classifier.jobs.get({ classify_job_id: job.id });






const result = await client.classifier.jobs.getResults({ classify_job_id: job.id });




// Print the classification results



for (const itemof result.items) {




if (item.result) {




console.log(`Classified type: ${item.result.type}`);




console.log(`Confidence: ${item.result.confidence}`);




console.log(`Reasoning: ${item.result.reasoning}`);




```

Notes:
  * `ClassifierRule` requires a `type` and a descriptive `description` that the model can follow.
  * `ClassifyParsingConfiguration` is optional; set `lang`, `max_pages`, or `target_pages` to control parsing.
  * In cases of partial failure, some of the items may not have a result (i.e. `results.items[*].result` could be `None`).


## Classification modes
[Section titled “Classification modes”](https://developers.llamaindex.ai/python/cloud/llamaclassify/getting_started/sdk/#classification-modes)
LlamaClassify supports two modes:
Mode | Credits per Page | Description  
---|---|---  
`FAST` | 1 | Text-based classification (default)  
`MULTIMODAL` | 2 | Vision-based classification for visual documents  
Use **Multimodal mode** when your documents contain images, charts, or complex layouts that are important for classification:
```


results = client.classifier.classify(




rules=rules,




files=["/path/to/visual-doc.pdf"],




mode="MULTIMODAL",# use vision model for classification



```

## Tips for writing good rules
[Section titled “Tips for writing good rules”](https://developers.llamaindex.ai/python/cloud/llamaclassify/getting_started/sdk/#tips-for-writing-good-rules)
  * Be specific about content features that distinguish the type.
  * Include key fields the document usually contains (e.g., invoice number, total amount).
  * Add multiple rules when needed to cover distinct patterns.
  * Start simple, test on a small set, then refine.


