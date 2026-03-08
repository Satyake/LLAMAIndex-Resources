[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#_top)
# Page Ranges
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
The page ranges parameter allows you to control which pages of a document are processed, enabling selective parsing for efficiency or targeted content extraction.
## How It Works
[Section titled “How It Works”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#how-it-works)
Page ranges can be configured in two ways:
  * **max_pages** : Limit the total number of pages to process (starting from page 1)
  * **target_pages** : Specify exact pages or ranges using 1-based indexing


Both options use **1-based page numbering** (unlike v1 which used 0-based indexing), meaning the first page is page 1.
## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#configuration)
The page ranges should be included at the root level of your parsing request:
```



"page_ranges": {




"max_pages": 10,




"target_pages": "1,3,5-10"




```

## Examples
[Section titled “Examples”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#examples)
### Process First 5 Pages Only
[Section titled “Process First 5 Pages Only”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#process-first-5-pages-only)
Limit processing to the first 5 pages of the document:
```



"page_ranges": {




"max_pages": 5




```

### Process Specific Pages
[Section titled “Process Specific Pages”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#process-specific-pages)
Parse only pages 1, 3, and pages 7 through 12:
```



"page_ranges": {




"target_pages": "1,3,7-12"




```

### Process Single Page
[Section titled “Process Single Page”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#process-single-page)
Parse only the first page:
```



"page_ranges": {




"target_pages": "1"




```

### Process Page Ranges
[Section titled “Process Page Ranges”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#process-page-ranges)
Parse pages 5-10 and page 15:
```



"page_ranges": {




"target_pages": "5-10,15"




```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/page_ranges/#complete-api-request-example)


Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v2/parse'\




-H'Accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--data'{




"file_id": "<file_id>",




"tier": "cost_effective",




"version": "latest",




"page_ranges": {




"target_pages": "1-5,10,15-20"




```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="cost_effective",




version="latest",




expand=["markdown"],




page_ranges={




"target_pages": "1-5,10,15-20"




```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.pdf'),




tier: "cost_effective",




version: "latest",




expand: ["markdown"],




page_ranges: {




target_pages: "1-5,10,15-20"




```

