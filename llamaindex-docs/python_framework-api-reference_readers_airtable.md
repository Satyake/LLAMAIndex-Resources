# Airtable
##  AirtableReader [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/airtable/#llama_index.readers.airtable.AirtableReader "Permanent link")
Bases: 
Airtable reader. Reads data from a table in a base.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`api_key` |  Airtable API key. |  _required_  
Source code in `llama_index/readers/airtable/base.py`
```
10
11
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
class AirtableReader(BaseReader):
"""
    Airtable reader. Reads data from a table in a base.

    Args:
        api_key (str): Airtable API key.

    """

    def __init__(self, api_key: str) -> None:
"""Initialize Airtable reader."""
        self.api_key = api_key

    def load_data(self, base_id: str, table_id: str) -> List[Document]:
"""
        Load data from a table in a base.

        Args:
            table_id (str): Table ID.
            base_id (str): Base ID.


        Returns:
            List[Document]: List of documents.

        """
        table = Table(self.api_key, base_id, table_id)
        all_records = table.all()
        return [Document(text=f"{all_records}", extra_info={})]

```
  
---|---  
###  load_data [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/airtable/#llama_index.readers.airtable.AirtableReader.load_data "Permanent link")
```
load_data(base_id: , table_id: ) -> []

```

Load data from a table in a base.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`table_id` |  Table ID. |  _required_  
`base_id` |  Base ID. |  _required_  
Returns:
Type | Description  
---|---  
`List[Document[](https://developers.llamaindex.ai/python/framework-api-reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` |  List[Document]: List of documents.  
Source code in `llama_index/readers/airtable/base.py`
```
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
def load_data(self, base_id: str, table_id: str) -> List[Document]:
"""
    Load data from a table in a base.

    Args:
        table_id (str): Table ID.
        base_id (str): Base ID.


    Returns:
        List[Document]: List of documents.

    """
    table = Table(self.api_key, base_id, table_id)
    all_records = table.all()
    return [Document(text=f"{all_records}", extra_info={})]

```
  
---|---  
options: members: - AirtableReader
