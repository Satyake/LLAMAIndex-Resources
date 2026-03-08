# Ollama
##  OllamaEmbedding [#](https://developers.llamaindex.ai/python/framework-api-reference/embeddings/ollama/#llama_index.embeddings.ollama.OllamaEmbedding "Permanent link")
Bases: 
Class for Ollama embeddings.
Source code in `llama_index/embeddings/ollama/base.py`
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
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
```
| ```
class OllamaEmbedding(BaseEmbedding):
"""Class for Ollama embeddings."""

    base_url: str = Field(description="Base url the model is hosted by Ollama")
    model_name: str = Field(description="The Ollama model to use.")
    embed_batch_size: int = Field(
        default=DEFAULT_EMBED_BATCH_SIZE,
        description="The batch size for embedding calls.",
        gt=0,
        le=2048,
    )
    ollama_additional_kwargs: Dict[str, Any] = Field(
        default_factory=dict, description="Additional kwargs for the Ollama API."
    )
    query_instruction: Optional[str] = Field(
        default=None, description="Instruction to prepend to query text."
    )
    text_instruction: Optional[str] = Field(
        default=None, description="Instruction to prepend to text."
    )
    keep_alive: Optional[Union[float, str]] = Field(
        default="5m",
        description="controls how long the model will stay loaded into memory following the request(default: 5m)",
    )

    _client: Client = PrivateAttr()
    _async_client: AsyncClient = PrivateAttr()

    def __init__(
        self,
        model_name: str,
        base_url: str = "http://localhost:11434",
        embed_batch_size: int = DEFAULT_EMBED_BATCH_SIZE,
        ollama_additional_kwargs: Optional[Dict[str, Any]] = None,
        query_instruction: Optional[str] = None,
        text_instruction: Optional[str] = None,
        callback_manager: Optional[CallbackManager] = None,
        client_kwargs: Optional[Dict[str, Any]] = None,
        keep_alive: Optional[Union[float, str]] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            model_name=model_name,
            base_url=base_url,
            embed_batch_size=embed_batch_size,
            ollama_additional_kwargs=ollama_additional_kwargs or {},
            query_instruction=query_instruction,
            text_instruction=text_instruction,
            callback_manager=callback_manager,
            keep_alive=keep_alive,
            **kwargs,
        )

        client_kwargs = client_kwargs or {}
        self._client = Client(host=self.base_url, **client_kwargs)
        self._async_client = AsyncClient(host=self.base_url, **client_kwargs)

    @classmethod
    def class_name(cls) -> str:
        return "OllamaEmbedding"

    def _get_query_embedding(self, query: str) -> List[float]:
"""Get query embedding."""
        formatted_query = self._format_query(query)
        return self.get_general_text_embedding(formatted_query)

    async def _aget_query_embedding(self, query: str) -> List[float]:
"""The asynchronous version of _get_query_embedding."""
        formatted_query = self._format_query(query)
        return await self.aget_general_text_embedding(formatted_query)

    def _get_text_embedding(self, text: str) -> List[float]:
"""Get text embedding."""
        formatted_text = self._format_text(text)
        return self.get_general_text_embedding(formatted_text)

    async def _aget_text_embedding(self, text: str) -> List[float]:
"""Asynchronously get text embedding."""
        formatted_text = self._format_text(text)
        return await self.aget_general_text_embedding(formatted_text)

    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
"""Get text embeddings."""
        embeddings_list: List[List[float]] = []
        for text in texts:
            formatted_text = self._format_text(text)
            embeddings = self.get_general_text_embedding(formatted_text)
            embeddings_list.append(embeddings)

        return embeddings_list

    async def _aget_text_embeddings(self, texts: List[str]) -> List[List[float]]:
"""Asynchronously get text embeddings."""
        formatted_texts = [self._format_text(text) for text in texts]
        return await asyncio.gather(
            *[self.aget_general_text_embedding(text) for text in formatted_texts]
        )

    def get_general_text_embedding(self, texts: str) -> List[float]:
"""Get Ollama embedding."""
        result = self._client.embed(
            model=self.model_name,
            input=texts,
            options=self.ollama_additional_kwargs,
            keep_alive=self.keep_alive,
        )
        return result.embeddings[0]

    async def aget_general_text_embedding(self, prompt: str) -> List[float]:
"""Asynchronously get Ollama embedding."""
        result = await self._async_client.embed(
            model=self.model_name,
            input=prompt,
            options=self.ollama_additional_kwargs,
            keep_alive=self.keep_alive,
        )
        return result.embeddings[0]

    def _format_query(self, query: str) -> str:
"""Format query with instruction if provided."""
        if self.query_instruction:
            return f"{self.query_instruction.strip()}{query.strip()}".strip()
        return query.strip()

    def _format_text(self, text: str) -> str:
"""Format text with instruction if provided."""
        if self.text_instruction:
            return f"{self.text_instruction.strip()}{text.strip()}".strip()
        return text.strip()

```
  
---|---  
###  get_general_text_embedding [#](https://developers.llamaindex.ai/python/framework-api-reference/embeddings/ollama/#llama_index.embeddings.ollama.OllamaEmbedding.get_general_text_embedding "Permanent link")
```
get_general_text_embedding(texts: ) -> [float]

```

Get Ollama embedding.
Source code in `llama_index/embeddings/ollama/base.py`
```
110
111
112
113
114
115
116
117
118
```
| ```
def get_general_text_embedding(self, texts: str) -> List[float]:
"""Get Ollama embedding."""
    result = self._client.embed(
        model=self.model_name,
        input=texts,
        options=self.ollama_additional_kwargs,
        keep_alive=self.keep_alive,
    )
    return result.embeddings[0]

```
  
---|---  
###  aget_general_text_embedding `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/embeddings/ollama/#llama_index.embeddings.ollama.OllamaEmbedding.aget_general_text_embedding "Permanent link")
```
aget_general_text_embedding(prompt: ) -> [float]

```

Asynchronously get Ollama embedding.
Source code in `llama_index/embeddings/ollama/base.py`
```
120
121
122
123
124
125
126
127
128
```
| ```
async def aget_general_text_embedding(self, prompt: str) -> List[float]:
"""Asynchronously get Ollama embedding."""
    result = await self._async_client.embed(
        model=self.model_name,
        input=prompt,
        options=self.ollama_additional_kwargs,
        keep_alive=self.keep_alive,
    )
    return result.embeddings[0]

```
  
---|---  
options: members: - OllamaEmbedding
