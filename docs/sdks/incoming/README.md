# Incoming
(*incoming*)

## Overview

### Available Operations

* [list](#list) - List the received SMS messages
* [get_by_ids](#get_by_ids) - Get the incoming messages by IDs

## list

Get the details of all received messages from your account incoming messages box. This method supports pagination so you have to pass `page` (number of page with received messages which you want to access) and a `limit` (max of received messages per page) named parameters. Messages are fetched from the latest one. This method will accept maximum **50** as `limit` parameter value.

As a successful result a `ListIncomingMessagesResponse` object will be returned with `result` property of type `List[IncomingMessage]` containing `IncomingMessage` objects, each object per single received message. `ListIncomingMessagesResponse` object will contain also a `headers` property where you can find `X-Total-Results` (a total count of all received messages which are available in incoming box on your account), `X-Total-Pages` (a total number of all pages with results), `X-Current-Page` (A current page number) and `X-Limit` (messages count per single page) elements.

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("GATEWAY_API_BEARER", ""),
)

res = s.incoming.list(page=1, limit=10)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number of results                                              | 1                                                                   |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of results on one page                                       | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListIncomingMessagesResponse](../../models/listincomingmessagesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ErrorResponseError    | 400, 401, 403, 404, 4XX, 5XX | application/problem+json     |

## get_by_ids

Get the details of one or more received messages using their `ids`. This method accepts a `List[int]` as a `ids` named parameter containing unique incoming message *IDs*, which were given while receiving a messages. The method will accept maximum 50 identifiers in one call.

As a successful result a `GetIncomingMessagesResponse` object will be returned with an `result` property of type `List[IncomingMessage]` containing `IncomingMessage` objects, each object per single received message. `GetIncomingMessagesResponse` object will contain also a `headers` property where you can find `X-Success-Count` (a count of incoming messages which were found and returned correctly) and `X-Error-Count` (count of incoming messages which were not found) elements.

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("GATEWAY_API_BEARER", ""),
)

res = s.incoming.get_by_ids(ids=[
    43456,
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                              | List[*int*]                                                                                                        | :heavy_check_mark:                                                                                                 | List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call. |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.GetIncomingMessagesResponse](../../models/getincomingmessagesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 404, 4XX, 5XX   | application/problem+json  |