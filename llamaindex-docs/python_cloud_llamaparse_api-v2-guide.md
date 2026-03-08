[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#_top)
# LlamaParse API v2 Guide
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
This comprehensive guide covers the new v2 API endpoint for LlamaParse, which introduces a structured configuration approach for better organization and validation.
## Quick Start
[Section titled “Quick Start”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#quick-start)
### Basic Usage
[Section titled “Basic Usage”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#basic-usage)
**File ID Parsing (recommended):**
Terminal window```


curl-XPOST\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-H"Content-Type: application/json"\





"file_id": "existing-file-id",




"tier": "agentic",




"version": "latest"





"https://api.cloud.llamaindex.ai/api/v2/parse"


```

**URL Parsing:**
Terminal window```


curl-XPOST\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-H"Content-Type: application/json"\





"source_url": "https://example.com/document.pdf",




"tier": "cost_effective",




"version": "latest"





"https://api.cloud.llamaindex.ai/api/v2/parse"


```

**Multipart File Upload:**
Terminal window```


curl-XPOST\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-F"file=@document.pdf"\




-F'configuration={




"tier": "fast",




"version": "latest"





"https://api.cloud.llamaindex.ai/api/v2/parse/upload"


```

### What’s Different from v1
[Section titled “What’s Different from v1”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#whats-different-from-v1)
  * **Tier-based** : Instead of parse modes, choose from LlamaParse tiers (`fast`, `cost_effective`, `agentic`, `agentic_plus`)
  * **Two endpoints** : `/parse` for JSON requests (file ID or URL), `/parse/upload` for multipart file uploads
  * **Better validation** : Structured JSON schema with clear error messages
  * **Hierarchical organization** : Related settings are grouped logically


## Endpoint Details
[Section titled “Endpoint Details”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#endpoint-details)
v2 provides four endpoints:
### JSON Parsing (Recommended)
[Section titled “JSON Parsing (Recommended)”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#json-parsing-recommended)
  * **URL** : `https://api.cloud.llamaindex.ai/api/v2/parse`
  * **Method** : `POST`
  * **Content-Type** : `application/json`
  * **Use case** : Parse an already uploaded file by ID, or parse a document from a URL. Exactly one of `file_id` or `source_url` must be provided.


### Multipart File Upload
[Section titled “Multipart File Upload”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#multipart-file-upload)
  * **URL** : `https://api.cloud.llamaindex.ai/api/v2/parse/upload`
  * **Method** : `POST`
  * **Content-Type** : `multipart/form-data`
  * **Use case** : Traditional file uploads from client applications


### List Parse Jobs
[Section titled “List Parse Jobs”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#list-parse-jobs)
  * **URL** : `https://api.cloud.llamaindex.ai/api/v2/parse`
  * **Method** : `GET`
  * **Query Parameters** : `page_size`, `page_token`, `status`
  * **Use case** : List and filter parse jobs in a project with pagination


### Get Parse Results
[Section titled “Get Parse Results”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#get-parse-results)
  * **URL** : `https://api.cloud.llamaindex.ai/api/v2/parse/{job_id}`
  * **Method** : `GET`
  * **Query Parameters** : `expand` (comma-separated list of fields to include)
  * **Use case** : Check job status and retrieve parse results


**Required Headers** : `Authorization: Bearer YOUR_API_KEY` (all endpoints)
## Listing Parse Jobs
[Section titled “Listing Parse Jobs”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#listing-parse-jobs)
The list endpoint allows you to query parse jobs in your project with optional filtering and pagination:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse?page_size=10&status=COMPLETED'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

### Query Parameters
[Section titled “Query Parameters”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#query-parameters)
Parameter | Type | Description  
---|---|---  
`page_size` | integer | Maximum number of items to return per page (optional)  
`page_token` | string | Token for retrieving the next page of results (optional)  
`status` | string | Filter by job status: `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED` (optional)  
### Response Format
[Section titled “Response Format”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#response-format)
```



"items": [





"id": "job-uuid-1",




"project_id": "project-uuid",




"status": "COMPLETED",




"error_message": null






"id": "job-uuid-2",




"project_id": "project-uuid",




"status": "RUNNING",




"error_message": null






"next_page_token": "eyJsYXN0X2lkIjogImpvYi11dWlkLTIifQ==",




"total_size": 42



```

### Response Fields
[Section titled “Response Fields”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#response-fields)
Field | Type | Description  
---|---|---  
`items` | array | List of parse job objects  
`items[].id` | string | Unique identifier for the parse job  
`items[].project_id` | string | Project this job belongs to  
`items[].status` | string | Current status: `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED`  
`items[].error_message` | string | Error message if job failed (null otherwise)  
`next_page_token` | string | Token to retrieve the next page (null if no more pages)  
`total_size` | integer | Total number of jobs matching the filter (may be an estimate)  
### Pagination Example
[Section titled “Pagination Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#pagination-example)
To paginate through all results:
Terminal window```

# First page



curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse?page_size=10'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"




# Next page (using next_page_token from previous response)



curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse?page_size=10&page_token=eyJsYXN0X2lkIjogImpvYi11dWlkLTIifQ=='\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

### Filtering by Status
[Section titled “Filtering by Status”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#filtering-by-status)
Get only failed jobs:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse?status=FAILED'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

Get only pending jobs:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse?status=PENDING'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

## Job Status and Results
[Section titled “Job Status and Results”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#job-status-and-results)
The result endpoint returns job status and optionally the requested result data. You can poll this endpoint to check status and retrieve results when ready:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse/{job_id}?expand=markdown'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

The response always includes a `job` object with:
  * `id`: The parse job ID
  * `project_id`: The project ID
  * `status`: Job status (`PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED`)
  * `error_message`: Error details if job failed


### Expand Parameter
[Section titled “Expand Parameter”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#expand-parameter)
Use the `expand` query parameter to include additional content in the response. Multiple values can be comma-separated:
Value | Description  
---|---  
`text` | Include plain text result  
`markdown` | Include markdown result  
`items` | Include structured JSON items  
`metadata` | Include page-level metadata (confidence, speaker notes, etc.)  
`text_content_metadata` | Include text file metadata with presigned URL  
`markdown_content_metadata` | Include markdown file metadata with presigned URL  
`items_content_metadata` | Include items file metadata with presigned URL  
`metadata_content_metadata` | Include metadata file metadata with presigned URL  
`xlsx_content_metadata` | Include XLSX file metadata with presigned URL  
`output_pdf_content_metadata` | Include output PDF metadata with presigned URL  
`images_content_metadata` | Include images metadata with presigned URLs  
You can combine multiple parameters to get different result formats in a single request:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse/{job_id}?expand=markdown,text,images_content_metadata'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

### Content Metadata Response Format
[Section titled “Content Metadata Response Format”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#content-metadata-response-format)
When requesting `*_content_metadata` expand values (like `xlsx_content_metadata` or `output_pdf_content_metadata`), the response includes a `result_content_metadata` object with presigned URLs for downloading the files directly from S3:
```



"job": { ... },




"result_content_metadata": {




"xlsx": {




"size_bytes": 15234,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/bucket/path/to/file.xlsx?..."





"outputPDF": {




"size_bytes": 102400,




"exists": true,




"presigned_url": "https://s3.amazonaws.com/bucket/path/to/file.pdf?..."





```

Each metadata entry contains:
  * `size_bytes`: Size of the file in bytes
  * `exists`: Whether the file was generated and exists
  * `presigned_url`: Temporary URL to download the file directly (valid for a limited time)


### Images Content Metadata
[Section titled “Images Content Metadata”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#images-content-metadata)
When requesting `images_content_metadata`, the response includes a separate `images_content_metadata` object (not inside `result_content_metadata`):
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

Each image entry contains:
  * `index`: Index of the image in extraction order
  * `filename`: Image filename (e.g., “image_0.png”)
  * `content_type`: MIME type of the image (e.g., “image/png”)
  * `size_bytes`: Size of the image file in bytes
  * `presigned_url`: Temporary URL to download the image directly


### Image Filename Filtering
[Section titled “Image Filename Filtering”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#image-filename-filtering)
When requesting `images_content_metadata`, you can filter to specific images:
Terminal window```


curl-X'GET'\




'https://api.cloud.llamaindex.ai/api/v2/parse/{job_id}?expand=images_content_metadata&image_filenames=image_0.png,image_1.jpg'\




-H'accept: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"


```

## Choosing the Right Endpoint
[Section titled “Choosing the Right Endpoint”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#choosing-the-right-endpoint)
Select the appropriate endpoint based on your use case:
Endpoint | Use When | Input Method | Content-Type  
---|---|---|---  
`/parse` |  **Recommended** : Parse an already uploaded file by ID | File ID reference | `application/json`  
`/parse` | Parsing documents directly from web URLs, shared links, or public documents | URL reference | `application/json`  
`/parse/upload` | Uploading new files from client applications, web forms, or file pickers | Multipart form data | `multipart/form-data`  
**Key Differences:**
  * **URL fields** : The `/parse` endpoint accepts either `file_id` or `source_url` (with optional `http_proxy`). Exactly one must be provided.
  * **File handling** : `/parse/upload` uses traditional file uploads, `/parse` references existing files or fetches from URLs
  * **Configuration location** : `/parse/upload` uses form data with a `configuration` parameter, `/parse` embeds configuration in the JSON body


## Configuration Structure
[Section titled “Configuration Structure”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#configuration-structure)
The configuration structure varies by endpoint:
### JSON Parsing (`/parse`)
[Section titled “JSON Parsing (/parse)”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#json-parsing-parse)
**JSON Request Body:**
Use either `file_id` or `source_url` (exactly one is required):
**With file_id:**
```



"file_id": "existing-file-id",




"tier": "fast|cost_effective|agentic|agentic_plus",




"version": "latest|2026-01-08|2025-12-31|2025-12-18|2025-12-11",




"processing_options": {...},




"agentic_options": {...},




"webhook_configurations": [...],




"input_options": {...},




"crop_box": {...},




"page_ranges": {...},




"disable_cache": "boolean (optional)",




"output_options": {...},




"processing_control": {...}



```

**With source_url:**
```



"source_url": "https://example.com/document.pdf",




"http_proxy": "https://proxy.example.com",




"tier": "fast|cost_effective|agentic|agentic_plus",




"version": "latest|2026-01-08|2025-12-31|2025-12-18|2025-12-11",




"processing_options": {...},




"agentic_options": {...},




"webhook_configurations": [...],




"input_options": {...},




"crop_box": {...},




"page_ranges": {...},




"disable_cache": "boolean (optional)",




"output_options": {...},




"processing_control": {...}



```

### Multipart Upload (`/upload`)
[Section titled “Multipart Upload (/upload)”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#multipart-upload-upload)
**Form Parameters:**
  * `file` (required): The document file to upload
  * `configuration` (required): JSON string containing parsing options


**Configuration JSON Structure:**
```



"tier": "fast|cost_effective|agentic|agentic_plus",




"version": "latest|2026-01-08|2025-12-31|2025-12-18|2025-12-11",




"processing_options": {...},




"agentic_options": {...},




"webhook_configurations": [...],




"input_options": {...},




"crop_box": {...},




"page_ranges": {...},




"disable_cache": "boolean (optional)",




"output_options": {...},




"processing_control": {...}



```

## Tier-Based Parsing
[Section titled “Tier-Based Parsing”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#tier-based-parsing)
The new v2 API uses a simplified tier-based system instead of complex parse modes. The `tier` field determines how your document is processed, with automatic model selection and optimized settings for each tier.
### Agentic Plus Tier (`"agentic_plus"`)
[Section titled “Agentic Plus Tier ("agentic_plus")”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#agentic-plus-tier-agentic_plus)
**Best for** : Most complex documents requiring maximum accuracy (financial reports, dense layouts, scientific papers).
**Available Versions** (required):
  * `"latest"` - Always uses the most recent stable version
  * `"2026-01-08"` - Specific version for reproducible results
  * `"2025-12-31"` - Specific version for reproducible results
  * `"2025-12-18"` - Specific version for reproducible results
  * `"2025-12-11"` - Specific version for reproducible results


**Configuration example** :
```



"tier": "agentic_plus",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_diagonal_text": true





"ocr_parameters": {




"languages": ["en", "fr"]






"agentic_options": {




"custom_prompt": "Translate everything to French"




```

### Agentic Tier (`"agentic"`)
[Section titled “Agentic Tier ("agentic")”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#agentic-tier-agentic)
**Best for** : Complex documents requiring high accuracy with intelligent reasoning.
**Available Versions** (required):
  * `"latest"` - Always uses the most recent stable version
  * `"2026-01-08"` - Specific version for reproducible results
  * `"2025-12-31"` - Specific version for reproducible results
  * `"2025-12-18"` - Specific version for reproducible results
  * `"2025-12-11"` - Specific version for reproducible results


**Configuration example** :
```



"tier": "agentic",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_diagonal_text": true





"ocr_parameters": {




"languages": ["en"]






"agentic_options": {




"custom_prompt": "Translate everything to French"




```

### Cost Effective Tier (`"cost_effective"`)
[Section titled “Cost Effective Tier ("cost_effective")”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#cost-effective-tier-cost_effective)
**Best for** : Documents with mixed content requiring structured output while maintaining cost efficiency.
**Available Versions** (required):
  * `"latest"` - Always uses the most recent stable version
  * `"2026-01-08"` - Specific version for reproducible results
  * `"2025-12-31"` - Specific version for reproducible results
  * `"2025-12-18"` - Specific version for reproducible results
  * `"2025-12-11"` - Specific version for reproducible results


**Configuration example** :
```



"tier": "cost_effective",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_diagonal_text": true





"ocr_parameters": {




"languages": ["en", "fr"]






"agentic_options": {




"custom_prompt": "Translate everything to French"




```

> **Note** : The `cost_effective` tier also supports `agentic_options.custom_prompt` for customized AI processing.
### Fast Tier (`"fast"`)
[Section titled “Fast Tier ("fast")”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#fast-tier-fast)
**Best for** : Quick text extraction from simple documents where speed is prioritized over advanced formatting.
**Available Versions** (required):
  * `"latest"` - Always uses the most recent stable version
  * `"2026-01-08"` - Specific version for reproducible results
  * `"2025-12-31"` - Specific version for reproducible results
  * `"2025-12-18"` - Specific version for reproducible results
  * `"2025-12-11"` - Specific version for reproducible results


**Configuration example** :
```



"tier": "fast",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_diagonal_text": true





"ocr_parameters": {




"languages": ["de"]





```

> **Note** : The `fast` tier does not support `agentic_options` as it uses non-LLM processing for speed.
## Input Options
[Section titled “Input Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#input-options)
Configure how different file types are processed:
```



"input_options": {




"html": {




"make_all_elements_visible": true,




"remove_fixed_elements": true,




"remove_navigation_elements": true





"spreadsheet": {




"detect_sub_tables_in_sheets": true,




"force_formula_computation_in_sheets": true





"presentation": {




"out_of_bounds_content": true,





```

### HTML Options
[Section titled “HTML Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#html-options)
  * `make_all_elements_visible`: Forces hidden elements to be visible during parsing
  * `remove_fixed_elements`: Removes fixed-position elements (headers, sidebars)
  * `remove_navigation_elements`: Removes navigation menus


### Spreadsheet Options
[Section titled “Spreadsheet Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#spreadsheet-options)
  * `detect_sub_tables_in_sheets`: Find and extract sub-tables within spreadsheet cells
  * `force_formula_computation_in_sheets`: Force re-computation of spreadsheet cells containing formulas


### Presentation Options
[Section titled “Presentation Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#presentation-options)
  * `out_of_bounds_content`: Extract out of bounds content in presentation slides


## Page Ranges
[Section titled “Page Ranges”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#page-ranges)
Control which pages to process:
```



"page_ranges": {




"max_pages": 10,




"target_pages": "1,3,5-10"




```

  * `max_pages`: Maximum number of pages to process
  * `target_pages`: Specific pages using **1-based indexing** (e.g., “1,3,5-10” for pages 1, 3, and 5 through 10)


> **Important** : v2 uses 1-based page indexing, unlike v1 which used 0-based indexing.
## Crop Box
[Section titled “Crop Box”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#crop-box)
Define a specific area of each page to parse:
```



"crop_box": {




"top": 0.1,




"right": 0.1,




"bottom": 0.1,




"left": 0.1




```

Values are ratios (0.0 to 1.0) of the page dimensions. Example above crops 10% margin on all sides.
## Output Options
[Section titled “Output Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#output-options)
Customize the output format and structure:
### Markdown Options
[Section titled “Markdown Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#markdown-options)
```



"output_options": {




"markdown": {




"annotate_links": true,




"tables": {




"compact_markdown_tables": false,




"output_tables_as_markdown": false,




"markdown_table_multiline_separator": "",




"merge_continued_tables": true






```

#### Table Merging Across Pages
[Section titled “Table Merging Across Pages”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#table-merging-across-pages)
When `merge_continued_tables` is enabled, tables that continue across or within pages are automatically merged into a single table. This affects both the markdown output and the structured items output:
  * **Markdown output** : The full merged table is included on the first page in which the merged tables appear.
  * **Structured items output** : The first page contains the full merged table with the `merged_from_pages` field, while subsequent pages contain empty table with the `merged_into_page` field


Example structured output for a table spanning pages 1-4:
**Page 1 (contains full merged table):**
```



"type": "table",




"rows": [["Header1", "Header2"], ["Row1", "Data1"], ...],




"html": "<table>...</table>",




"md": "| Header1 | Header2 |...",




"csv": "Header1,Header2\nRow1,Data1\n...",




"merged_from_pages": [1, 2, 3, 4]



```

**Pages 2, 3, 4 (empty tables):**
```



"type": "table",




"rows": [],




"html": "",




"md": "",




"csv": "",




"merged_into_page": 1



```

### Spatial Text Options
[Section titled “Spatial Text Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#spatial-text-options)
```



"output_options": {




"spatial_text": {




"preserve_layout_alignment_across_pages": true,




"preserve_very_small_text": false,




"do_not_unroll_columns": false





```

### Export Options
[Section titled “Export Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#export-options)
```



"output_options": {




"tables_as_spreadsheet": {




"enable": true





"extract_printed_page_number": true




```

> **Note** : When `tables_as_spreadsheet.enable` is `true`, `guess_sheet_name` is automatically set to `true`.
### Image Output Control
[Section titled “Image Output Control”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#image-output-control)
Control which image types are saved during parsing using the `images_to_save` array:
```



"output_options": {




"images_to_save": ["screenshot", "embedded", "layout"]




```

Category | Description  
---|---  
`screenshot` | Full page screenshots  
`embedded` | Images embedded within the document  
`layout` | Cropped images from layout detection  
**Examples:**
Save only screenshots:
```


{ "output_options": { "images_to_save": ["screenshot"] } }


```

Save embedded images and layout crops:
```


{ "output_options": { "images_to_save": ["embedded", "layout"] } }


```

Save no images (explicit):
```


{ "output_options": { "images_to_save": [] } }


```

> **Note** : If `images_to_save` is not specified, no images are saved by default.
## Webhook Configuration
[Section titled “Webhook Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#webhook-configuration)
Set up notifications for job completion:
```



"webhook_configurations": [





"webhook_url": "https://your-app.com/webhook",




"webhook_headers": {




"X-Custom-Header": "value"





"webhook_events": ["parse.success"]





```

> **Note** : Currently only the first webhook configuration is used.
## Processing Control
[Section titled “Processing Control”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#processing-control)
Configure timeouts and error handling:
```



"processing_control": {




"timeouts": {




"base_in_seconds": 300,




"extra_time_per_page_in_seconds": 30





"job_failure_conditions": {




"allowed_page_failure_ratio": 0.1,




"fail_on_image_extraction_error": false,




"fail_on_image_ocr_error": false,




"fail_on_markdown_reconstruction_error": true,




"fail_on_buggy_font": false





```

## Cache Control
[Section titled “Cache Control”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#cache-control)
Disable caching for fresh results:
```



"disable_cache": true



```

When `true`, this both invalidates any existing cache and prevents caching of new results.
## Always-Enabled Features
[Section titled “Always-Enabled Features”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#always-enabled-features)
The following features are **always enabled** in v2 and cannot be disabled:
**All tiers:**
  * `adaptive_long_table`: Adaptive long table detection
  * `high_res_ocr`: High-resolution OCR processing
  * `outlined_table_extraction`: Outlined table extraction
  * `inline_images_in_markdown`: Image references are included inline in markdown output (e.g., `![description](image.jpg)`). To retrieve the actual image files, add `"embedded"` to `output_options.images_to_save`.


**Non-fast tiers** (`cost_effective`, `agentic`, `agentic_plus`):
  * `precise_bounding_box`: Precise bounding box detection for layout elements


These were made default because they improve results for most documents and simplify the API.
## Agentic Options
[Section titled “Agentic Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#agentic-options)
For `cost_effective`, `agentic`, and `agentic_plus` tiers, you can provide custom prompts to guide the AI processing:
```



"tier": "agentic",




"version": "latest",




"agentic_options": {




"custom_prompt": "Translate everything to French"




```

> **Note** : The `fast` tier does not support `agentic_options` as it uses non-LLM processing.
## Complete Configuration Examples
[Section titled “Complete Configuration Examples”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#complete-configuration-examples)
### File ID Parsing Example (Recommended)
[Section titled “File ID Parsing Example (Recommended)”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#file-id-parsing-example-recommended)
Terminal window```


curl-XPOST\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-H"Content-Type: application/json"\





"file_id": "existing-file-id",




"tier": "agentic_plus",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_diagonal_text": true,




"ignore_text_in_image": false





"ocr_parameters": {




"languages": ["en", "es"]






"agentic_options": {




"custom_prompt": "Translate everything to French"





"page_ranges": {




"max_pages": 20,




"target_pages": "1-5,10,15-20"





"crop_box": {




"top": 0.05,




"bottom": 0.95,




"left": 0.05,




"right": 0.95





"output_options": {




"markdown": {




"annotate_links": true,




"tables": {




"output_tables_as_markdown": true






"images_to_save": ["screenshot", "embedded"]





"webhook_configurations": [





"webhook_url": "https://example.com",




"webhook_events": ["parse.success"]






"processing_control": {




"timeouts": {




"base_in_seconds": 600





"job_failure_conditions": {




"allowed_page_failure_ratio": 0.05






"disable_cache": false





"https://api.cloud.llamaindex.ai/api/v2/parse"


```

### URL Parsing Example
[Section titled “URL Parsing Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#url-parsing-example)
Terminal window```


curl-XPOST\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-H"Content-Type: application/json"\





"source_url": "https://example.com/report.pdf",




"http_proxy": "https://proxy.example.com",




"tier": "cost_effective",




"version": "latest",




"processing_options": {




"ocr_parameters": {




"languages": ["en"]






"page_ranges": {




"max_pages": 20





"webhook_configurations": [{




"webhook_url": "https://example.com/webhook",




"webhook_events": ["parse.success"]






"https://api.cloud.llamaindex.ai/api/v2/parse"


```

### Multipart Upload Example
[Section titled “Multipart Upload Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#multipart-upload-example)
Terminal window```


curl-XPOST\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-F"file=@document.pdf"\




-F'configuration={




"tier": "agentic",




"version": "latest",




"processing_options": {




"ignore": {




"ignore_diagonal_text": true,




"ignore_text_in_image": false





"ocr_parameters": {




"languages": ["en", "es"]






"agentic_options": {




"custom_prompt": "Translate everything to French"





"page_ranges": {




"max_pages": 20,




"target_pages": "1-5,10,15-20"





"crop_box": {




"top": 0.05,




"bottom": 0.95,




"left": 0.05,




"right": 0.95





"output_options": {




"markdown": {




"annotate_links": true,




"tables": {




"output_tables_as_markdown": true






"images_to_save": ["screenshot"]





"webhook_configurations": [





"webhook_url": "https://example.com/webhook",




"webhook_events": ["parse.success"]






"processing_control": {




"timeouts": {




"base_in_seconds": 600





"job_failure_conditions": {




"allowed_page_failure_ratio": 0.05






"disable_cache": false





"https://api.cloud.llamaindex.ai/api/v2/parse/upload"


```

### Simple File ID Parsing Example
[Section titled “Simple File ID Parsing Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#simple-file-id-parsing-example)
Terminal window```


curl-XPOST\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




-H"Content-Type: application/json"\





"file_id": "existing-file-id",




"tier": "agentic_plus",




"version": "latest",




"output_options": {




"markdown": {




"annotate_links": true







"https://api.cloud.llamaindex.ai/api/v2/parse"


```

## Error Handling
[Section titled “Error Handling”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#error-handling)
v2 provides detailed validation errors:
```



"detail": [





"type": "value_error",




"loc": ["tier"],




"msg": "Unsupported tier: invalid_tier. Must be one of: fast, cost_effective, agentic, agentic_plus",




"input": {...}





```

## Migration from v1
[Section titled “Migration from v1”](https://developers.llamaindex.ai/python/cloud/llamaparse/api-v2-guide/#migration-from-v1)
If you’re migrating from v1, see our [detailed migration guide](https://developers.llamaindex.ai/python/cloud/llamaparse/v2/migration-v1-to-v2/) for parameter mapping and breaking changes.
