# Wolfram alpha
##  WolframAlphaToolSpec [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/wolfram_alpha/#llama_index.tools.wolfram_alpha.WolframAlphaToolSpec "Permanent link")
Bases: 
Wolfram Alpha tool spec.
Source code in `llama_index/tools/wolfram_alpha/base.py`
```
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
```
| ```
class WolframAlphaToolSpec(BaseToolSpec):
"""Wolfram Alpha tool spec."""

    spec_functions = ["wolfram_alpha_query"]

    def __init__(self, app_id: Optional[str] = None) -> None:
"""Initialize with parameters."""
        self.token = app_id

    def wolfram_alpha_query(self, query: str):
"""
        Make a query to wolfram alpha about a mathematical or scientific problem.

        Example inputs:
            "(7 * 12 ^ 10) / 321"
            "How many calories are there in a pound of strawberries"

        Args:
            query (str): The query to be passed to wolfram alpha.

        """
        response = requests.get(
            QUERY_URL_TMPL.format(
                app_id=self.token, query=urllib.parse.quote_plus(query)
            )
        )
        return response.text

```
  
---|---  
###  wolfram_alpha_query [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/wolfram_alpha/#llama_index.tools.wolfram_alpha.WolframAlphaToolSpec.wolfram_alpha_query "Permanent link")
```
wolfram_alpha_query(query: )

```

Make a query to wolfram alpha about a mathematical or scientific problem.
Example inputs
"(7 * 12 ^ 10) / 321" "How many calories are there in a pound of strawberries"
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`query` |  The query to be passed to wolfram alpha. |  _required_  
Source code in `llama_index/tools/wolfram_alpha/base.py`
```
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
```
| ```
def wolfram_alpha_query(self, query: str):
"""
    Make a query to wolfram alpha about a mathematical or scientific problem.

    Example inputs:
        "(7 * 12 ^ 10) / 321"
        "How many calories are there in a pound of strawberries"

    Args:
        query (str): The query to be passed to wolfram alpha.

    """
    response = requests.get(
        QUERY_URL_TMPL.format(
            app_id=self.token, query=urllib.parse.quote_plus(query)
        )
    )
    return response.text

```
  
---|---  
options: members: - WolframAlphaToolSpec
