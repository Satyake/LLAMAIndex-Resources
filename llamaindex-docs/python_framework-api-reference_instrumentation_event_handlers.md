# Event handlers
Bases: `BaseModel`
Base callback handler that can be used to track event starts and ends.
Source code in `llama_index_instrumentation/event_handlers/base.py`
```
 9
10
11
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
```
| ```
class BaseEventHandler(BaseModel):
"""Base callback handler that can be used to track event starts and ends."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def class_name(cls) -> str:
"""Class name."""
        return "BaseEventHandler"

    @abstractmethod
    def handle(self, event: BaseEvent, **kwargs: Any) -> Any:
"""Logic for handling event."""

    async def ahandle(self, event: BaseEvent, **kwargs: Any) -> Any:
        return self.handle(event, **kwargs)

```
  
---|---  
##  class_name `classmethod` [#](https://developers.llamaindex.ai/python/framework-api-reference/instrumentation/event_handlers/#llama_index_instrumentation.event_handlers.base.BaseEventHandler.class_name "Permanent link")
```
class_name() -> 

```

Class name.
Source code in `llama_index_instrumentation/event_handlers/base.py`
```
14
15
16
17
```
| ```
@classmethod
def class_name(cls) -> str:
"""Class name."""
    return "BaseEventHandler"

```
  
---|---  
##  handle `abstractmethod` [#](https://developers.llamaindex.ai/python/framework-api-reference/instrumentation/event_handlers/#llama_index_instrumentation.event_handlers.base.BaseEventHandler.handle "Permanent link")
```
handle(event: BaseEvent, **kwargs: ) -> 

```

Logic for handling event.
Source code in `llama_index_instrumentation/event_handlers/base.py`
```
19
20
21
```
| ```
@abstractmethod
def handle(self, event: BaseEvent, **kwargs: Any) -> Any:
"""Logic for handling event."""

```
  
---|---  
options: show_root_heading: true show_root_full_path: false
