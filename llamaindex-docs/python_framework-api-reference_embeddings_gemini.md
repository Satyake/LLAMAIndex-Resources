# Gemini
##  GeminiEmbedding [#](https://developers.llamaindex.ai/python/framework-api-reference/embeddings/gemini/#llama_index.embeddings.gemini.GeminiEmbedding "Permanent link")
Bases: 
Google Gemini embeddings.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`model_name` |  Model for embedding. Defaults to "models/embedding-001". |  `'models/embedding-001'`  
`api_key` |  `Optional[str]` |  API key to access the model. Defaults to None. |  `None`  
`api_base` |  `Optional[str]` |  API base to access the model. Defaults to Official Base. |  `None`  
`transport` |  `Optional[str]` |  Transport to access the model. |  `None`  
Source code in `llama_index/embeddings/gemini/base.py`
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
141
142
143
144
```
| ```
@deprecated.deprecated(
    reason=(
        "Should use `llama-index-embeddings-google-genai` instead, using Google's latest unified SDK. "
        "See: https://docs.llamaindex.ai/en/stable/examples/embeddings/google_genai/"
    )
)
class GeminiEmbedding(BaseEmbedding):
"""
    Google Gemini embeddings.

    Args:
        model_name (str): Model for embedding.
            Defaults to "models/embedding-001".

        api_key (Optional[str]): API key to access the model. Defaults to None.
        api_base (Optional[str]): API base to access the model. Defaults to Official Base.
        transport (Optional[str]): Transport to access the model.

    """

    _model: gemini = PrivateAttr()
    _request_options: Optional[gemini.types.RequestOptions] = PrivateAttr()

    title: Optional[str] = Field(
        default="",
        description="Title is only applicable for retrieval_document tasks, and is used to represent a document title. For other tasks, title is invalid.",
    )
    task_type: Optional[str] = Field(
        default="retrieval_document",
        description="The task for embedding model.",
    )
    api_key: Optional[str] = Field(
        default=None,
        description="API key to access the model. Defaults to None.",
    )

    def __init__(
        self,
        model_name: str = "models/embedding-001",
        task_type: Optional[str] = "retrieval_document",
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        transport: Optional[str] = None,
        title: Optional[str] = None,
        embed_batch_size: int = DEFAULT_EMBED_BATCH_SIZE,
        callback_manager: Optional[CallbackManager] = None,
        request_options: Optional[gemini.types.RequestOptions] = None,
        **kwargs: Any,
    ):
        # API keys are optional. The API can be authorised via OAuth (detected
        # environmentally) or by the GOOGLE_API_KEY environment variable.
        config_params: Dict[str, Any] = {
            "api_key": api_key or os.getenv("GOOGLE_API_KEY"),
        }
        if api_base:
            config_params["client_options"] = {"api_endpoint": api_base}
        if transport:
            config_params["transport"] = transport
        # transport: A string, one of: [`rest`, `grpc`, `grpc_asyncio`].

        super().__init__(
            api_key=api_key,
            model_name=model_name,
            embed_batch_size=embed_batch_size,
            callback_manager=callback_manager,
            title=title,
            task_type=task_type,
            **kwargs,
        )
        gemini.configure(**config_params)

        self._model = gemini
        self._request_options = request_options

    @classmethod
    def class_name(cls) -> str:
        return "GeminiEmbedding"

    def _get_query_embedding(self, query: str) -> List[float]:
"""Get query embedding."""
        return self._model.embed_content(
            model=self.model_name,
            content=query,
            title=self.title,
            task_type=self.task_type,
            request_options=self._request_options,
        )["embedding"]

    def _get_text_embedding(self, text: str) -> List[float]:
"""Get text embedding."""
        return self._model.embed_content(
            model=self.model_name,
            content=text,
            title=self.title,
            task_type=self.task_type,
            request_options=self._request_options,
        )["embedding"]

    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
"""Get text embeddings."""
        return [
            self._model.embed_content(
                model=self.model_name,
                content=text,
                title=self.title,
                task_type=self.task_type,
                request_options=self._request_options,
            )["embedding"]
            for text in texts
        ]

    async def _aget_query_embedding(self, query: str) -> List[float]:
"""The asynchronous version of _get_query_embedding."""
        return (await self._aget_text_embeddings([query]))[0]

    async def _aget_text_embedding(self, text: str) -> List[float]:
"""Asynchronously get text embedding."""
        return (await self._aget_text_embeddings([text]))[0]

    async def _aget_text_embeddings(self, texts: List[str]) -> List[List[float]]:
"""Asynchronously get text embeddings."""
        response = await self._model.embed_content_async(
            model=self.model_name,
            content=texts,
            title=self.title,
            task_type=self.task_type,
            request_options=self._request_options,
        )
        return response["embedding"]

```
  
---|---  
options: members: - GeminiEmbedding
