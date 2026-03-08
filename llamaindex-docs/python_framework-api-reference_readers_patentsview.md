# Patentsview
##  PatentsviewReader [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/patentsview/#llama_index.readers.patentsview.PatentsviewReader "Permanent link")
Bases: 
Patentsview reader.
Read patent abstract.
Source code in `llama_index/readers/patentsview/base.py`
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
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
```
| ```
class PatentsviewReader(BaseReader):
"""
    Patentsview reader.

    Read patent abstract.

    """

    def __init__(self) -> None:
"""Initialize with request body."""
        self.json = {"q": {"patent_id": None}, "f": ["patent_abstract"]}

    def load_data(self, patent_number: List[str]) -> List[Document]:
"""
        Load patent abstract given list of patent numbers.

        Args:
            patent_number: List[str]: List of patent numbers, e.g., 8848839.

        Returens:
            List[Document]: A list of Document objects, each including the abstract for a patent.

        """
        if not patent_number:
            raise ValueError("Please input patent number")

        self.json["q"]["patent_id"] = patent_number

        response = requests.post(BASE_URL, json=self.json)

        if response.status_code == 200:
            data = response.json()
            patents = data.get("patents", [])

            results = []
            for patent in patents:
                results.append(Document(text=patent["patent_abstract"]))

        else:
            raise Exception(f"Request failed with status code: {response.status_code}")

        return results

```
  
---|---  
###  load_data [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/patentsview/#llama_index.readers.patentsview.PatentsviewReader.load_data "Permanent link")
```
load_data(patent_number: []) -> []

```

Load patent abstract given list of patent numbers.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`patent_number` |  `List[str]` |  List[str]: List of patent numbers, e.g., 8848839. |  _required_  
Returens
List[Document]: A list of Document objects, each including the abstract for a patent.
Source code in `llama_index/readers/patentsview/base.py`
```
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
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
```
| ```
def load_data(self, patent_number: List[str]) -> List[Document]:
"""
    Load patent abstract given list of patent numbers.

    Args:
        patent_number: List[str]: List of patent numbers, e.g., 8848839.

    Returens:
        List[Document]: A list of Document objects, each including the abstract for a patent.

    """
    if not patent_number:
        raise ValueError("Please input patent number")

    self.json["q"]["patent_id"] = patent_number

    response = requests.post(BASE_URL, json=self.json)

    if response.status_code == 200:
        data = response.json()
        patents = data.get("patents", [])

        results = []
        for patent in patents:
            results.append(Document(text=patent["patent_abstract"]))

    else:
        raise Exception(f"Request failed with status code: {response.status_code}")

    return results

```
  
---|---  
options: members: - PatentsviewReader
