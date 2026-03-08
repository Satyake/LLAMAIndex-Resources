# Span types
Bases: `BaseModel`
Base data class representing a span.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`id_` |  Id of span. |  `'793e18bc-9c16-4e7b-82f7-22cddf3259ca'`  
`parent_id` |  `str | None` |  Id of parent span. |  `None`  
`tags` |  `Dict[str, Any]`  
Source code in `llama_index_instrumentation/span/base.py`
```
 7
 8
 9
10
11
12
13
```
| ```
class BaseSpan(BaseModel):
"""Base data class representing a span."""

    model_config = ConfigDict(arbitrary_types_allowed=True)
    id_: str = Field(default_factory=lambda: str(uuid4()), description="Id of span.")
    parent_id: Optional[str] = Field(default=None, description="Id of parent span.")
    tags: Dict[str, Any] = Field(default={})

```
  
---|---  
options: show_root_heading: true show_root_full_path: false
