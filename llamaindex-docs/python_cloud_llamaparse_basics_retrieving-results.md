[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#_top)
# Retrieving Results
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
After submitting a parse job, you retrieve results using the `expand` parameter to control what data is included in the response. This guide explains how to use the `expand` parameter effectively.
## The Expand Parameter
[Section titled “The Expand Parameter”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#the-expand-parameter)
The `expand` query parameter controls which result fields are included in the API response when retrieving parse job results. By default, only job metadata (status, ID, error messages) is returned. Use `expand` to include parsed content or download URLs.


You can run an entire job end-to-end and expand as needed:
```

# pip install llama-cloud>=1.0



from llama_cloud import LlamaCloud, AsyncLlamaCloud





client =LlamaCloud(api_key="YOUR_LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="doc.pdf",




tier="cost_effective",




version="latest",




expand=["markdown_full"]






print(result.job.status)




print(result.markdown_full)




# Use the job ID to expand as needed



text_result = client.parsing.get(




job_id=result.job.id,




expand=["text_full"]





print(text_result.text_full)


```

You can run an entire job end-to-end and expand as needed:
```

// npm install @llamaindex/llama-cloud@



import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({apiKey: "YOUR_LLAMA_CLOUD_API_KEY"});




// Upload and parse a document with expansion



const result = await client.parsing.parse({




upload_file: fs.createReadStream("doc.pdf"),




tier: "cost_effective",




version: "latest",




expand: ["markdown_full"],





console.log(result.job.status);




console.log(result.markdown_full);




// Use the job ID to expand as needed



const textResult = await client.parsing.get({




job_id: result.job.id,




expand: ["text_full"],





console.log(textResult.text_full);


```

## Content Fields vs. Metadata Fields
[Section titled “Content Fields vs. Metadata Fields”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#content-fields-vs-metadata-fields)
There are two types of expand values: **content fields** and **metadata fields**.
### Content Fields
[Section titled “Content Fields”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#content-fields)
Content fields return the **actual parsed data** directly in the API response. Use these when you need immediate access to the parsed content.
Field | Description | Best For  
---|---|---  
`text` | Plain text extraction from the document per page | Simple text analysis, search indexing  
`markdown` | Markdown-formatted content with structure per page | Display, documentation, LLM prompts  
`items` | Structured JSON with typed elements (tables, headings, etc.) per page | Programmatic processing, data extraction  
`metadata` | Page-level metadata (confidence scores, speaker notes, etc.) | Quality assessment, presentation data  
`markdown_full` | Full raw markdown file content (output.md) | Complete markdown output without pagination  
`text_full` | Full plain text file content | Complete text output without pagination  
**Example response with content:**
```



"job": {




"id": "pjb-123",




"status": "COMPLETED"





"text": {




"pages": [





"page_number": 1,




"text": "This is the extracted text from page 1..."







"markdown": {




"pages": [





"page_number": 1,




"markdown": "# Heading\n\nThis is markdown content..."






```

### Metadata Fields
[Section titled “Metadata Fields”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#metadata-fields)
Metadata fields return **presigned download URLs** instead of the actual content. Use these when you want to download large files or defer processing.
Field | Description | Download Format  
---|---|---  
`text_content_metadata` | Download URL for plain text file | .txt file  
`markdown_content_metadata` | Download URL for markdown file | .md file  
`items_content_metadata` | Download URL for structured JSON | .json file  
`metadata_content_metadata` | Download URL for metadata file | .json file  
`xlsx_content_metadata` | Download URL for spreadsheet export | .xlsx file  
`output_pdf_content_metadata` | Download URL for output PDF | .pdf file  
`images_content_metadata` | List of download URLs for extracted images | .png, .jpg files  
`markdown_full_content_metadata` | Download URL for full raw markdown | .md file  
`text_full_content_metadata` | Download URL for full plain text | .txt file  
**Example response with metadata:**
```



"job": {




"id": "pjb-123",




"status": "COMPLETED"





"result_content_metadata": {




"md": {




"size_bytes": 45678,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/bucket/path/output.md?signature=..."





"fullText": {




"size_bytes": 23456,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/bucket/path/output.txt?signature=..."





```

### Images Content Metadata
[Section titled “Images Content Metadata”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#images-content-metadata)
The `images_content_metadata` field is special - it returns a structured list of all extracted images with individual download URLs:
```



"job": { ... },




"images_content_metadata": {




"total_count": 3,




"images": [





"index": 0,




"filename": "image_0.png",




"content_type": "image/png",




"size_bytes": 12345,




"presigned_url": "https://s3.amazonaws.com/..."






"index": 1,




"filename": "image_1.jpg",




"content_type": "image/jpeg",




"size_bytes": 23456,




"presigned_url": "https://s3.amazonaws.com/..."






```

You can filter to specific images using the `image_filenames` parameter:


```


result = client.parsing.get(




job_id="job-123",




expand=["images_content_metadata"],




image_filenames=["image_0.png", "image_5.jpg"]



```

```


const result = await client.parsing.get({




job_id: "job-123",




expand: ["images_content_metadata"],




image_filenames: ["image_0.png", "image_5.jpg"],



```

## All Available Expand Values
[Section titled “All Available Expand Values”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#all-available-expand-values)
### Content Fields
[Section titled “Content Fields”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#content-fields-1)
#### text
[Section titled “text”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#text)
Returns the plain text extraction from each page.
**Structure:**
```



"text": {




"pages": [





"page_number": 1,




"text": "Extracted plain text content..."






```

#### markdown
[Section titled “markdown”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#markdown)
Returns the markdown-formatted content from each page with preserved structure.
**Important:** Not available for the `fast` tier.
**Structure:**
```



"markdown": {




"pages": [





"page_number": 1,




"success": true,




"markdown": "# Heading\n\n## Subheading\n\nContent with **formatting**...",




"header": "Page header",




"footer": "LlamaIndex 2026"






```

#### items
[Section titled “items”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#items)
Returns structured JSON with typed elements (tables, headings, lists, code blocks, etc.).
**Important:** Not available for the `fast` tier.
**Structure:**
```



"items": {




"pages": [





"page_number": 1,




"page_width": 612.0,




"page_height": 792.0,




"items": [





"type": "heading",




"level": 1,




"value": "Document Title",




"md": "# Document Title"






"type": "table",




"rows": [["Header1", "Header2"], ["Row1", "Data1"]],




"html": "<table>...</table>",




"csv": "Header1,Header2\nRow1,Data1",




"md": "| Header1 | Header2 |\n|---------|---------|..."






"success": true






```

#### metadata
[Section titled “metadata”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#metadata)
Returns page-level metadata including confidence scores, speaker notes, and document-specific information.
**Structure:**
```



"metadata": {




"pages": [





"page_number": 1,




"confidence": 0.95,




"speaker_notes": "Notes from presentation slide",




"slide_section_name": "Introduction",




"printed_page_number": "i",




"original_orientation_angle": 0,




"cost_optimized": false,




"triggered_auto_mode": false






"document": {




"XRBIData": "XBRL metadata for financial documents"





```

#### markdown_full
[Section titled “markdown_full”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#markdown_full)
Returns the complete raw markdown output as a single string (the full output.md file).
**Structure:**
```



"markdown_full": "# Complete Document\n\n## Chapter 1\n\nContent...\n\n---\n\n## Chapter 2..."



```

### Metadata Fields (Download URLs)
[Section titled “Metadata Fields (Download URLs)”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#metadata-fields-download-urls)
All metadata fields return information about result files stored in S3, including presigned download URLs:
```



"result_content_metadata": {




"md": {




"size_bytes": 45678,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/..."





"fullText": {




"size_bytes": 23456,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/..."





"json": {




"size_bytes": 67890,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/..."





```

This includes:
  * `text_content_metadata`
  * `markdown_content_metadata`
  * `items_content_metadata`
  * `metadata_content_metadata`
  * `xlsx_content_metadata`
  * `output_pdf_content_metadata`
  * `images_content_metadata` [See above](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#images-content-metadata)
  * `markdown_full_content_metadata`


## Important Limitations
[Section titled “Important Limitations”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#important-limitations)
### Fast Tier and Markdown
[Section titled “Fast Tier and Markdown”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#fast-tier-and-markdown)
The `fast` tier does **not support markdown expansion**. Requesting `markdown`, `items`, `markdown_content_metadata` or ìtems_content_metadata` with a fast tier job will result in an error:
```



"detail": "Markdown expansion is not available for FAST tier jobs."



```

### Presigned URL Expiration
[Section titled “Presigned URL Expiration”](https://developers.llamaindex.ai/python/cloud/llamaparse/basics/retrieving-results/#presigned-url-expiration)
Presigned URLs expire after a limited time. Download files promptly or request new URLs if needed.
