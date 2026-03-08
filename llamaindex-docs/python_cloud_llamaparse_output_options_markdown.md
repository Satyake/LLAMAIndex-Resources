[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#_top)
# Markdown Output Options
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Markdown output options allow you to configure how the parsed content is formatted when output as Markdown.
## Available Options
[Section titled “Available Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#available-options)
### Annotate Links
[Section titled “Annotate Links”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#annotate-links)
Add annotations to links in the markdown output, providing additional context about the link destinations.
```



"output_options": {




"markdown": {




"annotate_links": true





```

#### Inline image
[Section titled “Inline image”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#inline-image)
Inline images in the markdown output as a image tag `\[description\]\(path\)` instead of transcribing them,
```



"output_options": {




"markdown": {




"inline_images": true





```

### Page Options
[Section titled “Page Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#page-options)
Configure page-level formatting for markdown output:
### Table Options
[Section titled “Table Options”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#table-options)
Configure how tables are formatted in markdown output:
#### Compact Markdown Tables
[Section titled “Compact Markdown Tables”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#compact-markdown-tables)
Use compact formatting for markdown tables, reducing whitespace and creating more condensed table layouts.
```



"output_options": {




"markdown": {




"tables": {




"compact_markdown_tables": true






```

#### Output Tables as Markdown
[Section titled “Output Tables as Markdown”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#output-tables-as-markdown)
Control whether tables are output in markdown format or as HTML. Set to `false` to output tables as HTML instead of markdown.
```



"output_options": {




"markdown": {




"tables": {




"output_tables_as_markdown": false






```

#### Multiline Separator
[Section titled “Multiline Separator”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#multiline-separator)
Specify a separator for multiline content within markdown table cells.
```



"output_options": {




"markdown": {




"tables": {




"markdown_table_multiline_separator": ""






```

## Combined Configuration
[Section titled “Combined Configuration”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#combined-configuration)
You can combine multiple markdown options:
```



"output_options": {




"markdown": {




"annotate_links": true,




"tables": {




"compact_markdown_tables": true,




"output_tables_as_markdown": true






```

## Complete API Request Example
[Section titled “Complete API Request Example”](https://developers.llamaindex.ai/python/cloud/llamaparse/output_options/markdown/#complete-api-request-example)


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




"output_options": {




"markdown": {




"annotate_links": true,




"tables": {




"compact_markdown_tables": true






```

```


from llama_cloud import LlamaCloud





client =LlamaCloud(api_key="LLAMA_CLOUD_API_KEY")





result = client.parsing.parse(




upload_file="example_file.pdf",




tier="agentic_plus",




version="latest",




output_options={




"markdown": {




"annotate_links": True,




"tables": {




"compact_markdown_tables": True









print(result.markdown)


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




output_options: {




markdown: {




annotate_links: true,




tables: {




compact_markdown_tables: true









console.log(result.markdown);


```

