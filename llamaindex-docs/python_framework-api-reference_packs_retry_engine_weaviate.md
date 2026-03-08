# Retry engine weaviate
##  WeaviateRetryEnginePack [#](https://developers.llamaindex.ai/python/framework-api-reference/packs/retry_engine_weaviate/#llama_index.packs.retry_engine_weaviate.WeaviateRetryEnginePack "Permanent link")
Bases: 
Weaviate Retry query engine pack.
Source code in `llama_index/packs/retry_engine_weaviate/base.py`
```
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
66
67
68
69
70
71
72
73
74
75
76
77
78
```
| ```
class WeaviateRetryEnginePack(BaseLlamaPack):
"""Weaviate Retry query engine pack."""

    def __init__(
        self,
        collection_name: str,
        vector_store_info: VectorStoreInfo,
        host: str,
        auth_client_secret: str,
        nodes: Optional[List[TextNode]] = None,
        **kwargs: Any,
    ) -> None:
"""Init params."""
        from weaviate import Client

        self.client: Client = Client(host, auth_client_secret=auth_client_secret)

        weaviate_client = self.client
        weaviate_collection = weaviate_client.get_or_create_collection(collection_name)

        self._vector_store = WeaviateVectorStore(
            weaviate_collection=weaviate_collection
        )

        if nodes is not None:
            self._storage_context = StorageContext.from_defaults(
                vector_store=self._vector_store
            )
            self._index = VectorStoreIndex(
                nodes, storage_context=self._storage_context, **kwargs
            )
        else:
            self._index = VectorStoreIndex.from_vector_store(
                self._vector_store, **kwargs
            )
            self._storage_context = self._index.storage_context

        self.retriever = self._index.as_retriever()

        base_query_engine = self._index.as_query_engine()
        guideline_eval = GuidelineEvaluator(guidelines=DEFAULT_GUIDELINES)
        self.query_engine = RetryGuidelineQueryEngine(
            base_query_engine, guideline_eval, resynthesize_query=True
        )

    def get_modules(self) -> Dict[str, Any]:
"""Get modules."""
        return {
            "vector_store": self._vector_store,
            "storage_context": self._storage_context,
            "index": self._index,
            "retriever": self.retriever,
            "query_engine": self.query_engine,
        }

    def retrieve(self, query_str: str) -> Any:
"""Retrieve."""
        return self.retriever.retrieve(query_str)

    def run(self, *args: Any, **kwargs: Any) -> Any:
"""Run the pipeline."""
        return self.query_engine.query(*args, **kwargs)

```
  
---|---  
###  get_modules [#](https://developers.llamaindex.ai/python/framework-api-reference/packs/retry_engine_weaviate/#llama_index.packs.retry_engine_weaviate.WeaviateRetryEnginePack.get_modules "Permanent link")
```
get_modules() -> [, ]

```

Get modules.
Source code in `llama_index/packs/retry_engine_weaviate/base.py`
```
62
63
64
65
66
67
68
69
70
```
| ```
def get_modules(self) -> Dict[str, Any]:
"""Get modules."""
    return {
        "vector_store": self._vector_store,
        "storage_context": self._storage_context,
        "index": self._index,
        "retriever": self.retriever,
        "query_engine": self.query_engine,
    }

```
  
---|---  
###  retrieve [#](https://developers.llamaindex.ai/python/framework-api-reference/packs/retry_engine_weaviate/#llama_index.packs.retry_engine_weaviate.WeaviateRetryEnginePack.retrieve "Permanent link")
```
retrieve(query_str: ) -> 

```

Retrieve.
Source code in `llama_index/packs/retry_engine_weaviate/base.py`
```
72
73
74
```
| ```
def retrieve(self, query_str: str) -> Any:
"""Retrieve."""
    return self.retriever.retrieve(query_str)

```
  
---|---  
###  run [#](https://developers.llamaindex.ai/python/framework-api-reference/packs/retry_engine_weaviate/#llama_index.packs.retry_engine_weaviate.WeaviateRetryEnginePack.run "Permanent link")
```
run(*args: , **kwargs: ) -> 

```

Run the pipeline.
Source code in `llama_index/packs/retry_engine_weaviate/base.py`
```
76
77
78
```
| ```
def run(self, *args: Any, **kwargs: Any) -> Any:
"""Run the pipeline."""
    return self.query_engine.query(*args, **kwargs)

```
  
---|---  
options: members: - WeaviateRetryEnginePack
