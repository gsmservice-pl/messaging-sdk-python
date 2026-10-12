# Outgoing.Mms

## Overview

### Available Operations

* [get_price](#get_price) - Check the price of MMS Messages
* [send](#send) - Send MMS Messages

## get_price

Check the price of single or multiple MMS messages at the same time before sending them. You can pass as a `request` named parameter a single `MmsMessage` (for single message) or `List[MmsMessage]` (for multiple messages). Each `MmsMessage` object has several properties, describing message parameters such as recipient phone number, content of the message, attachments, etc.
The method will accept maximum **50** messages in one call.

As a successful result a `GetMmsPriceResponse` object will be returned with `result` property of type `List[Price]` containing a `Price` objects, one object per each single message. You should check the `error` property of each `Price` object to make sure which messages were priced successfully and which finished with an error. Successfully priced messages will have `null` value of `error` property.

`GetSmsPriceResponse` object will include also `headers` property with `X-Success-Count` (a count of messages which were processed successfully) and `X-Error-Count` (count of messages which were rejected) elements.

### Example Usage: bulk

<!-- UsageSnippet language="python" operationID="getMmsPrice" method="post" path="/messages/mms/price" example="bulk" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.get_price(request=[
        {
            "recipients": "+48999999999",
            "subject": "This is a subject of the first message",
            "message": "This is first MMS message content",
            "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
            "date_": None,
        },
        {
            "recipients": "+48999888777",
            "subject": "This is a subject of the second message",
            "message": "This is second MMS message content",
            "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
            "date_": None,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: bulk_cid

<!-- UsageSnippet language="python" operationID="getMmsPrice" method="post" path="/messages/mms/price" example="bulk_cid" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.get_price(request=[
        {
            "recipients": {
                "nr": "+48999999999",
                "cid": "custom-id-A44445T",
            },
            "subject": "This is a subject of the first message",
            "message": "This is first MMS message content",
            "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
            "date_": None,
        },
        {
            "recipients": {
                "nr": "+48999888777",
                "cid": "custom-id-F44445R",
            },
            "subject": "This is a subject of the second message",
            "message": "This is second MMS message content",
            "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
            "date_": None,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: multi

<!-- UsageSnippet language="python" operationID="getMmsPrice" method="post" path="/messages/mms/price" example="multi" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.get_price(request={
        "recipients": [
            "+48999999999",
            "+48999888777",
        ],
        "subject": "This is a subject of the message",
        "message": "This is MMS message content.",
        "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "date_": None,
    })

    # Handle response
    print(res)

```
### Example Usage: multi_cid

<!-- UsageSnippet language="python" operationID="getMmsPrice" method="post" path="/messages/mms/price" example="multi_cid" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.get_price(request={
        "recipients": [
            {
                "nr": "+48999999999",
                "cid": "custom-id-A44445T",
            },
            {
                "nr": "+48999888777",
                "cid": "custom-id-F44445R",
            },
        ],
        "subject": "This is a subject of the message",
        "message": "This is MMS message content",
        "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "date_": None,
    })

    # Handle response
    print(res)

```
### Example Usage: single

<!-- UsageSnippet language="python" operationID="getMmsPrice" method="post" path="/messages/mms/price" example="single" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.get_price(request={
        "recipients": "+48999999999",
        "subject": "This is a subject of the message",
        "message": "This is MMS message content.",
        "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "date_": None,
    })

    # Handle response
    print(res)

```
### Example Usage: single_cid

<!-- UsageSnippet language="python" operationID="getMmsPrice" method="post" path="/messages/mms/price" example="single_cid" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.get_price(request={
        "recipients": {
            "nr": "+48999999999",
            "cid": "custom-id-A44445T",
        },
        "subject": "This is a subject of the message",
        "message": "This is MMS message content",
        "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "date_": None,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.GetMmsPriceRequestBody](../../models/getmmspricerequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.GetMmsPriceResponse](../../models/getmmspriceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 401, 405                  | application/problem+json  |
| models.ErrorResponseError | 400, 415, 4XX             | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## send

Send single or multiple MMS messages at the same time. You can pass as a `request` named parameter a single `MmsMessage` object (for single message) or `List[MmsMessage]` (for multiple messages). Each `MmsMessage` object has several properties, describing message parameters such recipient phone number, content of the message, attachments or scheduled sending date, etc. This method will accept maximum 50 messages in one call.

As a successful result a `SendMmsResponse` object will be returned with `result` property of type `List[Message]` containing `Message` objects, one object per each single message. You should check the `status_code` property of each `Message` object to make sure which messages were accepted by gateway (queued) and which were rejected. In case of rejection, `status_description` property will include a reason.

`SendMmsResponse` will also include `headers` property with `X-Success-Count` (a count of messages which were processed successfully), `X-Error-Count` (count of messages which were rejected) and `X-Sandbox` (if a request was made in Sandbox or Production system) elements.

### Example Usage: bulk

<!-- UsageSnippet language="python" operationID="sendMms" method="post" path="/messages/mms" example="bulk" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.send(request=[
        {
            "recipients": "+48999999999",
            "subject": "This is a subject of the first message",
            "message": "This is first MMS message content",
            "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
            "date_": None,
        },
        {
            "recipients": "+48999888777",
            "subject": "This is a subject of the second message",
            "message": "This is second MMS message content",
            "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
            "date_": None,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: bulk_cid

<!-- UsageSnippet language="python" operationID="sendMms" method="post" path="/messages/mms" example="bulk_cid" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.send(request=[
        {
            "recipients": {
                "nr": "+48999999999",
                "cid": "custom-id-A44445T",
            },
            "subject": "This is a subject of the first message",
            "message": "This is first MMS message content",
            "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
            "date_": None,
        },
        {
            "recipients": {
                "nr": "+48999888777",
                "cid": "custom-id-F44445R",
            },
            "subject": "This is a subject of the second message",
            "message": "This is second MMS message content",
            "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
            "date_": None,
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: multi

<!-- UsageSnippet language="python" operationID="sendMms" method="post" path="/messages/mms" example="multi" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.send(request={
        "recipients": [
            "+48999999999",
            "+48999888777",
        ],
        "subject": "This is a subject of the message",
        "message": "This is MMS message content.",
        "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "date_": None,
    })

    # Handle response
    print(res)

```
### Example Usage: multi_cid

<!-- UsageSnippet language="python" operationID="sendMms" method="post" path="/messages/mms" example="multi_cid" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.send(request={
        "recipients": [
            {
                "nr": "+48999999999",
                "cid": "custom-id-A44445T",
            },
            {
                "nr": "+48999888777",
                "cid": "custom-id-F44445R",
            },
        ],
        "subject": "This is a subject of the message",
        "message": "This is MMS message content",
        "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "date_": None,
    })

    # Handle response
    print(res)

```
### Example Usage: single

<!-- UsageSnippet language="python" operationID="sendMms" method="post" path="/messages/mms" example="single" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.send(request={
        "recipients": "+48999999999",
        "subject": "This is a subject of the message",
        "message": "This is MMS message content.",
        "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "date_": None,
    })

    # Handle response
    print(res)

```
### Example Usage: single_cid

<!-- UsageSnippet language="python" operationID="sendMms" method="post" path="/messages/mms" example="single_cid" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.mms.send(request={
        "recipients": {
            "nr": "+48999999999",
            "cid": "custom-id-A44445T",
        },
        "subject": "This is a subject of the message",
        "message": "This is MMS message content",
        "attachments": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "date_": None,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SendMmsRequestBody](../../models/sendmmsrequestbody.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SendMmsResponse](../../models/sendmmsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 401, 405                  | application/problem+json  |
| models.ErrorResponseError | 400, 403, 415, 4XX        | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |