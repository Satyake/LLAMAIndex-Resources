[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/presentation_options/#_top)
# Presentation Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Presentation options allow you to configure how PowerPoint and other presentation formats are processed during parsing.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/presentation_options/#available-options)
### Out of Bounds Content
[Section titled “Out of Bounds Content”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/presentation_options/#out-of-bounds-content)
Extract content that extends beyond the visible slide boundaries. This captures text, images, and other elements that may be positioned outside the standard slide area.
```



"input_options": {




"presentation": {




"out_of_bounds_content": true





```

### Skip Embedded Data
[Section titled “Skip Embedded Data”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/presentation_options/#skip-embedded-data)
Skip extraction of embedded data for charts in presentation slides. This can improve performance when you don’t need the underlying chart data.
```



"input_options": {




"presentation": {




"skip_embedded_data": true





```

## Combined Configuration
[Section titled “Combined Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/presentation_options/#combined-configuration)
You can combine multiple presentation options:
```



"input_options": {




"presentation": {




"out_of_bounds_content": true,




"skip_embedded_data": false





```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/presentation_options/#complete-api-request-example)


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




"input_options": {




"presentation": {




"out_of_bounds_content": true





```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pptx",




tier="agentic",




version="latest",




expand=["markdown"],




input_options={




"presentation": {




"out_of_bounds_content": True





```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.pptx'),




tier: "agentic",




version: "latest",




expand: ["markdown"],




input_options: {




presentation: {




out_of_bounds_content: true





```

