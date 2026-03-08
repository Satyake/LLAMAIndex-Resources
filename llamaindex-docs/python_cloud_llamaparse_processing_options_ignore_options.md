[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ignore_options/#_top)
# Ignore Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Ignore options allow you to skip specific types of text during parsing. These options are available for all tiers.
## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ignore_options/#configuration)
Use `processing_options.ignore` to configure these options.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ignore_options/#available-options)
### Ignore Diagonal Text
[Section titled “Ignore Diagonal Text”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ignore_options/#ignore-diagonal-text)
Skip text that appears diagonally on the page.
```



"tier": "agentic",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_diagonal_text": true





```

### Ignore Text in Images
[Section titled “Ignore Text in Images”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ignore_options/#ignore-text-in-images)
Skip OCR processing of text that appears within images.
```



"tier": "fast",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_text_in_image": true





```

### Ignore Hidden Text
[Section titled “Ignore Hidden Text”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ignore_options/#ignore-hidden-text)
Skip text that is hidden in the document (such as white text on white background or text marked as hidden).
```



"tier": "agentic_plus",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_hidden_text": true





```

## Combined Configuration
[Section titled “Combined Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ignore_options/#combined-configuration)
You can combine multiple ignore options:
```



"tier": "agentic_plus",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_diagonal_text": true,




"ignore_hidden_text": true,




"ignore_text_in_image": true





```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/ignore_options/#complete-api-request-example)


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




"ignore": {




"ignore_diagonal_text": true,




"ignore_hidden_text": true





```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic",




version="latest",




processing_options={




"ignore": {




"ignore_diagonal_text": True,




"ignore_hidden_text": True






expand=["markdown"],



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




ignore: {




ignore_diagonal_text: true,




ignore_hidden_text: true,






expand: ["markdown"],



```

