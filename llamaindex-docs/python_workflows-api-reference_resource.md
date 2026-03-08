# Resource
Declare a resource to inject into step functions.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`factory` |  `Callable[..., T]` |  Function returning the resource instance. May be async. |  _required_  
`cache` |  `bool` |  If True, reuse the produced resource across steps. Defaults to True. |  `True`  
Returns:
Type | Description  
---|---  
`_Resource[T]` |  _Resource[T]: A resource descriptor to be used in `typing.Annotated`.  
Examples:
```
fromtypingimport Annotated
fromworkflows.resourceimport Resource

defget_memory(**kwargs) -> Memory:
    return Memory.from_defaults("user123", token_limit=60000)

classMyWorkflow(Workflow):
    @step
    async deffirst(
        self,
        ev: StartEvent,
        memory: Annotated[Memory, Resource(get_memory)],
    ) -> StopEvent:
        await memory.aput(...)
        return StopEvent(result="ok")

```

Source code in `workflows/resource.py`
```
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
```
| ```
defResource(factory: Callable[..., T], cache: bool = True) -> _Resource[T]:
"""Declare a resource to inject into step functions.

    Args:
        factory (Callable[..., T]): Function returning the resource instance. May be async.
        cache (bool): If True, reuse the produced resource across steps. Defaults to True.

    Returns:
        _Resource[T]: A resource descriptor to be used in `typing.Annotated`.

    Examples:
        ```python
        from typing import Annotated
        from workflows.resource import Resource

        def get_memory(**kwargs) -> Memory:
            return Memory.from_defaults("user123", token_limit=60000)

        class MyWorkflow(Workflow):
            @step
            async def first(
                self,
                ev: StartEvent,
                memory: Annotated[Memory, Resource(get_memory)],
            ) -> StopEvent:
                await memory.aput(...)
                return StopEvent(result="ok")
        ```
    """
    return _Resource(factory, cache)

```
  
---|---
