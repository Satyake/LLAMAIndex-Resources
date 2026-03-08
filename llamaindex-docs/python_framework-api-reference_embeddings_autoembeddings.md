# Autoembeddings
##  ChonkieAutoEmbedding [#](https://developers.llamaindex.ai/python/framework-api-reference/embeddings/autoembeddings/#llama_index.embeddings.autoembeddings.ChonkieAutoEmbedding "Permanent link")
Bases: 
Autoembeddings from chonkie.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`model_name` |  The name of the model to use. |  _required_  
Source code in `llama_index/embeddings/autoembeddings/base.py`
```
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
```
| ```
class ChonkieAutoEmbedding(BaseEmbedding):
"""
    Autoembeddings from chonkie.

    Args:
        model_name (str): The name of the model to use.

    """

    model_name: str
    embedder: Optional[chonkie.BaseEmbeddings] = None

    def __init__(self, model_name: str) -> None:
        super().__init__(model_name=model_name)
        self.embedder = AutoEmbeddings.get_embeddings(self.model_name)

    @classmethod
    def class_name(cls) -> str:
        return "ChonkieAutoEmbedding"

    def _get_embedding(self, text: str) -> List[float]:
        embed = self.embedder.embed(text)
        return embed.tolist()

    async def _aget_embedding(self, text: str) -> List[float]:
        return self._get_embedding(text)

    def _get_embeddings(self, texts: List[str]) -> List[List[float]]:
        embeds = self.embedder.embed_batch(texts)
        return [e.tolist() for e in embeds]

    async def _aget_embeddings(
        self,
        texts: List[str],
    ) -> List[List[float]]:
        return self._get_embeddings(texts)

    def _get_query_embedding(self, query: str) -> List[float]:
"""Get query embedding."""
        return self._get_embedding(query)

    async def _aget_query_embedding(self, query: str) -> List[float]:
"""Get query embedding."""
        return await self._aget_embedding(query)

    def _get_text_embedding(self, text: str) -> List[float]:
"""Get text embedding."""
        return self._get_embedding(text)

```
  
---|---  
options: members: - AutoEmbeddings
