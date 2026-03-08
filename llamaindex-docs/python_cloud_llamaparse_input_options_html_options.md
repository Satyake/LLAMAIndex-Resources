[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/html_options/#_top)
# HTML Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
HTML options allow you to configure how web pages and HTML documents are processed during parsing.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/html_options/#available-options)
### Make All Elements Visible
[Section titled “Make All Elements Visible”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/html_options/#make-all-elements-visible)
Force hidden elements to be visible during parsing. This ensures that content hidden by CSS or JavaScript is still extracted.
```



"input_options": {




"html": {




"make_all_elements_visible": true





```

### Remove Navigation Elements
[Section titled “Remove Navigation Elements”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/html_options/#remove-navigation-elements)
Remove navigation menus, breadcrumbs, and similar navigational elements that typically don’t contain the main content.
```



"input_options": {




"html": {




"remove_navigation_elements": true





```

### Remove Fixed Elements
[Section titled “Remove Fixed Elements”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/html_options/#remove-fixed-elements)
Remove fixed-position elements like sticky headers, sidebars, and floating elements that may interfere with content extraction.
```



"input_options": {




"html": {




"remove_fixed_elements": true





```

## Combined Configuration
[Section titled “Combined Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/html_options/#combined-configuration)
You can combine multiple HTML options:
```



"input_options": {




"html": {




"make_all_elements_visible": true,




"remove_navigation_elements": true,




"remove_fixed_elements": true





```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/html_options/#complete-api-request-example)


Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v2/parse'\




-H'Accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--data'{




"file_id": "<file_id>",




"tier": "cost_effective",




"version": "latest",




"input_options": {




"html": {




"make_all_elements_visible": true,




"remove_navigation_elements": true





```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.html",




tier="cost_effective",




version="latest",




expand=["markdown"],




input_options={




"html": {




"make_all_elements_visible": True,




"remove_navigation_elements": True





```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.html'),




tier: "cost_effective",




version: "latest",




expand: ["markdown"],




input_options: {




html: {




make_all_elements_visible: true,




remove_navigation_elements: true





```

