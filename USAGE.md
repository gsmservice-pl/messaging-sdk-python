<!-- Start SDK Example Usage [usage] -->
### Sending single SMS Message

This example demonstrates simple sending SMS message to a single recipient:

```python
# Synchronous Example
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.sms.send(request=[
        {
            "recipients": [
                "+48999999999",
            ],
            "message": "To jest treść wiadomości",
            "sender": "Bramka SMS",
            "type": 1,
            "unicode": False,
            "flash": False,
            "date_": None,
        },
    ])

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gsmservice_gateway import Client

async def main():

    async with Client(
        bearer="<YOUR API ACCESS TOKEN>",
    ) as client:

        res = await client.outgoing.sms.send_async(request=[
            {
                "recipients": "+48999999999",
                "message": "To jest treść wiadomości",
                "sender": "Bramka SMS",
                "type": 1,
                "unicode": False,
                "flash": False,
                "date_": None,
            },
        ])

        # Handle response
        print(res)

asyncio.run(main())
```

### Sending single MMS Message

This example demonstrates simple sending MMS message to a single recipient:

```python
# Synchronous Example
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.send(request=[
        {
            "recipients": [
                "+48999999999",
            ],
            "subject": "To jest temat wiadomości",
            "message": "To jest treść wiadomości",
            "attachments": [
                "<file_body in base64 format>",
            ],
            "date_": None,
        },
    ])

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from gsmservice_gateway import Client

async def main():

    async with Client(
        bearer="<YOUR API ACCESS TOKEN>",
    ) as client:

        res = await client.outgoing.mms.send_async(request={
            "recipients": {
                "nr": "+48999999999",
                "cid": "my-id-1113",
            },
            "subject": "To jest temat wiadomości",
            "message": "To jest treść wiadomości",
            "attachments": "<file_body in base64 format>",
            "date_": None,
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->