<!-- Start SDK Example Usage [usage] -->
### Sending single SMS Message

This example demonstrates simple sending SMS message to a single recipient:

```python
# Synchronous Example
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("GATEWAY_API_BEARER", ""),
)

res = s.outgoing.sms.send(request=[
    {
        "recipients": [
            "+48999999999",
        ],
        "message": "To jest treść wiadomości",
        "sender": "Bramka SMS",
        "type": 1,
        "unicode": True,
        "flash": False,
        "date_": None,
    },
])

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gsmservice_gateway import Client
import os

async def main():
    s = Client(
        bearer=os.getenv("GATEWAY_API_BEARER", ""),
    )
    res = await s.outgoing.sms.send_async(request=[
        {
            "recipients": "+48999999999",
            "message": "To jest treść wiadomości",
            "sender": "Bramka SMS",
            "type": 1,
            "unicode": True,
            "flash": False,
            "date_": None,
        },
    ])
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->