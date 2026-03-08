[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/specialized_chart_parsing/#_top)
# Specialized Chart Parsing
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Specialized chart parsing enables enhanced extraction of charts and graphs from documents using AI-powered analysis.
Note that any specialized chart parsing mode can be used with any of the `agentic_plus`, `agentic`, and `cost_effective` tiers.
## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/specialized_chart_parsing/#configuration)
Use `processing_options.specialized_chart_parsing` to enable this feature.
## Available Modes
[Section titled “Available Modes”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/specialized_chart_parsing/#available-modes)
Mode | Description  
---|---  
`agentic_plus` | Enhanced agentic mode with additional processing for complex charts  
`agentic` | Uses AI agents to analyze and extract chart data with high accuracy  
`efficient` | Faster processing with good accuracy for simpler charts  
## Examples
[Section titled “Examples”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/specialized_chart_parsing/#examples)
### Agentic Plus Mode
[Section titled “Agentic Plus Mode”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/specialized_chart_parsing/#agentic-plus-mode)
Maximum accuracy for the most complex charts:
```



"tier": "agentic_plus",




"version": "latest",




"processing_options": {




"specialized_chart_parsing": "agentic_plus"




```

### Agentic Mode
[Section titled “Agentic Mode”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/specialized_chart_parsing/#agentic-mode)
Best for complex charts requiring detailed analysis:
```



"tier": "agentic",




"version": "latest",




"processing_options": {




"specialized_chart_parsing": "agentic"




```

### Efficient Mode
[Section titled “Efficient Mode”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/specialized_chart_parsing/#efficient-mode)
Good balance between speed and accuracy:
```



"tier": "cost_effective",




"version": "latest",




"processing_options": {




"specialized_chart_parsing": "efficient"




```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/specialized_chart_parsing/#complete-api-request-example)
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




"specialized_chart_parsing": "agentic_plus"




```

