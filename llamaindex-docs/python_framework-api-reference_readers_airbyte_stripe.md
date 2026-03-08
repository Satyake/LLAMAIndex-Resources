# Airbyte stripe
##  AirbyteStripeReader [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/airbyte_stripe/#llama_index.readers.airbyte_stripe.AirbyteStripeReader "Permanent link")
Bases: 
AirbyteStripeReader reader.
Retrieve documents from Stripe
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`config` |  `Mapping[str, Any]` |  The config object for the stripe source. |  _required_  
Source code in `llama_index/readers/airbyte_stripe/base.py`
```
 6
 7
 8
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
25
26
27
28
29
```
| ```
class AirbyteStripeReader(AirbyteCDKReader):
"""
    AirbyteStripeReader reader.

    Retrieve documents from Stripe

    Args:
        config: The config object for the stripe source.

    """

    def __init__(
        self,
        config: Mapping[str, Any],
        record_handler: Optional[RecordHandler] = None,
    ) -> None:
"""Initialize with parameters."""
        import source_stripe

        super().__init__(
            source_class=source_stripe.SourceStripe,
            config=config,
            record_handler=record_handler,
        )

```
  
---|---  
options: members: - AirbyteStripeReader
