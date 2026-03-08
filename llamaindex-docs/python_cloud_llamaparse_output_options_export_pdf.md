[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/export_pdf/#_top)
# Retrieving Exported PDF
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
A PDF version of each document is generated during parsing.
You can request a presigned url to retrieve the generated PDF after parsing completes.
## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/export_pdf/#complete-api-request-example)


### Parse the Document
[Section titled “Parse the Document”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/export_pdf/#parse-the-document)
Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v2/parse'\




-H'Accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--data'{




"file_id": "<file_id>",




"tier": "agentic_plus",




"version": "latest",



```

### Retrieving the Exported PDF
[Section titled “Retrieving the Exported PDF”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/export_pdf/#retrieving-the-exported-pdf)
After parsing completes, retrieve the exported PDF using the `output_pdf_content_metadata` expand parameter. This returns a presigned URL for direct download:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse/{job_id}?expand=output_pdf_content_metadata'\




-H'Accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

The response includes metadata with a presigned URL:
```



"job": { ... },




"result_content_metadata": {




"outputPDF": {




"size_bytes": 102400,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/..."





```

Use the `presigned_url` to download the PDF file directly. The URL is temporary and valid for a limited time.
```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.docx",




tier="agentic_plus",




expand=["output_pdf_content_metadata"],





# Returns a presigned URL to download the exported PDF



print(result.result_content_metadata['outputPDF'].presigned_url)


```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.docx'),




tier: "agentic_plus",




version: "latest",




expand: ["output_pdf_content_metadata"],





// Returns a presigned URL to download the exported PDF



console.log(result.result_content_metadata!.outputPDF!.presigned_url);


```

