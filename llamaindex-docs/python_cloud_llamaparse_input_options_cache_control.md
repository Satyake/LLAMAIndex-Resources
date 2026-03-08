[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/cache_control/#_top)
# Cache Control
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Cache control allows you to configure caching behavior for parsing operations, controlling whether results are cached and whether existing cache should be invalidated.
## How It Works
[Section titled “How It Works”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/cache_control/#how-it-works)
By default, LlamaParse caches parsing results to improve performance on repeated requests. Cache control allows you to disable this caching when you need fresh results or want to ensure no cached data is used.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/cache_control/#available-options)
### Disable Cache
[Section titled “Disable Cache”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/cache_control/#disable-cache)
Disable caching for the current parsing request. This both prevents caching of new results and invalidates any existing cache.
```



"disable_cache": true



```

### Enable Cache (Default)
[Section titled “Enable Cache (Default)”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/cache_control/#enable-cache-default)
Allow normal caching behavior. This is the default setting when the parameter is not specified.
```



"disable_cache": false



```

## Use Cases
[Section titled “Use Cases”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/cache_control/#use-cases)
  * **Fresh Results** : Ensure LlamaParse processes the document anew each time
  * **Testing** : Get consistent results during development and testing
  * **Performance Testing** : Measure parsing performance without cache influence
  * **Debugging** : Isolate parsing issues by eliminating cached results


## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/input_options/cache_control/#complete-api-request-example)


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




"disable_cache": true



```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic",




version="latest",




expand=["markdown"],




disable_cache=True



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




disable_cache: true



```

