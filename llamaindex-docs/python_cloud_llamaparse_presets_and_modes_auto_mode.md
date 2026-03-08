[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaparse/presets_and_modes/auto_mode/#_top)
# Auto Mode
Automatically routes each page to Balanced or Premium preset
#### Overview
[Section titled “Overview”](https://developers.llamaindex.ai/python/cloud/llamaparse/presets_and_modes/auto_mode/#overview)
Auto Mode analyzes each page individually and dynamically chooses between Balanced and Premium parsing. This allows for higher accuracy while reducing unnecessary cost.
#### Under the Hood
[Section titled “Under the Hood”](https://developers.llamaindex.ai/python/cloud/llamaparse/presets_and_modes/auto_mode/#under-the-hood)
When `auto_mode=True` is enabled, LlamaParse first attempts to parse each page using Balanced Mode. If specific conditions are met, it will automatically reparse that page using Premium Mode for improved fidelity.
This mode enables flexibility but may result in variable and less predictable costs depending on the content of the file.
To use this mode, set `auto_mode=True`.


```


parser =LlamaParse(




auto_mode=True



```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'\




-H'accept: application/json'\




-H'Content-Type: multipart/form-data'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--form'auto_mode="true"'\




-F'file=@/path/to/your/file.pdf;type=application/pdf'


```

## Trigger on Table
[Section titled “Trigger on Table”](https://developers.llamaindex.ai/python/cloud/llamaparse/presets_and_modes/auto_mode/#trigger-on-table)
If you want to upgrade parsing to Premium when a table is detected on the page, set `auto_mode_trigger_on_table_in_page=True`.


```


parser =LlamaParse(




auto_mode_trigger_on_table_in_page=True



```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'\




-H'accept: application/json'\




-H'Content-Type: multipart/form-data'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--form'auto_mode_trigger_on_table_in_page="true"'\




-F'file=@/path/to/your/file.pdf;type=application/pdf'


```

## Trigger on Image
[Section titled “Trigger on Image”](https://developers.llamaindex.ai/python/cloud/llamaparse/presets_and_modes/auto_mode/#trigger-on-image)
If you want to upgrade parsing to Premium when images are present on a page, set `auto_mode_trigger_on_image_in_page=True`.


```


parser =LlamaParse(




auto_mode_trigger_on_image_in_page=True



```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'\




-H'accept: application/json'\




-H'Content-Type: multipart/form-data'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--form'auto_mode_trigger_on_image_in_page="true"'\




-F'file=@/path/to/your/file.pdf;type=application/pdf'


```

## Trigger on RegExp
[Section titled “Trigger on RegExp”](https://developers.llamaindex.ai/python/cloud/llamaparse/presets_and_modes/auto_mode/#trigger-on-regexp)
To trigger Premium parsing when a regular expression matches text on the page, set `auto_mode_trigger_on_regexp_in_page` to your pattern (ECMA262 format).


```


parser =LlamaParse(




auto_mode_trigger_on_regexp_in_page="/((total cost)|(tax))/g"



```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'\




-H'accept: application/json'\




-H'Content-Type: multipart/form-data'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--form'auto_mode_trigger_on_regexp_in_page="/((total cost)|(tax))/g"'\




-F'file=@/path/to/your/file.pdf;type=application/pdf'


```

## Trigger on Text
[Section titled “Trigger on Text”](https://developers.llamaindex.ai/python/cloud/llamaparse/presets_and_modes/auto_mode/#trigger-on-text)
To trigger Premium parsing when specific text appears on a page, use `auto_mode_trigger_on_text_in_page`.


```


parser =LlamaParse(




auto_mode_trigger_on_text_in_page="total"



```

Terminal window```


curl-X'POST'\




'https://api.cloud.llamaindex.ai/api/v1/parsing/upload'\




-H'accept: application/json'\




-H'Content-Type: multipart/form-data'\




-H"Authorization: Bearer $LLAMA_CLOUD_API_KEY"\




--form'auto_mode_trigger_on_text_in_page="total"'\




-F'file=@/path/to/your/file.pdf;type=application/pdf'


```

