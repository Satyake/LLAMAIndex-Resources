[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#_top)
# Tables as Spreadsheet Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Tables as spreadsheet options allow you to configure how tables are exported as spreadsheet files during parsing.
## How It Works
[Section titled “How It Works”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#how-it-works)
When enabled, this feature extracts tables from documents and exports them as spreadsheet files (Excel format), making it easier to work with tabular data in spreadsheet applications.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#available-options)
### Enable Tables as Spreadsheet
[Section titled “Enable Tables as Spreadsheet”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#enable-tables-as-spreadsheet)
Enable or disable the tables as spreadsheet export feature.
```



"output_options": {




"tables_as_spreadsheet": {




"enable": true





```

### Automatic Sheet Naming
[Section titled “Automatic Sheet Naming”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#automatic-sheet-naming)
Sheet names are automatically guessed based on table content and context. This feature is always enabled in v2.
## Use Cases
[Section titled “Use Cases”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#use-cases)
  * **Data Analysis** : Export tables for further analysis in Excel or other spreadsheet tools
  * **Data Migration** : Extract tabular data from PDFs for database imports
  * **Financial Reports** : Convert financial tables to spreadsheet format for calculations
  * **Research Data** : Extract datasets from academic papers or reports


## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#complete-api-request-example)


### Parse the Document with PDF Export Enabled
[Section titled “Parse the Document with PDF Export Enabled”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#parse-the-document-with-pdf-export-enabled)
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




"output_options": {




"tables_as_spreadsheet": {




"enable": true





```

### Retrieving the XLSX File
[Section titled “Retrieving the XLSX File”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/tables_as_spreadsheet/#retrieving-the-xlsx-file)
After parsing completes, retrieve the XLSX file using the `xlsx_content_metadata` expand parameter. This returns a presigned URL for direct download:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse/{job_id}?expand=xlsx_content_metadata'\




-H'Accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

The response includes metadata with a presigned URL:
```



"job": { ... },




"result_content_metadata": {




"xlsx": {




"size_bytes": 15234,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/..."





```

Use the `presigned_url` to download the XLSX file directly. The URL is temporary and valid for a limited time.
```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic_plus",




version="latest",




output_options={




"tables_as_spreadsheet": {




"enable": True






expand=["xlsx_content_metadata"]






for output_type in result.result_content_metadata.keys():




print(f"Output Type: {output_type}, Presigned URL: {result.result_content_metadata[output_type].presigned_url}")


```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.pdf'),




tier: "agentic_plus",




version: "latest",




output_options: {




tables_as_spreadsheet: {




enable: true






expand: ["xlsx_content_metadata"]






for (const outputTypein result.result_content_metadata!) {




const contentMetadataresult.result_content_metadata![outputType];




console.log(`Output Type: ${outputType}, Presigned URL: ${contentMetadata.presigned_url}`);



```

