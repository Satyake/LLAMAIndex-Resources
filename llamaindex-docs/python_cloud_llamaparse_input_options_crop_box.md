[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/crop_box/#_top)
# Crop Box
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
The crop box parameter allows you to define a specific rectangular area of each page to parse, effectively cropping out unwanted content from the margins.
## How It Works
[Section titled “How It Works”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/crop_box/#how-it-works)
The crop box is defined using four ratio values (between 0.0 and 1.0) that represent the boundaries of the area to parse:
  * **top** : Distance from the top edge as a ratio of page height
  * **right** : Distance from the right edge as a ratio of page width
  * **bottom** : Distance from the bottom edge as a ratio of page height
  * **left** : Distance from the left edge as a ratio of page width


The crop box applies to every page in the document.
## Common Use Cases
[Section titled “Common Use Cases”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/crop_box/#common-use-cases)
  * **Remove headers and footers** : Crop out repetitive page headers and footers
  * **Focus on main content** : Extract only the central content area of a document
  * **Remove margin text** : Exclude annotations, page numbers, or watermarks in margins


## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/crop_box/#configuration)
The crop box should be included at the root level of your parsing request:
```



"crop_box": {




"top": 0.1,




"right": 0.05,




"bottom": 0.15,




"left": 0.05




```

## Examples
[Section titled “Examples”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/crop_box/#examples)
### Remove Headers and Footers
[Section titled “Remove Headers and Footers”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/crop_box/#remove-headers-and-footers)
Exclude the top 10% and bottom 15% of each page:
```



"crop_box": {




"top": 0.1,




"bottom": 0.15




```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/crop_box/#complete-api-request-example)


Terminal window```


curl-X'POST'




'https://api.cloud.llamaindex.ai/api/v2/parse'\




-H'Accept: application/json'




-H'Content-Type: application/json'




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"




--data'{




"file_id": "<file_id>",




"tier": "agentic",




"version": "latest",




"crop_box": {




"top": 50,




"bottom": 50,




"left": 25,




"right": 25




```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic",




version="latest",




expand=["markdown"],




crop_box={




"top": 0.1,




"bottom": 0.15,




"left": 0.05,




"right": 0.05




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




expand: ["markdown"],




crop_box: {




top: 0.1,




bottom: 0.15,




left: 0.05,




right: 0.05




```

