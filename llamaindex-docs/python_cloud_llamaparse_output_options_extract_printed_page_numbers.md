[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/extract_printed_page_numbers/#_top)
# Extract Printed Page Numbers
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Extract printed page numbers allows you to configure whether page numbers that are printed on the document pages are extracted and included in the parsed content.
## How It Works
[Section titled “How It Works”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/extract_printed_page_numbers/#how-it-works)
When enabled, this feature identifies and extracts page numbers that are visually printed on the document pages (such as “Page 1 of 10” or ”- 5 -”), making them available in the parsed output.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/extract_printed_page_numbers/#available-options)
### Enable Extraction
[Section titled “Enable Extraction”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/extract_printed_page_numbers/#enable-extraction)
Enable extraction of printed page numbers from document pages.
```



"output_options": {




"extract_printed_page_number": true




```

### Disable Extraction
[Section titled “Disable Extraction”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/extract_printed_page_numbers/#disable-extraction)
Set to `false` to skip extraction of printed page numbers.
```



"output_options": {




"extract_printed_page_number": false




```

## Use Cases
[Section titled “Use Cases”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/extract_printed_page_numbers/#use-cases)
  * **Document Indexing** : Preserve original page numbering for reference
  * **Academic Papers** : Maintain citation-friendly page numbers
  * **Legal Documents** : Preserve official page numbering
  * **Report Processing** : Keep original pagination for cross-references


## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/extract_printed_page_numbers/#complete-api-request-example)


Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v2/parse'\




-H'Accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--data'{




"file_id": "<file_id>",




"tier": "agentic",




"version": "latest",




"output_options": {




"extract_printed_page_number": true




```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic",




version="latest",




output_options={




"extract_printed_page_number": True




```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.pdf'),




tier: "agentic",




version: "latest",




output_options: {




extract_printed_page_number: true




```

