# Bedrock agentcore
##  AgentCoreMemory [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory "Permanent link")
Bases: `BaseAgentCoreMemory`
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
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
```
| ```
class AgentCoreMemory(BaseAgentCoreMemory):
    search_msg_limit: int = Field(
        default=5,
        description="Limit of chat history messages to use for context in search API",
    )
    insert_method: InsertMethod = Field(
        default=InsertMethod.SYSTEM,
        description="Whether to inject memory blocks into a system message or into the latest user message.",
    )

    _context: AgentCoreMemoryContext = PrivateAttr()

    def __init__(
        self,
        context: AgentCoreMemoryContext,
        # TODO: add support for InsertMethod.USER. for now default to InsertMethod.SYSTEM
        # insert_method: InsertMethod = InsertMethod.SYSTEM,
        profile_name: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        region_name: Optional[str] = None,
        api_version: Optional[str] = None,
        use_ssl: bool = True,
        verify: Optional[Union[bool, str]] = None,
        endpoint_url: Optional[str] = None,
        botocore_session: Optional[Any] = None,
        client: Optional[Any] = None,
        timeout: Optional[float] = 60.0,
        max_retries: Optional[int] = 10,
        botocore_config: Optional[Any] = None,
    ) -> None:
        boto3_user_agent_identifier = "x-client-framework:llama_index"

        session_kwargs = {
            "profile_name": profile_name,
            "region_name": region_name,
            "aws_access_key_id": aws_access_key_id,
            "aws_secret_access_key": aws_secret_access_key,
            "aws_session_token": aws_session_token,
            "botocore_session": botocore_session,
        }
        self._config = (
            Config(
                retries={"max_attempts": max_retries, "mode": "standard"},
                connect_timeout=timeout,
                read_timeout=timeout,
                user_agent_extra=boto3_user_agent_identifier,
            )
            if botocore_config is None
            else botocore_config
        )

        self._boto_client_kwargs = {
            "api_version": api_version,
            "use_ssl": use_ssl,
            "verify": verify,
            "endpoint_url": endpoint_url,
        }

        try:
            self._config = (
                Config(
                    retries={"max_attempts": max_retries, "mode": "standard"},
                    connect_timeout=timeout,
                    read_timeout=timeout,
                    user_agent_extra=boto3_user_agent_identifier,
                )
                if botocore_config is None
                else botocore_config
            )
            session = boto3.Session(**session_kwargs)
        except ImportError:
            raise ImportError(
                "boto3  package not found, install with pip install boto3"
            )
        session = boto3.Session(**session_kwargs)

        if client is not None:
            self._client = client
        else:
            self._client = session.client(
                "bedrock-agentcore",
                config=self._config,
                **self._boto_client_kwargs,
            )
        self._client._serializer._serializer._serialize_type_timestamp = (
            self._serialize_timestamp_with_microseconds
        )
        super().__init__(self._client)

        self._context = context

    @model_serializer
    def serialize_memory(self) -> Dict[str, Any]:
        # leaving out the two keys since they are causing serialization/deserialization problems
        return {
            "search_msg_limit": self.search_msg_limit,
        }

    @classmethod
    def class_name(cls) -> str:
"""Class name."""
        return "AgentCoreMemory"

    @classmethod
    def from_defaults(cls, **kwargs: Any) -> "AgentCoreMemory":
        raise NotImplementedError("Use either from_client or from_config")

    def _serialize_timestamp_with_microseconds(self, serialized, value, shape, name):
        original_serialize_timestamp = (
            self._client._serializer._serializer._serialize_type_timestamp
        )
        if isinstance(value, datetime):
            serialized[name] = value.timestamp()  # Float with microseconds
        else:
            original_serialize_timestamp(serialized, value, shape, name)

    def _add_msgs_to_client_memory(self, messages: List[ChatMessage]) -> None:
"""Add new user and assistant messages to client memory."""
        self.create_event(
            messages=messages,
            memory_id=self._context.memory_id,
            actor_id=self._context.actor_id,
            session_id=self._context.session_id,
        )

    async def aget(self, input: Optional[str] = None) -> List[ChatMessage]:
        # Get list of events to represent as the chat history. Use this as the query for the memory records. If an input is provided, then also append it to the list of events
        messages = self.list_events(
            memory_id=self._context.memory_id,
            session_id=self._context.session_id,
            actor_id=self._context.actor_id,
        )
        input = convert_messages_to_string(messages, input)

        search_criteria = {"searchQuery": input[:10000]}
        if self._context.memory_strategy_id is not None:
            search_criteria["memoryStrategyId"] = self._context.memory_strategy_id

        memory_records = self.retrieve_memories(
            memory_id=self._context.memory_id,
            namespace=self._context.namespace,
            search_criteria=search_criteria,
        )

        if self.insert_method == InsertMethod.SYSTEM:
            system_message = convert_memory_to_system_message(memory_records)
            # If system message is present
            if len(messages)  0 and messages[0].role == MessageRole.SYSTEM:
                assert messages[0].content is not None
                system_message = convert_memory_to_system_message(
                    response=memory_records, existing_system_message=messages[0]
                )
            messages.insert(0, system_message)
        elif self.insert_method == InsertMethod.USER:
            # Find the latest user message
            session_idx = next(
                (
                    i
                    for i, msg in enumerate(reversed(messages))
                    if msg.role == MessageRole.USER
                ),
                None,
            )

            memory_content = convert_memory_to_user_message(memory_records)

            if session_idx is not None:
                # Get actual index (since we enumerated in reverse)
                actual_idx = len(messages) - 1 - session_idx
                # Update existing user message since many LLMs have issues with consecutive user msgs
                final_user_content = (
                    memory_content.content + messages[actual_idx].content
                )
                messages[actual_idx] = ChatMessage(
                    content=final_user_content, role=MessageRole.USER
                )
                messages[actual_idx].blocks = [
                    *memory_content.blocks,
                    *messages[actual_idx].blocks,
                ]
            else:
                messages.append(
                    ChatMessage(content=memory_content, role=MessageRole.USER)
                )

        return messages

    async def aget_all(self) -> List[ChatMessage]:
        return self.list_events(
            memory_id=self._context.memory_id,
            session_id=self._context.session_id,
            actor_id=self._context.actor_id,
        )

    async def aput(self, message: ChatMessage) -> None:
"""Add a message to the chat store and process waterfall logic if needed."""
        # Add the message to the chat store
        self._add_msgs_to_client_memory([message])

    async def aput_messages(self, messages: List[ChatMessage]) -> None:
"""Add a list of messages to the chat store and process waterfall logic if needed."""
        # Add the messages to the chat store
        self._add_msgs_to_client_memory(messages)

    async def aset(self, messages: List[ChatMessage]) -> None:
        initial_chat_len = len(self.get_all())
        # Insert only new chat messages
        self._add_msgs_to_client_memory(messages[initial_chat_len:])

    # ---- Sync method wrappers ----
    def get(self, input: Optional[str] = None) -> List[ChatMessage]:
"""Get chat history."""
        return asyncio_run(self.aget(input=input))

    def get_all(self) -> List[ChatMessage]:
"""Returns all chat history."""
        return asyncio_run(self.aget_all())

    def put(self, message: ChatMessage) -> None:
"""Add message to chat history and client memory."""
        return asyncio_run(self.aput(message))

    def put_messages(self, messages: List[ChatMessage]) -> None:
        return asyncio_run(self.aput_messages(messages))

    def set(self, messages: List[ChatMessage]) -> None:
"""Set chat history and add new messages to client memory."""
        return asyncio_run(self.aset(messages))

    def reset(self) -> None:
"""Only reset chat history."""
        # Our guidance has been to not delete memory resources in AgentCore on behalf of the customer. If this changes in the future, then we can implement this method.

    def get_context(self) -> AgentCoreMemoryContext:
        return self._context.get_context()

```
  
---|---  
###  class_name `classmethod` [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory.class_name "Permanent link")
```
class_name() -> 

```

Class name.
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
245
246
247
248
```
| ```
@classmethod
def class_name(cls) -> str:
"""Class name."""
    return "AgentCoreMemory"

```
  
---|---  
###  aput `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory.aput "Permanent link")
```
aput(message: ) -> None

```

Add a message to the chat store and process waterfall logic if needed.
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
341
342
343
344
```
| ```
async def aput(self, message: ChatMessage) -> None:
"""Add a message to the chat store and process waterfall logic if needed."""
    # Add the message to the chat store
    self._add_msgs_to_client_memory([message])

```
  
---|---  
###  aput_messages `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory.aput_messages "Permanent link")
```
aput_messages(messages: []) -> None

```

Add a list of messages to the chat store and process waterfall logic if needed.
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
346
347
348
349
```
| ```
async def aput_messages(self, messages: List[ChatMessage]) -> None:
"""Add a list of messages to the chat store and process waterfall logic if needed."""
    # Add the messages to the chat store
    self._add_msgs_to_client_memory(messages)

```
  
---|---  
###  get [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory.get "Permanent link")
```
get(input: Optional[] = None) -> []

```

Get chat history.
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
357
358
359
```
| ```
def get(self, input: Optional[str] = None) -> List[ChatMessage]:
"""Get chat history."""
    return asyncio_run(self.aget(input=input))

```
  
---|---  
###  get_all [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory.get_all "Permanent link")
```
get_all() -> []

```

Returns all chat history.
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
361
362
363
```
| ```
def get_all(self) -> List[ChatMessage]:
"""Returns all chat history."""
    return asyncio_run(self.aget_all())

```
  
---|---  
###  put [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory.put "Permanent link")
```
put(message: ) -> None

```

Add message to chat history and client memory.
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
365
366
367
```
| ```
def put(self, message: ChatMessage) -> None:
"""Add message to chat history and client memory."""
    return asyncio_run(self.aput(message))

```
  
---|---  
###  set [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory.set "Permanent link")
```
set(messages: []) -> None

```

Set chat history and add new messages to client memory.
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
372
373
374
```
| ```
def set(self, messages: List[ChatMessage]) -> None:
"""Set chat history and add new messages to client memory."""
    return asyncio_run(self.aset(messages))

```
  
---|---  
###  reset [#](https://developers.llamaindex.ai/python/framework-api-reference/memory/bedrock_agentcore/#llama_index.memory.bedrock_agentcore.AgentCoreMemory.reset "Permanent link")
```
reset() -> None

```

Only reset chat history.
Source code in `llama_index/memory/bedrock_agentcore/base.py`
```
376
377
```
| ```
def reset(self) -> None:
"""Only reset chat history."""

```
  
---|---  
options: members: - AgentCoreMemory
