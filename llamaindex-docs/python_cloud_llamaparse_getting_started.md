[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#_top)
# Getting Started
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Quickly start parsing documents with LlamaParse—whether you prefer Python, TypeScript, or using the web UI. This guide walks you through creating an API key and running your first job.
## Get your API Key
[Section titled “Get your API Key”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#get-your-api-key)
🔑 **Before you begin** : You’ll need an API key to access LlamaParse services.
[**Get your API key →**](https://developers.llamaindex.ai/python/cloud/general/api_key)
## Choose Your Setup
[Section titled “Choose Your Setup”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#choose-your-setup)


#### Using LlamaParse in the Web UI
[Section titled “Using LlamaParse in the Web UI”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#using-llamaparse-in-the-web-ui)
If you’re non-technical or just want to quickly sandbox LlamaParse, the web interface is the easiest way to get started.
#### Step-by-Step Workflow
[Section titled “Step-by-Step Workflow”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#step-by-step-workflow)
  1. Go to [LlamaCloud](https://cloud.llamaindex.ai/parse)
  2. Choose a parsing **Tier** from **Recommended Settings** or switch to **Advanced settings** for a custom configuration
  3. Upload your document
  4. Click **Parse** and view your parsed results right in the browser


#### Choosing a Tier
[Section titled “Choosing a Tier”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#choosing-a-tier)
LlamaParse offers four main tiers:
  * [**Cost Effective**](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#cost-effective) – Optimized for speed and cost. Best for text-heavy documents with minimal structure.
  * [**Agentic**](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#agentic) – Works well with documents that have images and diagrams, but may struggle with complex layouts.
  * [**Agentic Plus**](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#agentic-plus) – Maximum fidelity. Best for complex layouts, tables, and visual structure.
  * [**Fast**](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#fast) – A special mode that only outputs the spatial text of your documents, but not the markdown.


#### Install the package
[Section titled “Install the package”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#install-the-package)
Terminal window```


pipinstallllama_cloud=1.0


```

#### Parse in Python
[Section titled “Parse in Python”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#parse-in-python)
##### Usage
[Section titled “Usage”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#usage)
```


from llama_cloud import LlamaCloud, AsyncLlamaCloud




import httpx




import re





client =AsyncLlamaCloud(api_key="llx-...")




# Upload and parse a document



file_obj =await client.files.create(file="./attention_is_all_you_need.pdf",purpose="parse")





result =await client.parsing.parse(




file_id=file_obj.id,




tier="agentic",




version="latest",





# Options specific to the input file type, e.g. html, spreadsheet, presentation, etc.




input_options={},





# Control the output structure and markdown styling




output_options={




"markdown": {




"tables": {




"output_tables_as_markdown": False,






# Saving images for later retrieval




"images_to_save": ["screenshot"],






# Options for controlling how we process the document




processing_options={




"ignore": {




"ignore_diagonal_text": True,





"ocr_parameters": {




"languages": ["fr"]







# Parsed content to include in the returned response




expand=["text", "markdown", "items", "images_content_metadata"],






print(result.markdown.pages[0].markdown)




print(result.text.pages[0].text)




# Iterate over page items to find tables



for page in result.items.pages:




for item in page.items:




ifisinstance(item, ItemsPageStructuredResultPageItemTableItem):




print(f"Table found on page {page.page_number} with (item.rows)} rows and {item.b_box} location")





defis_page_screenshot(image_name: str) -> bool:




return re.match(r"^page_(\d+)\.jpg$", image_name) isnotNone




# Iterate over results looking for page screenshots



for image in result.images_content_metadata.images:




if image.presigned_url isNoneornotis_page_screenshot(image.filename):




continue





print(f"Downloading {image.filename}, {image.size_bytes} bytes")




withopen(f"{image.filename}","wb") as img_file:




asyncwith httpx.AsyncClient() as http_client:




response =await http_client.get(image.presigned_url)




img_file.write(response.content)


```

#### Install the package
[Section titled “Install the package”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#install-the-package-1)
Terminal window```


npminstall@llamaindex/llama-cloud


```

#### Parse in TypeScript
[Section titled “Parse in TypeScript”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#parse-in-typescript)
Let’s create a `parse.ts` file and put our dependencies in it:
```


import LlamaCloud from'@llamaindex/llama-cloud';




import fs from'fs';





const clientnewLlamaCloud({ apiKey: process.env.LLAMA_CLOUD_API_KEY });





console.log('Uploading file...');




// Upload and parse a document



const fileObj = await client.files.create({




file: fs.createReadStream('./attention_is_all_you_need.pdf'),




purpose: 'parse',






console.log('Parsing file...');





const result = await client.parsing.parse({




file_id: fileObj.id,




tier: 'agentic',




version: 'latest',





// Options specific to the input file type, e.g. html, spreadsheet, presentation, etc.




input_options: {},





// Control the output structure and markdown styling




output_options: {




markdown: {




tables: {




output_tables_as_markdown: false,






// Saving images for later retrieval




images_to_save: ['screenshot'],






// Options for controlling how we process the document




processing_options: {




ignore: {




ignore_diagonal_text: true,





ocr_parameters: {




languages: ['en'],







// Parsed content to include in the returned response




expand: ['text', 'markdown', 'items', 'images_content_metadata'],






console.log(result.markdown.pages[0].markdown);




console.log(result.text.pages[0].text);




// Iterate over page items to find tables



for (const pageof result.items.pages) {




for (const itemof page.items) {




if (item.type==='table') {




console.log(




`Table found on page ${page.page_number} with ${item.rows.length} rows and ${JSON.stringify(item.bbox)} location`









const isPageScreenshot(imageName) =>/^page_(\d+)\.jpg$/.test(imageName);




// Iterate over results looking for page screenshots



for (const imageof result.images_content_metadata.images) {




if (!image.presigned_url||!isPageScreenshot(image.filename)) {




continue;






console.log(`Downloading ${image.filename}, ${image.size_bytes} bytes`);




const response = await fetch(image.presigned_url);




const bufferBuffer.from(await response.arrayBuffer());




fs.writeFileSync(image.filename, buffer);



```

Run the script with:
Terminal window```


LLAMA_CLOUD_API_KEY="llx-..."npxts-nodeparse.ts


```

#### Using the REST API
[Section titled “Using the REST API”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#using-the-rest-api)
If you would prefer to use a raw API, the REST API lets you integrate parsing into any environment—no client required. Below are sample endpoints to help you get started.
#### 1. Upload a file
[Section titled “1. Upload a file”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#1-upload-a-file)
Send a document to the File API:
Terminal window```


curl-XPOST\




https://api.cloud.llamaindex.ai/api/v1/files/\




-H'Accept: application/json'\




-H'Content-Type: multipart/form-data'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-F'file=@/path/to/your/file.pdf;type=application/pdf'


```

Get the `id` from the response:
```



"id": "cafe1337-e0dd-4762-b5f5-769fef112558",




```

#### 2. Parse the file
[Section titled “2. Parse the file”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#2-parse-the-file)
Pass the File ID to LlamaParse as a `file_id`. Don’t forget to select a tier as well:
Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v2/parse/'\




-H'Accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--data'{




"file_id": "<file_id>",




"tier": "agentic_plus",




"version": "latest"



```

You’ll get a `job_id` as a response:
```



"id": "c0defee1-76a0-42c3-bbed-094e4566b762",




"status": "PENDING"



```

#### 3. Check job status and retrieve results
[Section titled “3. Check job status and retrieve results”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#3-check-job-status-and-retrieve-results)
Use the `job_id` returned from the parse step to check status and retrieve results. The result endpoint returns metadata (including status) along with the requested result types:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse/<job_id>/result?include_markdown=true'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

The response includes a `metadata` object with the job `status` (e.g., `PENDING`, `SUCCESS`, `ERROR`). Once status is `SUCCESS`, the requested result data will be included.
Available query parameters:
  * `include_text=true` - Include spatial text result
  * `include_markdown=true` - Include markdown result
  * `include_items=true` - Include items tree result
  * `include_json_output=true` - Include JSON output result


See more details in our [API Reference](https://developers.llamaindex.ai/cloud-api-reference/category/parse)
#### Example
[Section titled “Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#example)
Here is an example notebook for [Raw API Usage](https://github.com/run-llama/llama_cloud_services/blob/main/examples/parse/demo_api.ipynb)
## Resources
[Section titled “Resources”](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/#resources)
  * See [Credit Pricing & Usage](https://developers.llamaindex.ai/python/cloud/general/pricing)
  * Next steps? Check out [LlamaExtract](https://developers.llamaindex.ai/python/cloud/llamaextract/getting_started) to extract structured data from unstructured documents!


