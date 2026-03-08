[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#_top)
# Table Extraction
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Table extraction options allow you to configure how tables are detected and extracted from documents. These options are available for all tiers.
## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#configuration)
Use `processing_options` to configure these options.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#available-options)
### Aggressive Table Extraction
[Section titled “Aggressive Table Extraction”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#aggressive-table-extraction)
Enable more aggressive table detection and extraction methods. This may capture more tables but could also introduce false positives.
```



"tier": "agentic",




"version": "latest",




"processing_options": {




"aggressive_table_extraction": true




```

### Disable Heuristics
[Section titled “Disable Heuristics”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#disable-heuristics)
Disable table-related heuristics including outlined table extraction and adaptive long table handling. Use this when the default heuristics are producing unwanted results.
```



"tier": "agentic",




"version": "latest",




"processing_options": {




"disable_heuristics": true




```

When enabled, this disables:
  * **Outlined table extraction** : Detection of tables with visible borders
  * **Adaptive long table handling** : Special handling for long tables


## Examples
[Section titled “Examples”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#examples)
### Fast Tier
[Section titled “Fast Tier”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#fast-tier)
```



"tier": "fast",




"version": "latest",




"processing_options": {




"aggressive_table_extraction": true




```

### Agentic Tier
[Section titled “Agentic Tier”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#agentic-tier)
```



"tier": "agentic_plus",




"version": "latest",




"processing_options": {




"aggressive_table_extraction": true




```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/table_extraction/#complete-api-request-example)


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




"processing_options": {




"aggressive_table_extraction": true




```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic_plus",




version="latest",




processing_options={




"aggressive_table_extraction": True





expand=["markdown"],



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




processing_options: {




aggressive_table_extraction: true





expand: ["markdown"],



```

