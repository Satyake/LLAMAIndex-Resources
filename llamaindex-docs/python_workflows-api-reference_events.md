# Events
##  Event [#](https://developers.llamaindex.ai/python/workflows-api-reference/events/#workflows.events.Event "Permanent link")
Bases: `DictLikeModel`
Base class for all workflow events.
Events are light-weight, serializable payloads passed between steps. They support both attribute and mapping access to dynamic fields.
Examples:
Subclassing with typed fields:
```
frompydanticimport Field

classCustomEv(Event):
    score: int = Field(ge=0)

e = CustomEv(score=10)
print(e.score)

```

See Also

Source code in `workflows/events.py`
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
```
| ```
classEvent(DictLikeModel):
"""
    Base class for all workflow events.

    Events are light-weight, serializable payloads passed between steps.
    They support both attribute and mapping access to dynamic fields.

    Examples:
        Subclassing with typed fields:

        ```python
        from pydantic import Field

        class CustomEv(Event):
            score: int = Field(ge=0)

        e = CustomEv(score=10)
        print(e.score)
        ```

    See Also:
        - [StartEvent][workflows.events.StartEvent]
        - [StopEvent][workflows.events.StopEvent]
        - [InputRequiredEvent][workflows.events.InputRequiredEvent]
        - [HumanResponseEvent][workflows.events.HumanResponseEvent]
    """

    def__init__(self, **params: Any):
        super().__init__(**params)

```
  
---|---  
##  InputRequiredEvent [#](https://developers.llamaindex.ai/python/workflows-api-reference/events/#workflows.events.InputRequiredEvent "Permanent link")
Bases: 
Emitted when human input is required to proceed.
Automatically written to the event stream if returned from a step.
If returned from a step, it does not need to be consumed by other steps and will pass validation. It's expected that the caller will respond to this event and send back a [HumanResponseEvent](https://developers.llamaindex.ai/python/workflows-api-reference/events/#workflows.events.HumanResponseEvent "HumanResponseEvent").
Use this directly or subclass it.
Typical flow: a step returns `InputRequiredEvent`, callers consume it from the stream and send back a [HumanResponseEvent](https://developers.llamaindex.ai/python/workflows-api-reference/events/#workflows.events.HumanResponseEvent "HumanResponseEvent").
Examples:
```
fromworkflows.eventsimport InputRequiredEvent, HumanResponseEvent

classHITLWorkflow(Workflow):
    @step
    async defmy_step(self, ev: StartEvent) -> InputRequiredEvent:
        return InputRequiredEvent(prefix="What's your name? ")

    @step
    async defmy_step(self, ev: HumanResponseEvent) -> StopEvent:
        return StopEvent(result=ev.response)

```

Source code in `workflows/events.py`
```
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
```
| ```
classInputRequiredEvent(Event):
"""Emitted when human input is required to proceed.

    Automatically written to the event stream if returned from a step.

    If returned from a step, it does not need to be consumed by other steps and will pass validation.
    It's expected that the caller will respond to this event and send back a [HumanResponseEvent][workflows.events.HumanResponseEvent].

    Use this directly or subclass it.

    Typical flow: a step returns `InputRequiredEvent`, callers consume it from
    the stream and send back a [HumanResponseEvent][workflows.events.HumanResponseEvent].

    Examples:
        ```python
        from workflows.events import InputRequiredEvent, HumanResponseEvent

        class HITLWorkflow(Workflow):
            @step
            async def my_step(self, ev: StartEvent) -> InputRequiredEvent:
                return InputRequiredEvent(prefix="What's your name? ")

            @step
            async def my_step(self, ev: HumanResponseEvent) -> StopEvent:
                return StopEvent(result=ev.response)
        ```
    """

```
  
---|---  
##  HumanResponseEvent [#](https://developers.llamaindex.ai/python/workflows-api-reference/events/#workflows.events.HumanResponseEvent "Permanent link")
Bases: 
Carries a human's response for a prior input request.
If consumed by a step and not returned by another, it will still pass validation.
Examples:
```
fromworkflows.eventsimport InputRequiredEvent, HumanResponseEvent

classHITLWorkflow(Workflow):
    @step
    async defmy_step(self, ev: StartEvent) -> InputRequiredEvent:
        return InputRequiredEvent(prefix="What's your name? ")

    @step
    async defmy_step(self, ev: HumanResponseEvent) -> StopEvent:
        return StopEvent(result=ev.response)

```

Source code in `workflows/events.py`
```
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
```
| ```
classHumanResponseEvent(Event):
"""Carries a human's response for a prior input request.

    If consumed by a step and not returned by another, it will still pass validation.

    Examples:
        ```python
        from workflows.events import InputRequiredEvent, HumanResponseEvent

        class HITLWorkflow(Workflow):
            @step
            async def my_step(self, ev: StartEvent) -> InputRequiredEvent:
                return InputRequiredEvent(prefix="What's your name? ")

            @step
            async def my_step(self, ev: HumanResponseEvent) -> StopEvent:
                return StopEvent(result=ev.response)
        ```
    """

```
  
---|---  
##  StartEvent [#](https://developers.llamaindex.ai/python/workflows-api-reference/events/#workflows.events.StartEvent "Permanent link")
Bases: 
Implicit entry event sent to kick off a `Workflow.run()`.
Source code in `workflows/events.py`
```
151
152
```
| ```
classStartEvent(Event):
"""Implicit entry event sent to kick off a `Workflow.run()`."""

```
  
---|---  
##  StopEvent [#](https://developers.llamaindex.ai/python/workflows-api-reference/events/#workflows.events.StopEvent "Permanent link")
Bases: 
Terminal event that signals the workflow has completed.
The `result` property contains the return value of the workflow run. When a custom stop event subclass is used, the workflow result is that event instance itself.
Examples:
```
# default stop event: result holds the value
return StopEvent(result={"answer": 42})

```

Subclassing to provide a custom result:
```python class MyStopEv(StopEvent): pass
@step async def my_step(self, ctx: Context, ev: StartEvent) -> MyStopEv: return MyStopEv(result={"answer": 42})
Source code in `workflows/events.py`
```
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
```
| ```
classStopEvent(Event):
"""Terminal event that signals the workflow has completed.

    The `result` property contains the return value of the workflow run. When a
    custom stop event subclass is used, the workflow result is that event
    instance itself.

    Examples:
        ```python
        # default stop event: result holds the value
        return StopEvent(result={"answer": 42})
        ```

        Subclassing to provide a custom result:

        ```python
        class MyStopEv(StopEvent):
            pass

        @step
        async def my_step(self, ctx: Context, ev: StartEvent) -> MyStopEv:
            return MyStopEv(result={"answer": 42})
    """

    _result: Any = PrivateAttr(default=None)

    def__init__(self, result: Any = None, **kwargs: Any) -> None:
        # forces the user to provide a result
        super().__init__(_result=result, **kwargs)

    def_get_result(self) -> Any:
"""This can be overridden by subclasses to return the desired result."""
        return self._result

    @property
    defresult(self) -> Any:
        return self._get_result()

    @model_serializer(mode="wrap")
    defcustom_model_dump(self, handler: Any) -> dict[str, Any]:
        data = handler(self)
        # include _result in serialization for base StopEvent
        if self._result is not None:
            data["result"] = self._result
        return data

    def__repr__(self) -> str:
        dict_items = {**self._data, **self.model_dump()}
        # Format as key=value pairs
        parts = [f"{k}={v!r}" for k, v in dict_items.items()]
        dict_str = ", ".join(parts)
        return f"{self.__class__.__name__}({dict_str})"

    def__str__(self) -> str:
        return str(self._result)

```
  
---|---
