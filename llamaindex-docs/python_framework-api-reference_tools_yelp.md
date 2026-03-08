# Yelp
##  YelpToolSpec [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/yelp/#llama_index.tools.yelp.YelpToolSpec "Permanent link")
Bases: 
Yelp tool spec.
Source code in `llama_index/tools/yelp/base.py`
```
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
54
55
56
57
58
59
60
61
62
63
64
65
```
| ```
class YelpToolSpec(BaseToolSpec):
"""Yelp tool spec."""

    # TODO add disclaimer
    spec_functions = ["business_search", "business_reviews"]

    def __init__(self, api_key: str, client_id: str) -> Document:
"""Initialize with parameters."""
        from yelpapi import YelpAPI

        self.client = YelpAPI(api_key)

    def business_search(self, location: str, term: str, radius: Optional[int] = None):
"""
        Make a query to Yelp to find businesses given a location to search.

        Args:
            Businesses returned in the response may not be strictly within the specified location.
            term (str): Search term, e.g. "food" or "restaurants", The term may also be the business's name, such as "Starbucks"
            radius (int): A suggested search radius in meters. This field is used as a suggestion to the search. The actual search radius may be lower than the suggested radius in dense urban areas, and higher in regions of less business density.


        """
        response = self.client.search_query(location=location, term=term)
        return [Document(text=str(response))]

    def business_reviews(self, id: str):
"""
        Make a query to Yelp to find a business using an id from business_search.

        Args:
            # The id

        """
        response = self.client.reviews_query(id=id)
        return [Document(text=str(response))]

```
  
---|---  
###  business_search [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/yelp/#llama_index.tools.yelp.YelpToolSpec.business_search "Permanent link")
```
business_search(location: , term: , radius: Optional[] = None)

```

Make a query to Yelp to find businesses given a location to search.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`term` |  Search term, e.g. "food" or "restaurants", The term may also be the business's name, such as "Starbucks" |  _required_  
`radius` |  A suggested search radius in meters. This field is used as a suggestion to the search. The actual search radius may be lower than the suggested radius in dense urban areas, and higher in regions of less business density. |  `None`  
Source code in `llama_index/tools/yelp/base.py`
```
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
54
```
| ```
def business_search(self, location: str, term: str, radius: Optional[int] = None):
"""
    Make a query to Yelp to find businesses given a location to search.

    Args:
        Businesses returned in the response may not be strictly within the specified location.
        term (str): Search term, e.g. "food" or "restaurants", The term may also be the business's name, such as "Starbucks"
        radius (int): A suggested search radius in meters. This field is used as a suggestion to the search. The actual search radius may be lower than the suggested radius in dense urban areas, and higher in regions of less business density.


    """
    response = self.client.search_query(location=location, term=term)
    return [Document(text=str(response))]

```
  
---|---  
###  business_reviews [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/yelp/#llama_index.tools.yelp.YelpToolSpec.business_reviews "Permanent link")
```
business_reviews(id: )

```

Make a query to Yelp to find a business using an id from business_search.
Source code in `llama_index/tools/yelp/base.py`
```
56
57
58
59
60
61
62
63
64
65
```
| ```
def business_reviews(self, id: str):
"""
    Make a query to Yelp to find a business using an id from business_search.

    Args:
        # The id

    """
    response = self.client.reviews_query(id=id)
    return [Document(text=str(response))]

```
  
---|---  
options: members: - YelpToolSpec
