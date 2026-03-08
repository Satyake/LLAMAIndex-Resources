[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/spatial_text/#_top)
# Spatial Text Output Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Spatial text output options allow you to configure how text positioning and layout are preserved in the spatial text output format.
## What is Spatial Text?
[Section titled “What is Spatial Text?”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/spatial_text/#what-is-spatial-text)
Spatial text is a text format where whitespace is strategically inserted to preserve the spatial positioning of text elements on the page. Instead of flowing text in reading order, spatial text maintains the original layout by using spaces and line breaks to keep elements in their correct relative positions.
This format is particularly useful for:
  * Documents with complex layouts (forms, tables, diagrams)
  * Preserving visual relationships between text elements
  * Maintaining column structures and alignments
  * CAD drawings or technical documents where positioning matters


## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/spatial_text/#available-options)
### Preserve Layout Alignment Across Pages
[Section titled “Preserve Layout Alignment Across Pages”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/spatial_text/#preserve-layout-alignment-across-pages)
Preserve text alignment across page boundaries. This is useful for documents with continuous tables or consistent alignment that spans multiple pages.
```



"output_options": {




"spatial_text": {




"preserve_layout_alignment_across_pages": true





```

### Preserve Very Small Text
[Section titled “Preserve Very Small Text”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/spatial_text/#preserve-very-small-text)
Include very small text in the spatial output. This can be useful for documents containing vector graphics with very small text lines that may not be recognized by OCR or vision models (such as in CAD drawings).
```



"output_options": {




"spatial_text": {




"preserve_very_small_text": true





```

### Do Not Unroll Columns
[Section titled “Do Not Unroll Columns”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/spatial_text/#do-not-unroll-columns)
Keep column structure intact without unrolling. By default, LlamaParse tries to unroll columns into reading order. Enable this option to maintain the original column layout.
```



"output_options": {




"spatial_text": {




"do_not_unroll_columns": true





```

## Combined Configuration
[Section titled “Combined Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/spatial_text/#combined-configuration)
You can combine multiple spatial text options:
```



"output_options": {




"spatial_text": {




"preserve_layout_alignment_across_pages": true,




"preserve_very_small_text": true,




"do_not_unroll_columns": false





```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/spatial_text/#complete-api-request-example)


Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v2/parse'\




-H'Accept: application/json'\




-H'Content-Type: application/json'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--data'{




"file_id": "<file_id>",




"tier": "fast",




"version": "latest",




"output_options": {




"spatial_text": {




"preserve_layout_alignment_across_pages": true,




"preserve_very_small_text": true





```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="fast",




version="latest",




output_options={




"spatial_text": {




"preserve_layout_alignment_across_pages": True,




"preserve_very_small_text": True






expand=["text"]






print(result.text)


```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud({




apiKey: "LLAMA_CLOUD_API_KEY",






const result = await client.parsing.parse({




upload_file: fs.createReadStream('example_file.pdf'),




tier: "fast",




version: "latest",




output_options: {




spatial_text: {




preserve_layout_alignment_across_pages: true,




preserve_very_small_text: true






expand: ["text"],






console.log(result.text);


```

