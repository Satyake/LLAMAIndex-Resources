[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/custom_prompt/#_top)
# Custom Prompt
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
The custom prompt option allows you to provide custom instructions for AI-powered parsing. This option is only available for agentic tiers (`cost_effective`, `agentic`, and `agentic_plus`).
## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/custom_prompt/#configuration)
Use `agentic_options.custom_prompt` to configure this option.
## Usage
[Section titled “Usage”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/custom_prompt/#usage)
Provide a custom prompt to guide the AI model during parsing:
```



"tier": "agentic",




"version": "latest",




"agentic_options": {




"custom_prompt": "Extract all financial data and format tables with currency symbols."




```

## Examples
[Section titled “Examples”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/custom_prompt/#examples)
### Document-Specific Instructions
[Section titled “Document-Specific Instructions”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/custom_prompt/#document-specific-instructions)
```



"tier": "agentic_plus",




"version": "latest",




"agentic_options": {




"custom_prompt": "This is a legal contract. Pay special attention to dates, parties involved, and monetary amounts."




```

### Formatting Instructions
[Section titled “Formatting Instructions”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/custom_prompt/#formatting-instructions)
```



"tier": "cost_effective",




"version": "latest",




"agentic_options": {




"custom_prompt": "Format all headings consistently and preserve the original document hierarchy."




```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/custom_prompt/#complete-api-request-example)


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




"agentic_options": {




"custom_prompt": "Extract all tables and ensure numerical data is properly formatted."




```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic_plus",




version="latest",




agentic_options={




"custom_prompt": "Extract all tables and ensure numerical data is properly formatted."





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




agentic_options: {




custom_prompt: "Extract all tables and ensure numerical data is properly formatted."





expand: ["markdown"],



```

> **Note** : This option is not available for the `fast` tier, which does not use AI models.
