[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/spreadsheet_options/#_top)
# Spreadsheet Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Spreadsheet options allow you to configure how Excel, CSV, and other spreadsheet formats are processed during parsing.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/spreadsheet_options/#available-options)
### Detect Sub-Tables
[Section titled “Detect Sub-Tables”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/spreadsheet_options/#detect-sub-tables)
Find and extract sub-tables within spreadsheet cells. This is useful for spreadsheets that contain multiple logical tables within a single sheet.
```



"input_options": {




"spreadsheet": {




"detect_sub_tables_in_sheets": true





```

### Force Formula Computation
[Section titled “Force Formula Computation”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/spreadsheet_options/#force-formula-computation)
Re-compute spreadsheet cells containing formulas instead of using cached values. This ensures you get the most up-to-date calculated results.
```



"input_options": {




"spreadsheet": {




"force_formula_computation_in_sheets": true





```

> **Performance Note** : Enabling formula computation may impact performance for spreadsheets containing many formulas, as each formula needs to be re-evaluated.
## Combined Configuration
[Section titled “Combined Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/spreadsheet_options/#combined-configuration)
You can combine multiple spreadsheet options:
```



"input_options": {




"spreadsheet": {




"detect_sub_tables_in_sheets": true,




"force_formula_computation_in_sheets": true





```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/spreadsheet_options/#complete-api-request-example)


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




"input_options": {




"spreadsheet": {




"detect_sub_tables_in_sheets": true,




"force_formula_computation_in_sheets": true





```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.xlsx",




tier="agentic_plus",




expand=["markdown"],




input_options={




"spreadsheet": {




"detect_sub_tables_in_sheets": True,




"force_formula_computation_in_sheets": True





```

```


import fs from"fs";




import { LlamaCloud } from"llama_cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




uploadFile: fs.createReadStream("example_file.xlsx"),




tier: "agentic_plus",




expand: ["markdown"],




input_options: {




spreadsheet: {




detectSubTablesInSheets: true,




forceFormulaComputationInSheets: true,





```

