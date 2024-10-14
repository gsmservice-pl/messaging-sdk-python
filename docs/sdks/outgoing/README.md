# Outgoing
(*outgoing*)

## Overview

### Available Operations

* [get_by_ids](#get_by_ids) - Get the messages details and status by IDs
* [cancel_scheduled](#cancel_scheduled) - Cancel a scheduled messages
* [list](#list) - Lists the history of sent messages

## get_by_ids

Check the current status and details of one or more messages using their `ids`. You have to pass the unique message *IDs* as path parameter, which were returned after sending a message. If you want to get the details of multiple messages at once, please separate their IDs with a comma. The system will accept maximum 50 identifiers in one call. If you need to get details of larger volume of messages, please split it to several separate requests.
    
As a successful result an array with `Message` objects will be returned, each object per single found message. Response will also include meta-data headers: `X-Success-Count` (a count of messages which were found and returned correctly) and `X-Error-Count` (count of messages which were not found).

If you pass duplicated IDs, API will return data of this message only once. This request have to be authenticated using **API Access Token**. 

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.outgoing.get_by_ids(ids=[
    43456,
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                                    | List[*int*]                                                                                                              | :heavy_check_mark:                                                                                                       | Message IDs assigned by the system (separated by comma). The system will accept a maximum of 50 identifiers in one call. |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.GetMessagesResponse](../../models/getmessagesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ErrorResponseError    | 400, 401, 403, 404, 4XX, 5XX | application/problem+json     |

## cancel_scheduled

Cancel messages using their `ids` which were scheduled to be sent at a specific time. You have to pass the unique message IDs as path parameter, which were returned after sending a message. If you want to cancel multiple messages at once, please separate their IDs with a comma. The system will accept maximum 50 identifiers in one call. If you need to cancel larger volume of messages, please split it to several separate requests. You can cancel only messages with *SCHEDULED* status.
 
As a successful result an array with `CancelledMessage` objects will be returned, each object per single message id. The `status` property will contain a status code of operation - `204` if message was cancelled successfully and other code if an error occured with cancelling a given message. In case of an error, an `error` property will contain `ErrorResponse` object with the details of an error.
 
Response will also include meta-data headers: `X-Success-Count` (a count of messages which were cancelled successfully), `X-Error-Count` (count of messages which were not cancelled) and `X-Sandbox` (if a request was made in Sandbox or Production system).
 
If you pass duplicated message IDs in one call, API will process them only once. This request have to be authenticated using **API Access Token**.

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.outgoing.cancel_scheduled(ids=[
    43456,
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                                    | List[*int*]                                                                                                              | :heavy_check_mark:                                                                                                       | Message IDs assigned by the system (separated by comma). The system will accept a maximum of 50 identifiers in one call. |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[models.CancelMessagesResponse](../../models/cancelmessagesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ErrorResponseError    | 400, 401, 403, 404, 4XX, 5XX | application/problem+json     |

## list

Get the details and current status of all of sent messages from your account message history. This endpoint supports pagination so you have to pass as query parameters a `page` value (number of page with messages which you want to access) and a `limit` value (max of messages per page). Messages are fetched from the latest one. The system will accept maximum **50** as `limit` parameter value. If you need to get details of larger volume of messages, please access them with next pages.
    
As a successful result an array with `Message` objects will be returned, each object per single message. Response will also include meta-data headers: `X-Total-Results` (a total count of all messages which are available in history on your account), `X-Total-Pages` (a total number of all pages with results), `X-Current-Page` (A current page number) and `X-Limit` (messages count per single page). This request have to be authenticated using **API Access Token**. 

A response contains also a special `Link` header which includes *URIs* to access next, previous, first and last page with messages (which complies with [RFC 5988](https://www.rfc-editor.org/rfc/rfc5988)). 

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).


### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.outgoing.list(page=1, limit=10)

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

**[models.ListMessagesResponse](../../models/listmessagesresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ErrorResponseError    | 400, 401, 403, 404, 4XX, 5XX | application/problem+json     |