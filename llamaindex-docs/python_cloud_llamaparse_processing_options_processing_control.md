[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#_top)
# Processing Control
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Processing control options allow you to configure timeouts and job failure conditions for parsing operations.
## Timeouts
[Section titled “Timeouts”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#timeouts)
Configure how long parsing operations are allowed to run before timing out.
### Base Timeout
[Section titled “Base Timeout”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#base-timeout)
Set the base timeout for parsing operations in seconds (maximum 30 minutes).
```



"processing_control": {




"timeouts": {




"base_in_seconds": 300





```

### Extra Time Per Page
[Section titled “Extra Time Per Page”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#extra-time-per-page)
Set additional timeout per page in seconds (maximum 5 minutes per page).
```



"processing_control": {




"timeouts": {




"base_in_seconds": 300,




"extra_time_per_page_in_seconds": 30





```

## Job Failure Conditions
[Section titled “Job Failure Conditions”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#job-failure-conditions)
Configure conditions that determine when a parsing job should fail.
### Allowed Page Failure Ratio
[Section titled “Allowed Page Failure Ratio”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#allowed-page-failure-ratio)
Set the maximum ratio of pages allowed to fail (0-1). If more pages fail than this ratio, the entire job fails.
```



"processing_control": {




"job_failure_conditions": {




"allowed_page_failure_ratio": 0.1





```

### Fail on Image Extraction Error
[Section titled “Fail on Image Extraction Error”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#fail-on-image-extraction-error)
Fail the job if image extraction encounters errors.
```



"processing_control": {




"job_failure_conditions": {




"fail_on_image_extraction_error": true





```

### Fail on Image OCR Error
[Section titled “Fail on Image OCR Error”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#fail-on-image-ocr-error)
Fail the job if image OCR encounters errors.
```



"processing_control": {




"job_failure_conditions": {




"fail_on_image_ocr_error": true





```

### Fail on Markdown Reconstruction Error
[Section titled “Fail on Markdown Reconstruction Error”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#fail-on-markdown-reconstruction-error)
Fail the job if markdown reconstruction encounters errors.
```



"processing_control": {




"job_failure_conditions": {




"fail_on_markdown_reconstruction_error": true





```

### Fail on Buggy Font
[Section titled “Fail on Buggy Font”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#fail-on-buggy-font)
Fail the job if buggy fonts are detected in the document.
```



"processing_control": {




"job_failure_conditions": {




"fail_on_buggy_font": true





```

## Combined Configuration
[Section titled “Combined Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#combined-configuration)
You can combine timeout and failure condition settings:
```



"processing_control": {




"timeouts": {




"base_in_seconds": 600,




"extra_time_per_page_in_seconds": 45





"job_failure_conditions": {




"allowed_page_failure_ratio": 0.05,




"fail_on_image_extraction_error": false,




"fail_on_buggy_font": true





```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/processing_options/processing_control/#complete-api-request-example)


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




"processing_control": {




"timeouts": {




"base_in_seconds": 600





"job_failure_conditions": {




"allowed_page_failure_ratio": 0.1





```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic_plus",




version="latest",




processing_control={




"timeouts": {"base_in_seconds": 600},




"job_failure_conditions": {"allowed_page_failure_ratio": 0.1},





expand=["markdown"],



```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.pdf'),




tier: "agentic_plus",




version: "latest",




processing_control: {




timeouts: { base_in_seconds: 600 },




job_failure_conditions: { allowed_page_failure_ratio: 0.1 },





expand: ["markdown"],



```

