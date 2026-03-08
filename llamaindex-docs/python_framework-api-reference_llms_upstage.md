# Upstage
##  Upstage [#](https://developers.llamaindex.ai/python/framework-api-reference/llms/upstage/#llama_index.llms.upstage.Upstage "Permanent link")
Bases: 
Upstage LLM.
Examples:
`pip install llama-index-llms-upstage`
```
from llama_index.llms.upstage import Upstage
import os

os.environ["UPSTAGE_API_KEY"] = "YOUR_API_KEY"

llm = Upstage()
stream = llm.stream("Hello, how are you?")

for response in stream:
    print(response.delta, end="")

```

Source code in `llama_index/llms/upstage/base.py`
```
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
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
```
| ```
class Upstage(OpenAI):
"""
    Upstage LLM.

    Examples:
        `pip install llama-index-llms-upstage`

        ```python
        from llama_index.llms.upstage import Upstage
        import os

        os.environ["UPSTAGE_API_KEY"] = "YOUR_API_KEY"

        llm = Upstage()
        stream = llm.stream("Hello, how are you?")

        for response in stream:
            print(response.delta, end="")

        ```

    """

    model_config = ConfigDict(arbitrary_types_allowed=True, populate_by_name=True)
    model: str = Field(
        default=DEFAULT_UPSTAGE_MODEL, description="The Upstage model to use."
    )
    temperature: float = Field(
        default=DEFAULT_TEMPERATURE,
        description="The temperature to use during generation.",
        gte=0.0,
        lte=1.0,
    )
    max_tokens: Optional[int] = Field(
        description="The maximum number of tokens to generate."
    )
    logprobs: Optional[bool] = Field(
        description="Whether to return logprobs per token."
    )
    top_logprobs: int = Field(
        description="The number of top token logprobs to return.",
        default=0,
        gte=0,
        lte=20,
    )
    additional_kwargs: Dict[str, Any] = Field(
        description="Additional kwargs for the Upstage API.", default_factory=dict
    )
    max_retries: int = Field(
        description="The maximum number of API retries.", default=3, gte=0
    )
    timeout: float = Field(
        description="The timeout, in seconds, for API requests.", default=60.0, gte=0.0
    )
    reuse_client: bool = Field(
        description=(
            "Reuse the OpenAI client between requests. When doing anything with large "
            "volumes of async API calls, setting this to false can improve stability."
        ),
        default=True,
    )
    tokenizer_name: str = Field(
        description=(
            "Huggingface pretrained tokenizer name "
            "upstage opened solar tokenizer in Huggingface. https://huggingface.co/upstage/solar-1-mini-tokenizer"
        ),
        default=SOLAR_TOKENIZERS[DEFAULT_UPSTAGE_MODEL],
    )

    api_key: str = Field(
        default=None, alias="upstage_api_key", description="The Upstage API key."
    )
    api_base: str = Field(
        default="https://api.upstage.ai/v1/solar",
        description="The Upstage API base URL.",
    )
    top_p: Optional[float] = Field(
        default=1,
        gte=0,
        lte=1,
        description="An optional parameter to trigger nucleus sampling.",
    )
    frequency_penalty: Optional[float] = Field(
        default=0,
        gte=-2,
        lte=2,
        description="An optional parameter that controls the model’s tendency to repeat tokens.",
    )
    presence_penalty: Optional[float] = Field(
        default=0,
        gte=-2,
        lte=2,
        description="An optional parameter that adjusts the model’s tendency to include tokens already present in the input or generated text.",
    )
    response_format: Optional[dict] = Field(
        default=None,
        description="An object specifying the format that the model must generate.",
    )

    _client: Optional[SyncOpenAI] = PrivateAttr()
    _aclient: Optional[AsyncOpenAI] = PrivateAttr()
    _http_client: Optional[httpx.Client] = PrivateAttr()

    def __init__(
        self,
        model: str = DEFAULT_UPSTAGE_MODEL,
        temperature: float = DEFAULT_TEMPERATURE,
        max_tokens: Optional[int] = None,
        logprobs: Optional[bool] = None,
        top_logprobs: int = 0,
        additional_kwargs: Dict[str, Any] = None,
        max_retries: int = 3,
        timeout: float = 60.0,
        reuse_client: bool = True,
        tokenizer_name: str = "upstage/solar-1-mini-tokenizer",
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        callback_manager: Optional[CallbackManager] = None,
        default_headers: Optional[Dict[str, str]] = None,
        http_client: Optional[httpx.Client] = None,  # from base class
        system_prompt: Optional[str] = None,
        messages_to_prompt: Optional[Callable[[Sequence[ChatMessage]], str]] = None,
        completion_to_prompt: Optional[Callable[[str], str]] = None,
        pydantic_program_mode: PydanticProgramMode = PydanticProgramMode.DEFAULT,
        output_parser: Optional[BaseOutputParser] = None,
        reasoning_effort: Optional[Literal["low", "medium", "high"]] = None,
        top_p: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        response_format: Optional[dict] = None,
        **kwargs: Any,
    ) -> None:
        if "upstage_api_key" in kwargs:
            api_key = kwargs.pop("upstage_api_key")
        additional_kwargs = additional_kwargs or {}
        api_key, api_base = resolve_upstage_credentials(
            api_key=api_key, api_base=api_base
        )

        default_headers = (default_headers or {}) | {"x-upstage-client": "llamaindex"}

        super().__init__(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            logprobs=logprobs,
            top_logprobs=top_logprobs,
            additional_kwargs=additional_kwargs,
            max_retries=max_retries,
            timeout=timeout,
            reuse_client=reuse_client,
            api_key=api_key,
            api_base=api_base,
            callback_manager=callback_manager,
            default_headers=default_headers,
            http_client=http_client,
            system_prompt=system_prompt,
            messages_to_prompt=messages_to_prompt,
            completion_to_prompt=completion_to_prompt,
            pydantic_program_mode=pydantic_program_mode,
            output_parser=output_parser,
            **kwargs,
        )

        self.tokenizer_name = tokenizer_name
        self._client = None
        self._aclient = None
        self._http_client = http_client
        self.reasoning_effort = reasoning_effort
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.response_format = response_format

    def _get_model_name(self) -> str:
        return self.model

    @classmethod
    def class_name(cls) -> str:
        return "upstage_llm"

    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata(
            context_window=upstage_modelname_to_contextsize(
                modelname=self._get_model_name()
            ),
            num_output=self.max_tokens or -1,
            is_chat_model=is_chat_model(model=self._get_model_name()),
            is_function_calling_model=is_function_calling_model(
                model=self._get_model_name()
            ),
            model_name=self.model,
        )

    @property
    def _tokenizer(self) -> Optional[Tokenizer]:
"""
        Get a Huggingface tokenizer for solar models.
        """
        if SOLAR_TOKENIZERS.get(self.model) != self.tokenizer_name:
            warnings.warn(
                f"You are using a different tokenizer than the one specified in the model. This may cause issues with token counting. Please use {SOLAR_TOKENIZERS[self.model]} as the tokenizer name."
            )
        return Tokenizer.from_pretrained(self.tokenizer_name)

    def get_num_tokens_from_message(self, messages: Sequence[ChatMessage]) -> int:
        tokens_per_message = 5  # <|im_start|>{role}\n{message}<|im_end|>
        tokens_prefix = 1  # <|startoftext|>
        tokens_suffix = 3  # <|im_start|>assistant\n

        num_tokens = 0

        num_tokens += tokens_prefix

        message_dicts = to_openai_message_dicts(messages)
        for message in message_dicts:
            num_tokens += tokens_per_message
            for value in message.values():
                num_tokens += len(
                    self._tokenizer.encode(str(value), add_special_tokens=False)
                )
        num_tokens += tokens_suffix
        return num_tokens

    @llm_retry_decorator
    def _chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse:
        if is_doc_parsing_model(self.model, kwargs):
            document_contents = self._parse_documents(kwargs.pop("file_path"))
            messages.append(ChatMessage(role="user", content=document_contents))
        return super()._chat(messages, **kwargs)

    @llm_retry_decorator
    def _achat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse:
        if is_doc_parsing_model(self.model, kwargs):
            document_contents = self._parse_documents(kwargs.pop("file_path"))
            messages.append(ChatMessage(role="user", content=document_contents))
        return super()._achat(messages, **kwargs)

    @llm_retry_decorator
    def _stream_chat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponseGen:
        if is_doc_parsing_model(self.model, kwargs):
            document_contents = self._parse_documents(kwargs.pop("file_path"))
            messages.append(ChatMessage(role="user", content=document_contents))
        return super()._stream_chat(messages, **kwargs)

    @llm_retry_decorator
    def _astream_chat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponseAsyncGen:
        if is_doc_parsing_model(self.model, kwargs):
            document_contents = self._parse_documents(kwargs.pop("file_path"))
            messages.append(ChatMessage(role="user", content=document_contents))
        return super()._astream_chat(messages, **kwargs)

    def _parse_documents(
        self, file_path: Union[str, Path, List[str], List[Path]]
    ) -> str:
        document_contents = "Documents:\n"

        loader = UpstageDocumentParseReader(
            api_key=self.api_key, output_format="text", coordinates=False
        )
        docs = loader.load_data(file_path)

        if isinstance(file_path, list):
            file_titles = [os.path.basename(path) for path in file_path]
        else:
            file_titles = [os.path.basename(file_path)]

        for i, doc in enumerate(docs):
            file_title = file_titles[min(i, len(file_titles) - 1)]
            document_contents += f"{file_title}:\n{doc.text}\n\n"
        return document_contents

    def _get_model_kwargs(self, **kwargs: Any) -> Dict[str, Any]:
        all_kwargs = super()._get_model_kwargs(**kwargs)
        return all_kwargs | {
            "reasoning_effort": self.reasoning_effort,
            "top_p": self.top_p,
            "frequency_penalty": self.frequency_penalty,
            "presence_penalty": self.presence_penalty,
            "response_format": self.response_format,
        }

```
  
---|---  
options: members: - Upstage
