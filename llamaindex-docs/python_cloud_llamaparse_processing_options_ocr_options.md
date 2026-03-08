[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ocr_options/#_top)
# OCR Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
OCR options allow you to configure optical character recognition settings for processing images within documents. These options are available for all tiers.
## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ocr_options/#configuration)
Use `processing_options.ocr_parameters` to configure these options.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ocr_options/#available-options)
### Languages
[Section titled “Languages”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ocr_options/#languages)
Specify which languages to use for OCR processing of images. This only affects text extracted from images, not native text in the document.
```



"tier": "agentic",




"version": "latest",




"processing_options": {




"ocr_parameters": {




"languages": ["en", "zh", "ja"]





```

## Examples
[Section titled “Examples”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ocr_options/#examples)
### Single Language
[Section titled “Single Language”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ocr_options/#single-language)
```



"tier": "fast",




"version": "latest",




"processing_options": {




"ocr_parameters": {




"languages": ["en"]





```

### Multiple Languages
[Section titled “Multiple Languages”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ocr_options/#multiple-languages)
```



"tier": "agentic_plus",




"version": "latest",




"processing_options": {




"ocr_parameters": {




"languages": ["en", "fr", "de", "es"]





```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ocr_options/#complete-api-request-example)


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




"processing_options": {




"ocr_parameters": {




"languages": ["en", "es"]





```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic",




version="latest",




processing_options={




"ocr_parameters": {




"languages": ["en", "es"]





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




processing_options: {




ocr_parameters: {




languages: ["en", "es"]





```

