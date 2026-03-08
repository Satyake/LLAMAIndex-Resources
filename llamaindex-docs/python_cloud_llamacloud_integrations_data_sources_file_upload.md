[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/file_upload/#_top)
# File Upload Data Source
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Directly upload files
## Configure via UI
[Section titled “Configure via UI”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/file_upload/#configure-via-ui)
## Configure via API / Client
[Section titled “Configure via API / Client”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/file_upload/#configure-via-api--client)
```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





file_obj = client.files.create(file="path/to/your/file.txt",purpose="general")


```

```typescript import fs from "fs"; import { LlamaCloud } from "@llamaindex/llama-cloud"; 
```

const client = new LlamaCloud({



apiKey: "LLAMA_CLOUD_API_KEY",



});



const fileObj = await client.files.create({



file: fs.createReadStream('path/to/your/file.txt'),




purpose: 'general',



});


```

```

```python file_obj = client.files.upload(upload_file="path/to/your/file.txt") ```  ```typescript const fileObj = await client.files.upload({ upload_file: "path/to/your/file.txt", }); ```  ``` # Step 1: Generate a presigned URL for file upload curl -X POST "https://api.cloud.llamaindex.ai/api/v1/files/presigned-url" \ -H "Content-Type: application/json" \ -H "Authorization: Bearer $LLAMA_CLOUD_API_KEY" \ -d '{ "name": "example.txt" }' 
```

# Step 2: Use the presigned URL to upload the file to S3 within 30 seconds


curl -X PUT "https://your-presigned-url-from-step-1" \



-H "Content-Type: text/plain" \




-F 'file=@path/to/your/example.txt'




# Step 3: Confirm the file upload with LlamaCloud


curl -X PUT "https://api.cloud.llamaindex.ai/api/v1/files/sync" \



-H "Content-Type: application/json" \




-H "Authorization: Bearer $LLAMA_CLOUD_API_KEY"



```

```

