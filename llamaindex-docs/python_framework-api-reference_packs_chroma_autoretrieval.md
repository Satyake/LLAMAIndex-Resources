# Chroma autoretrieval
##  ChromaAutoretrievalPack [#](https://developers.llamaindex.ai/python/framework-api-reference/packs/chroma_autoretrieval/#llama_index.packs.chroma_autoretrieval.ChromaAutoretrievalPack "Permanent link")
Bases: 
Chroma auto-retrieval pack.
Source code in `llama_index/packs/chroma_autoretrieval/base.py`
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
```
| ```
class ChromaAutoretrievalPack(BaseLlamaPack):
"""Chroma auto-retrieval pack."""

    def __init__(
        self,
        collection_name: str,
        vector_store_info: VectorStoreInfo,
        nodes: Optional[List[TextNode]] = None,
        client: Optional[Any] = None,
        **kwargs: Any,
    ) -> None:
"""Init params."""
        import chromadb

        chroma_client = client or chromadb.EphemeralClient()
        chroma_collection = chroma_client.get_or_create_collection(collection_name)

        self._vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

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

        self.retriever = VectorIndexAutoRetriever(
            self._index, vector_store_info=vector_store_info
        )
        self.query_engine = RetrieverQueryEngine(self.retriever)

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
###  get_modules [#](https://developers.llamaindex.ai/python/framework-api-reference/packs/chroma_autoretrieval/#llama_index.packs.chroma_autoretrieval.ChromaAutoretrievalPack.get_modules "Permanent link")
```
get_modules() -> [, ]

```

Get modules.
Source code in `llama_index/packs/chroma_autoretrieval/base.py`
```
54
55
56
57
58
59
60
61
62
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
###  retrieve [#](https://developers.llamaindex.ai/python/framework-api-reference/packs/chroma_autoretrieval/#llama_index.packs.chroma_autoretrieval.ChromaAutoretrievalPack.retrieve "Permanent link")
```
retrieve(query_str: ) -> 

```

Retrieve.
Source code in `llama_index/packs/chroma_autoretrieval/base.py`
```
64
65
66
```
| ```
def retrieve(self, query_str: str) -> Any:
"""Retrieve."""
    return self.retriever.retrieve(query_str)

```
  
---|---  
###  run [#](https://developers.llamaindex.ai/python/framework-api-reference/packs/chroma_autoretrieval/#llama_index.packs.chroma_autoretrieval.ChromaAutoretrievalPack.run "Permanent link")
```
run(*args: , **kwargs: ) -> 

```

Run the pipeline.
Source code in `llama_index/packs/chroma_autoretrieval/base.py`
```
68
69
70
```
| ```
def run(self, *args: Any, **kwargs: Any) -> Any:
"""Run the pipeline."""
    return self.query_engine.query(*args, **kwargs)

```
  
---|---  
options: members: - ChromaAutoretrievalPack
