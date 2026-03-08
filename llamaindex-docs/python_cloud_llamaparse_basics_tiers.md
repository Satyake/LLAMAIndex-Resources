[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#_top)
# Tiers
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
LlamaParse offers four different tiers designed to meet various parsing needs, balancing cost and accuracy.
## Versioning and Requirements
[Section titled “Versioning and Requirements”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#versioning-and-requirements)
### Tier Versioning
[Section titled “Tier Versioning”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#tier-versioning)
Tiers in LlamaParse v2 are **versioned** to ensure consistent and predictable behavior. When you specify a tier with a specific version like `"agentic"` with `version="2025-11-18"`, the parsing behavior will never change - you’ll always get the same model, prompts, and configuration.
This versioning system allows us to introduce new models, update prompts, and add new options in newer versions without breaking existing integrations or changing behavior for previous versions.
### Mandatory Tier Selection
[Section titled “Mandatory Tier Selection”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#mandatory-tier-selection)
Unlike LlamaParse v1, **specifying a tier is mandatory** when parsing files in v2. You must include both the `tier` and `version` parameters in your parsing request.
Use `"version": "latest"` to always get the most recent version. For production use, we recommend using specific version dates (e.g., `"2026-01-08"`, `"2025-12-31"`, `"2025-12-18"`, `"2025-12-11"`) to ensure consistent results.
## Available Tiers
[Section titled “Available Tiers”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#available-tiers)
The following tier configurations should be included at the root level of your API request. For complete API request examples, see the [Getting Started guide](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/).
### Agentic Plus
[Section titled “Agentic Plus”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#agentic-plus)
The most advanced tier with state-of-the-art models for maximum accuracy.
```



"tier": "agentic_plus",




"version": "latest"



```

With explicit version for reproducibility:
```



"tier": "agentic_plus",




"version": "2026-01-08"



```

### Agentic
[Section titled “Agentic”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#agentic)
Advanced parsing with intelligent agents for complex documents.
```



"tier": "agentic",




"version": "latest"



```

### Cost Effective
[Section titled “Cost Effective”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#cost-effective)
Balanced performance and cost using efficient models.
```



"tier": "cost_effective",




"version": "latest"



```

### Fast
[Section titled “Fast”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#fast)
The fastest tier with basic parsing capabilities.
```



"tier": "fast",




"version": "latest"



```

## Example API Request
[Section titled “Example API Request”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/tiers/#example-api-request)
Here’s a complete example of how to use a tier in an API request:


Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v2/parse'\




-H'Accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--data'{




"file_id": "<file_id>",




"tier": "agentic_plus",




"version": "latest"



```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic_plus",




version="latest"



```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.pdf'),




tier: "agentic_plus",




version: "latest"



```

