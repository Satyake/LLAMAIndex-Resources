[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/tutorials/parse_with_prompts/#_top)
# Parse with Additional Prompts
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
[Parsing prompts](https://developers.llamaindex.ai/python/cloud/llamaparse/features/prompts) allow you to guide our parsing model in the same way you would instruct an LLM.
These prompts can be useful for improving the parser’s performance on complex document layouts, extracting data in a specific format, or transforming the document in other ways.
In this example, we showcase how providing addtiaional instructions (prompts) to LlamaParse can be used to shape the way an LLM parses information from unstructured documents. Using a McDonald’s Receipt, we show how to ignore parts of the document and only parse the price of each order and the final amount to be paid.
## Setup
[Section titled “Setup”](https://developers.llamaindex.ai/python/cloud/llamaparse/tutorials/parse_with_prompts/#setup)
First, we setup our environment and connect to LlamaCloud:
Terminal window```


pipinstallllama-cloud


```

```


import os




from getpass import getpass





os.environ["LLAMA_CLOUD_API_KEY"] =getpass("Llama Cloud API Key: ")


```

## Parse Receipt With No Instructions
[Section titled “Parse Receipt With No Instructions”](https://developers.llamaindex.ai/python/cloud/llamaparse/tutorials/parse_with_prompts/#parse-receipt-with-no-instructions)
For this example, we’re using the following McDonald’s receipt. Download it and save it with the name `mcdonalds_receipt.png`:
We start off by intilizing `LlamaParse`, with no instructions:
```


from llama_cloud import AsyncLlamaCloud





llama_cloud_client =AsyncLlamaCloud(




api_key=os.getenv("LLAMA_CLOUD_API_KEY")



```

The results we get are the following:
```


from llama_cloud.types.parsing_create_params import OutputOptions, OutputOptionsMarkdown, OutputOptionsMarkdownTables, ProcessingOptions, ProcessingOptionsAutoModeConfiguration, ProcessingOptionsAutoModeConfigurationParsingConf





file_obj =await llama_cloud_client.files.create(




file="mcdonalds_receipt.png",




purpose="parse",




external_file_id="mcdonalds_receipt.png",





vanilla_result =await llama_cloud_client.parsing.parse(




tier="agentic",




version="latest",




file_id=file_obj.id,




expand=["markdown"],




output_options=OutputOptions(




markdown=OutputOptionsMarkdown(




tables=OutputOptionsMarkdownTables(output_tables_as_markdown=True)






processing_options=ProcessingOptions(




auto_mode_configuration=[ProcessingOptionsAutoModeConfiguration(




parsing_conf=ProcessingOptionsAutoModeConfigurationParsingConf(




high_res_ocr=True,




outlined_table_extraction=True








print(vanilla_result.markdown.pages[0].markdown)


```

```

Started parsing the file under job_id fa0c25a4-999f-439a-81a2-54f024ce2809




> Rate us HIGHLY SATISFIED and


> Receive ONE FREE ITEM


> Purchase any sandwich and receive an item of equal or lesser value


> Go to www.mcdvoice.com within 7 days and tell us about your visit.


> Validation Code:


> Expires 30 days after receipt date.


> Valid at participating US McDonald's.


> Survey Code:


> 31278-01121-21018-20481-00081-0



## McDonald's Restaurant #31278


2378 PINE RD NW


RICE, MN 56367-9740


TEL# 320 393 4600



| KS# 1           | 12/08/2022 08:48 PM |


|-----------------|---------------------|


| Side1           | Order 12            |



| Item                     | Price |


|--------------------------|-------|


| 1 Happy Meal 6 Pc        | 4.89  |


| - 1 Creamy Ranch Cup     |       |


| - 1 Extra Kids Fry       |       |


| - 1 Wreck It Ralph 2     |       |


| - 1 S Coke               |       |


| 1 Snack Oreo McFlurry    | 2.69  |



| Subtotal                 | 7.58  |


| Tax                      | 0.52  |


| Take-Out Total           | 8.10  |



| Cash Tendered            | 10.00 |


| Change                   | 1.90  |



> McDonalds Restaurant Rice


> ***NOW ACCEPTING APPLICATIONS***


> text to #36453


> apply31278

```

## Parse Receipt With Instructions
[Section titled “Parse Receipt With Instructions”](https://developers.llamaindex.ai/python/cloud/llamaparse/tutorials/parse_with_prompts/#parse-receipt-with-instructions)
Now let’s have a look at the way we can change the output by providing an additional prompt:
```


from llama_cloud.types.parsing_create_params import AgenticOptions





parsing_instruction ="""The provided document is a McDonald's receipt. Provide ONLY each line item (item name and price) and the final amount to be paid."""





result_with_prompt =await llama_cloud_client.parsing.parse(




tier="agentic",




version="latest",




file_id=file_obj.id,




expand=["markdown"],




output_options=OutputOptions(




markdown=OutputOptionsMarkdown(




tables=OutputOptionsMarkdownTables(output_tables_as_markdown=True)






processing_options=ProcessingOptions(




auto_mode_configuration=[ProcessingOptionsAutoModeConfiguration(




parsing_conf=ProcessingOptionsAutoModeConfigurationParsingConf(




high_res_ocr=True,




outlined_table_extraction=True,




custom_prompt=parsing_instruction









print(result_with_prompt.markdown.pages[0].markdown)


```

Which results in:
```

Started parsing the file under job_id 4c6a6443-0590-4384-b84d-65e4455f5e48



* Happy Meal 6 Pc 4.89


* Snack Oreo McFlurry 2.69



Take-Out Total 8.10

```

