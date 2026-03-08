[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#_top)
# Screenshots Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Screenshots options allow you to configure whether page screenshots are generated during document parsing.
## How It Works
[Section titled “How It Works”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#how-it-works)
When enabled, this feature takes a screenshot of each page in the document, providing a visual representation of the original page layout alongside the extracted text content.
## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#configuration)
In v2, screenshot generation is controlled via the `images_to_save` array. Include `"screenshot"` in the array to enable screenshot generation.
### Enable Screenshots
[Section titled “Enable Screenshots”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#enable-screenshots)
Enable screenshot generation for each page of the document:
```



"output_options": {




"images_to_save": ["screenshot"]




```

### Combine with Other Image Types
[Section titled “Combine with Other Image Types”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#combine-with-other-image-types)
You can combine screenshots with other image types:
```



"output_options": {




"images_to_save": ["screenshot", "embedded", "layout"]




```

### Disable Screenshots
[Section titled “Disable Screenshots”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#disable-screenshots)
To disable screenshots, simply omit `"screenshot"` from the array, or use an empty array to disable all image saving:
```



"output_options": {




"images_to_save": []




```

> **Note** : If `images_to_save` is not specified, no images (including screenshots) are saved by default.
## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#complete-api-request-example)


### Parse the Document with Screenshot Generation Enabled
[Section titled “Parse the Document with Screenshot Generation Enabled”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#parse-the-document-with-screenshot-generation-enabled)
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




"output_options": {




"images_to_save": ["screenshot"]




```

### Retrieving Screenshots
[Section titled “Retrieving Screenshots”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/screenshots/#retrieving-screenshots)
After parsing completes, retrieve screenshot metadata using the `images_content_metadata` expand parameter. This returns presigned URLs for direct download:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse/{job_id}?expand=images_content_metadata'\




-H'Accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

The response includes metadata with presigned URLs:
```



"job": { ... },




"images_content_metadata": {




"total_count": 5,




"images": [





"filename": "screenshot_page_0.png",




"content_type": "image/png",




"size_bytes": 45678,




"presigned_url": "https://s3.amazonaws.com/..."






"filename": "screenshot_page_1.png",




"content_type": "image/png",




"size_bytes": 52341,




"presigned_url": "https://s3.amazonaws.com/..."






```

Use the `presigned_url` for each image to download the screenshots directly. URLs are temporary and valid for a limited time.
```


import httpx




from llama_cloud import LlamaCloud






client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")




# Upload and parse a document, requdesting image content metadata



result =await client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic",




version="latest",




output_options={




"screenshots": {"enable": True},





expand=["images_content_metadata"],





# Download extracted images using presigned URLs



for image in result.images_content_metadata.images:




print(f"Downloading {image.filename}, {image.size_bytes} bytes")




withopen(f"{image.filename}","wb") as img_file:




with httpx.Client() as http_client:




response = http_client.get(image.presigned_url)




img_file.write(response.content)


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




expand: ["images_content_metadata"],




output_options: {




screenshots: {




enable: true








for (const imageof result.images_content_metadata!.images) {




console.log(`Downloading ${image.filename}, ${image.size_bytes} bytes`);




const response = await fetch(image.presigned_url);




const arrayBuffer = await response.arrayBuffer();




fs.writeFileSync(image.filename, Buffer.from(arrayBuffer));



```

