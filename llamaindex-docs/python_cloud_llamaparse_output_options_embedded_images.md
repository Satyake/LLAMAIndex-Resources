[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/embedded_images/#_top)
# Embedded Images Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Embedded images options allow you to configure whether images found within documents are extracted and made available as separate files.
## How It Works
[Section titled “How It Works”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/embedded_images/#how-it-works)
When enabled, this feature extracts images that are embedded within the document (such as charts, diagrams, photos, or illustrations) and makes them available as separate image files alongside the parsed text content.
## Configuration
[Section titled “Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/embedded_images/#configuration)
In v2, embedded image extraction is controlled via the `images_to_save` array. Include `"embedded"` in the array to enable extraction of embedded images.
### Enable Embedded Images Extraction
[Section titled “Enable Embedded Images Extraction”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/embedded_images/#enable-embedded-images-extraction)
Enable extraction of embedded images from documents:
```



"output_options": {




"images_to_save": ["embedded"]




```

### Combine with Other Image Types
[Section titled “Combine with Other Image Types”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/embedded_images/#combine-with-other-image-types)
You can combine embedded images with other image types:
```



"output_options": {




"images_to_save": ["screenshot", "embedded", "layout"]




```

Available image categories:
  * `"screenshot"` - Full page screenshots
  * `"embedded"` - Images embedded within the document
  * `"layout"` - Cropped images from layout detection


> **Note** : If `images_to_save` is not specified, no images (including embedded images) are saved by default.
## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/embedded_images/#complete-api-request-example)


### Parse the Document with Embedded Images Extraction Enabled
[Section titled “Parse the Document with Embedded Images Extraction Enabled”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/embedded_images/#parse-the-document-with-embedded-images-extraction-enabled)
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




"output_options": {




"images_to_save": ["embedded"]




```

### Retrieving Embedded Images
[Section titled “Retrieving Embedded Images”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/embedded_images/#retrieving-embedded-images)
After parsing completes, retrieve image metadata using the `images_content_metadata` expand parameter. This returns presigned URLs for direct download:
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




"total_count": 3,




"images": [





"filename": "image_0.png",




"content_type": "image/png",




"size_bytes": 12345,




"presigned_url": "https://s3.amazonaws.com/..."






"filename": "image_1.jpg",




"content_type": "image/jpeg",




"size_bytes": 23456,




"presigned_url": "https://s3.amazonaws.com/..."






```

You can also filter to specific image filenames:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse/{job_id}?expand=images_content_metadata&image_filenames=image_0.png,image_1.jpg'\




-H'Accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

Use the `presigned_url` for each image to download directly. URLs are temporary and valid for a limited time.
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




"embedded_images": {"enable": True},





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




embedded_images: {




enable: true








for (const imageof result.images_content_metadata!.images) {




console.log(`Downloading ${image.filename}, ${image.size_bytes} bytes`);




const response = await fetch(image.presigned_url);




const arrayBuffer = await response.arrayBuffer();




fs.writeFileSync(image.filename, Buffer.from(arrayBuffer));



```

