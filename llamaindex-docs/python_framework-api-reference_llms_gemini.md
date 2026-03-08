# Gemini
##  Gemini [#](https://developers.llamaindex.ai/python/framework-api-reference/llms/gemini/#llama_index.llms.gemini.Gemini "Permanent link")
Bases: `FunctionCallingLLM`
Gemini LLM.
Examples:
`pip install llama-index-llms-gemini`
```
from llama_index.llms.gemini import Gemini

llm = Gemini(model="models/gemini-ultra", api_key="YOUR_API_KEY")
resp = llm.complete("Write a poem about a magic backpack")
print(resp)

```

Source code in `llama_index/llms/gemini/base.py`
```
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
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
```
| ```
@deprecated.deprecated(
    reason=(
        "Should use `llama-index-llms-google-genai` instead, using Google's latest unified SDK. "
        "See: https://docs.llamaindex.ai/en/stable/examples/llm/google_genai/"
    )
)
class Gemini(FunctionCallingLLM):
"""
    Gemini LLM.

    Examples:
        `pip install llama-index-llms-gemini`

        ```python
        from llama_index.llms.gemini import Gemini

        llm = Gemini(model="models/gemini-ultra", api_key="YOUR_API_KEY")
        resp = llm.complete("Write a poem about a magic backpack")
        print(resp)
        ```

    """

    model: str = Field(default=GEMINI_MODELS[0], description="The Gemini model to use.")
    temperature: float = Field(
        default=DEFAULT_TEMPERATURE,
        description="The temperature to use during generation.",
        ge=0.0,
        le=2.0,
    )
    max_tokens: int = Field(
        default=DEFAULT_NUM_OUTPUTS,
        description="The number of tokens to generate.",
        gt=0,
    )
    generate_kwargs: dict = Field(
        default_factory=dict, description="Kwargs for generation."
    )

    _model: genai.GenerativeModel = PrivateAttr()
    _model_meta: genai.types.Model = PrivateAttr()
    _request_options: Optional[genai.types.RequestOptions] = PrivateAttr()

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = GEMINI_MODELS[0],
        temperature: float = DEFAULT_TEMPERATURE,
        max_tokens: Optional[int] = None,
        generation_config: Optional[genai.types.GenerationConfigDict] = None,
        safety_settings: Optional[genai.types.SafetySettingDict] = None,
        callback_manager: Optional[CallbackManager] = None,
        api_base: Optional[str] = None,
        transport: Optional[str] = None,
        model_name: Optional[str] = None,
        default_headers: Optional[Dict[str, str]] = None,
        request_options: Optional[genai.types.RequestOptions] = None,
        **generate_kwargs: Any,
    ):
"""Creates a new Gemini model interface."""
        if model_name is not None:
            warnings.warn(
                "model_name is deprecated, please use model instead",
                DeprecationWarning,
            )

            model = model_name

        # API keys are optional. The API can be authorised via OAuth (detected
        # environmentally) or by the GOOGLE_API_KEY environment variable.
        config_params: Dict[str, Any] = {
            "api_key": api_key or os.getenv("GOOGLE_API_KEY"),
        }
        if api_base:
            config_params["client_options"] = {"api_endpoint": api_base}
        if transport:
            config_params["transport"] = transport
        if default_headers:
            default_metadata = []
            for key, value in default_headers.items():
                default_metadata.append((key, value))
            # `default_metadata` contains (key, value) pairs that will be sent with every request.
            # When using `transport="rest"`, these will be sent as HTTP headers.
            config_params["default_metadata"] = default_metadata
        # transport: A string, one of: [`rest`, `grpc`, `grpc_asyncio`].
        genai.configure(**config_params)

        base_gen_config = generation_config if generation_config else {}
        # Explicitly passed args take precedence over the generation_config.
        final_gen_config = cast(
            generation_types.GenerationConfigDict,
            {"temperature": temperature, **base_gen_config},
        )

        model_meta = genai.get_model(model)

        genai_model = genai.GenerativeModel(
            model_name=model,
            generation_config=final_gen_config,
            safety_settings=safety_settings,
        )

        supported_methods = model_meta.supported_generation_methods
        if "generateContent" not in supported_methods:
            raise ValueError(
                f"Model {model} does not support content generation, only "
                f"{supported_methods}."
            )

        if not max_tokens:
            max_tokens = model_meta.output_token_limit
        else:
            max_tokens = min(max_tokens, model_meta.output_token_limit)

        super().__init__(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            generate_kwargs=generate_kwargs,
            callback_manager=callback_manager,
        )

        self._model_meta = model_meta
        self._model = genai_model
        self._request_options = request_options
        self._is_function_call_model = is_function_calling_model(model)

    @classmethod
    def class_name(cls) -> str:
        return "Gemini_LLM"

    @property
    def metadata(self) -> LLMMetadata:
        total_tokens = self._model_meta.input_token_limit + self.max_tokens
        return LLMMetadata(
            context_window=total_tokens,
            num_output=self.max_tokens,
            model_name=self.model,
            is_chat_model=True,
            # All gemini models support function calling
            is_function_calling_model=self._is_function_call_model,
        )

    @llm_completion_callback()
    def complete(
        self, prompt: str, formatted: bool = False, **kwargs: Any
    ) -> CompletionResponse:
        request_options = self._request_options or kwargs.pop("request_options", None)
        result = self._model.generate_content(
            prompt, request_options=request_options, **kwargs
        )
        return completion_from_gemini_response(result)

    @llm_completion_callback()
    async def acomplete(
        self, prompt: str, formatted: bool = False, **kwargs: Any
    ) -> CompletionResponse:
        request_options = self._request_options or kwargs.pop("request_options", None)
        result = await self._model.generate_content_async(
            prompt, request_options=request_options, **kwargs
        )
        return completion_from_gemini_response(result)

    @llm_completion_callback()
    def stream_complete(
        self, prompt: str, formatted: bool = False, **kwargs: Any
    ) -> CompletionResponseGen:
        request_options = self._request_options or kwargs.pop("request_options", None)

        def gen():
            text = ""
            it = self._model.generate_content(
                prompt, stream=True, request_options=request_options, **kwargs
            )
            for r in it:
                delta = r.text or ""
                text += delta
                yield completion_from_gemini_response(r, text=text, delta=delta)

        return gen()

    @llm_completion_callback()
    def astream_complete(
        self, prompt: str, formatted: bool = False, **kwargs: Any
    ) -> CompletionResponseAsyncGen:
        request_options = self._request_options or kwargs.pop("request_options", None)

        async def gen():
            text = ""
            it = await self._model.generate_content_async(
                prompt, stream=True, request_options=request_options, **kwargs
            )
            async for r in it:
                delta = r.text or ""
                text += delta
                yield completion_from_gemini_response(r, text=text, delta=delta)

        return gen()

    @llm_chat_callback()
    def chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse:
        request_options = self._request_options or kwargs.pop("request_options", None)
        merged_messages = merge_neighboring_same_role_messages(messages)
        *history, next_msg = map(chat_message_to_gemini, merged_messages)
        chat = self._model.start_chat(history=history)
        response = chat.send_message(
            next_msg,
            request_options=request_options,
            **kwargs,
        )
        return chat_from_gemini_response(response)

    @llm_chat_callback()
    async def achat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponse:
        request_options = self._request_options or kwargs.pop("request_options", None)
        merged_messages = merge_neighboring_same_role_messages(messages)
        *history, next_msg = map(chat_message_to_gemini, merged_messages)
        chat = self._model.start_chat(history=history)
        response = await chat.send_message_async(
            next_msg, request_options=request_options, **kwargs
        )
        return chat_from_gemini_response(response)

    @llm_chat_callback()
    def stream_chat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponseGen:
        request_options = self._request_options or kwargs.pop("request_options", None)
        merged_messages = merge_neighboring_same_role_messages(messages)
        *history, next_msg = map(chat_message_to_gemini, merged_messages)
        chat = self._model.start_chat(history=history)
        response = chat.send_message(
            next_msg, stream=True, request_options=request_options, **kwargs
        )

        def gen() -> ChatResponseGen:
            content = ""
            existing_tool_calls = []
            for r in response:
                top_candidate = r.candidates[0]
                content_delta = top_candidate.content.parts[0].text
                content += content_delta
                llama_resp = chat_from_gemini_response(r)
                existing_tool_calls.extend(
                    llama_resp.message.additional_kwargs.get("tool_calls", [])
                )
                llama_resp.delta = content_delta
                llama_resp.message.content = content
                llama_resp.message.additional_kwargs["tool_calls"] = existing_tool_calls
                yield llama_resp

        return gen()

    @llm_chat_callback()
    async def astream_chat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponseAsyncGen:
        request_options = self._request_options or kwargs.pop("request_options", None)
        merged_messages = merge_neighboring_same_role_messages(messages)
        *history, next_msg = map(chat_message_to_gemini, merged_messages)
        chat = self._model.start_chat(history=history)
        response = await chat.send_message_async(
            next_msg, stream=True, request_options=request_options, **kwargs
        )

        async def gen() -> ChatResponseAsyncGen:
            content = ""
            existing_tool_calls = []
            async for r in response:
                top_candidate = r.candidates[0]
                content_delta = top_candidate.content.parts[0].text
                content += content_delta
                llama_resp = chat_from_gemini_response(r)
                existing_tool_calls.extend(
                    llama_resp.message.additional_kwargs.get("tool_calls", [])
                )
                llama_resp.delta = content_delta
                llama_resp.message.content = content
                llama_resp.message.additional_kwargs["tool_calls"] = existing_tool_calls
                yield llama_resp

        return gen()

    def _to_function_calling_config(
        self, tool_required: bool, tool_choice: Optional[str]
    ) -> dict:
        if tool_choice and not isinstance(tool_choice, str):
            raise ValueError("Gemini only supports string tool_choices")
        tool_choice = tool_choice or ("any" if tool_required else "auto")

        if tool_choice == "auto":
            tool_mode = FunctionCallingMode.AUTO
        elif tool_choice == "none":
            tool_mode = FunctionCallingMode.NONE
        else:
            tool_mode = FunctionCallingMode.ANY

        allowed_function_names = None
        if tool_choice not in ["auto", "none", "any"]:
            allowed_function_names = [tool_choice]
        return {
            "mode": tool_mode,
            **(
                {"allowed_function_names": allowed_function_names}
                if allowed_function_names
                else {}
            ),
        }

    def _prepare_chat_with_tools(
        self,
        tools: Sequence["BaseTool"],
        user_msg: Optional[Union[str, ChatMessage]] = None,
        chat_history: Optional[List[ChatMessage]] = None,
        verbose: bool = False,
        allow_parallel_tool_calls: bool = False,
        tool_required: bool = False,
        tool_choice: Optional[Union[str, dict]] = None,
        strict: Optional[bool] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
"""Predict and call the tool."""
        tool_config = {
            "function_calling_config": self._to_function_calling_config(
                tool_required, tool_choice
            ),
        }

        tool_declarations = []
        for tool in tools:
            descriptions = {}
            for param_name, param_schema in tool.metadata.get_parameters_dict()[
                "properties"
            ].items():
                param_description = param_schema.get("description", None)
                if param_description:
                    descriptions[param_name] = param_description

            tool.metadata.fn_schema.__doc__ = tool.metadata.description
            tool_declarations.append(
                FunctionDeclaration.from_function(tool.metadata.fn_schema, descriptions)
            )

        if isinstance(user_msg, str):
            user_msg = ChatMessage(role=MessageRole.USER, content=user_msg)

        messages = chat_history or []
        if user_msg:
            messages.append(user_msg)

        return {
            "messages": messages,
            "tools": (
                ToolDict(function_declarations=tool_declarations)
                if tool_declarations
                else None
            ),
            "tool_config": tool_config,
            **kwargs,
        }

    def get_tool_calls_from_response(
        self,
        response: ChatResponse,
        error_on_no_tool_call: bool = True,
        **kwargs: Any,
    ) -> List[ToolSelection]:
"""Predict and call the tool."""
        tool_calls = response.message.additional_kwargs.get("tool_calls", [])

        if len(tool_calls)  1:
            if error_on_no_tool_call:
                raise ValueError(
                    f"Expected at least one tool call, but got {len(tool_calls)} tool calls."
                )
            else:
                return []

        tool_selections = []
        for tool_call in tool_calls:
            if not isinstance(tool_call, genai.protos.FunctionCall):
                raise ValueError("Invalid tool_call object")

            tool_selections.append(
                ToolSelection(
                    tool_id=str(uuid.uuid4()),
                    tool_name=tool_call.name,
                    tool_kwargs=dict(tool_call.args),
                )
            )

        return tool_selections

    @dispatcher.span
    def structured_predict(
        self,
        output_cls: Type[Model],
        prompt: PromptTemplate,
        llm_kwargs: Optional[Dict[str, Any]] = None,
        **prompt_args: Any,
    ) -> Model:
"""Structured predict."""
        llm_kwargs = llm_kwargs or {}

        if self._is_function_call_model:
            llm_kwargs["tool_required"] = True
        # by default structured prediction uses function calling to extract structured outputs
        # here we force tool_choice to be required
        return super().structured_predict(
            output_cls, prompt, llm_kwargs=llm_kwargs, **prompt_args
        )

    @dispatcher.span
    async def astructured_predict(
        self,
        output_cls: Type[Model],
        prompt: PromptTemplate,
        llm_kwargs: Optional[Dict[str, Any]] = None,
        **prompt_args: Any,
    ) -> Model:
"""Structured predict."""
        llm_kwargs = llm_kwargs or {}

        if self._is_function_call_model:
            llm_kwargs["tool_required"] = True
        # by default structured prediction uses function calling to extract structured outputs
        # here we force tool_choice to be required
        return await super().astructured_predict(
            output_cls, prompt, llm_kwargs=llm_kwargs, **prompt_args
        )

    @dispatcher.span
    def stream_structured_predict(
        self,
        output_cls: Type[Model],
        prompt: PromptTemplate,
        llm_kwargs: Optional[Dict[str, Any]] = None,
        **prompt_args: Any,
    ) -> Generator[Union[Model, FlexibleModel], None, None]:
"""Stream structured predict."""
        llm_kwargs = llm_kwargs or {}

        if self._is_function_call_model:
            llm_kwargs["tool_required"] = True
        # by default structured prediction uses function calling to extract structured outputs
        # here we force tool_choice to be required
        return super().stream_structured_predict(
            output_cls, prompt, llm_kwargs=llm_kwargs, **prompt_args
        )

    @dispatcher.span
    async def astream_structured_predict(
        self,
        output_cls: Type[Model],
        prompt: PromptTemplate,
        llm_kwargs: Optional[Dict[str, Any]] = None,
        **prompt_args: Any,
    ) -> AsyncGenerator[Union[Model, FlexibleModel], None]:
"""Stream structured predict."""
        llm_kwargs = llm_kwargs or {}

        if self._is_function_call_model:
            llm_kwargs["tool_required"] = True
        # by default structured prediction uses function calling to extract structured outputs
        # here we force tool_choice to be required
        return await super().astream_structured_predict(
            output_cls, prompt, llm_kwargs=llm_kwargs, **prompt_args
        )

```
  
---|---  
###  get_tool_calls_from_response [#](https://developers.llamaindex.ai/python/framework-api-reference/llms/gemini/#llama_index.llms.gemini.Gemini.get_tool_calls_from_response "Permanent link")
```
get_tool_calls_from_response(response: , error_on_no_tool_call:  = True, **kwargs: ) -> []

```

Predict and call the tool.
Source code in `llama_index/llms/gemini/base.py`
```
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
```
| ```
def get_tool_calls_from_response(
    self,
    response: ChatResponse,
    error_on_no_tool_call: bool = True,
    **kwargs: Any,
) -> List[ToolSelection]:
"""Predict and call the tool."""
    tool_calls = response.message.additional_kwargs.get("tool_calls", [])

    if len(tool_calls)  1:
        if error_on_no_tool_call:
            raise ValueError(
                f"Expected at least one tool call, but got {len(tool_calls)} tool calls."
            )
        else:
            return []

    tool_selections = []
    for tool_call in tool_calls:
        if not isinstance(tool_call, genai.protos.FunctionCall):
            raise ValueError("Invalid tool_call object")

        tool_selections.append(
            ToolSelection(
                tool_id=str(uuid.uuid4()),
                tool_name=tool_call.name,
                tool_kwargs=dict(tool_call.args),
            )
        )

    return tool_selections

```
  
---|---  
###  structured_predict [#](https://developers.llamaindex.ai/python/framework-api-reference/llms/gemini/#llama_index.llms.gemini.Gemini.structured_predict "Permanent link")
```
structured_predict(output_cls: [], prompt: , llm_kwargs: Optional[[, ]] = None, **prompt_args: ) -> 

```

Structured predict.
Source code in `llama_index/llms/gemini/base.py`
```
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
```
| ```
@dispatcher.span
def structured_predict(
    self,
    output_cls: Type[Model],
    prompt: PromptTemplate,
    llm_kwargs: Optional[Dict[str, Any]] = None,
    **prompt_args: Any,
) -> Model:
"""Structured predict."""
    llm_kwargs = llm_kwargs or {}

    if self._is_function_call_model:
        llm_kwargs["tool_required"] = True
    # by default structured prediction uses function calling to extract structured outputs
    # here we force tool_choice to be required
    return super().structured_predict(
        output_cls, prompt, llm_kwargs=llm_kwargs, **prompt_args
    )

```
  
---|---  
###  astructured_predict `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/llms/gemini/#llama_index.llms.gemini.Gemini.astructured_predict "Permanent link")
```
astructured_predict(output_cls: [], prompt: , llm_kwargs: Optional[[, ]] = None, **prompt_args: ) -> 

```

Structured predict.
Source code in `llama_index/llms/gemini/base.py`
```
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
```
| ```
@dispatcher.span
async def astructured_predict(
    self,
    output_cls: Type[Model],
    prompt: PromptTemplate,
    llm_kwargs: Optional[Dict[str, Any]] = None,
    **prompt_args: Any,
) -> Model:
"""Structured predict."""
    llm_kwargs = llm_kwargs or {}

    if self._is_function_call_model:
        llm_kwargs["tool_required"] = True
    # by default structured prediction uses function calling to extract structured outputs
    # here we force tool_choice to be required
    return await super().astructured_predict(
        output_cls, prompt, llm_kwargs=llm_kwargs, **prompt_args
    )

```
  
---|---  
###  stream_structured_predict [#](https://developers.llamaindex.ai/python/framework-api-reference/llms/gemini/#llama_index.llms.gemini.Gemini.stream_structured_predict "Permanent link")
```
stream_structured_predict(output_cls: [], prompt: , llm_kwargs: Optional[[, ]] = None, **prompt_args: ) -> Generator[Union[, FlexibleModel], None, None]

```

Stream structured predict.
Source code in `llama_index/llms/gemini/base.py`
```
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
```
| ```
@dispatcher.span
def stream_structured_predict(
    self,
    output_cls: Type[Model],
    prompt: PromptTemplate,
    llm_kwargs: Optional[Dict[str, Any]] = None,
    **prompt_args: Any,
) -> Generator[Union[Model, FlexibleModel], None, None]:
"""Stream structured predict."""
    llm_kwargs = llm_kwargs or {}

    if self._is_function_call_model:
        llm_kwargs["tool_required"] = True
    # by default structured prediction uses function calling to extract structured outputs
    # here we force tool_choice to be required
    return super().stream_structured_predict(
        output_cls, prompt, llm_kwargs=llm_kwargs, **prompt_args
    )

```
  
---|---  
###  astream_structured_predict `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/llms/gemini/#llama_index.llms.gemini.Gemini.astream_structured_predict "Permanent link")
```
astream_structured_predict(output_cls: [], prompt: , llm_kwargs: Optional[[, ]] = None, **prompt_args: ) -> AsyncGenerator[Union[, FlexibleModel], None]

```

Stream structured predict.
Source code in `llama_index/llms/gemini/base.py`
```
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
```
| ```
@dispatcher.span
async def astream_structured_predict(
    self,
    output_cls: Type[Model],
    prompt: PromptTemplate,
    llm_kwargs: Optional[Dict[str, Any]] = None,
    **prompt_args: Any,
) -> AsyncGenerator[Union[Model, FlexibleModel], None]:
"""Stream structured predict."""
    llm_kwargs = llm_kwargs or {}

    if self._is_function_call_model:
        llm_kwargs["tool_required"] = True
    # by default structured prediction uses function calling to extract structured outputs
    # here we force tool_choice to be required
    return await super().astream_structured_predict(
        output_cls, prompt, llm_kwargs=llm_kwargs, **prompt_args
    )

```
  
---|---  
options: members: - Gemini
