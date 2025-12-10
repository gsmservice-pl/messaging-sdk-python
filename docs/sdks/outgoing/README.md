# Outgoing

## Overview

### Available Operations

* [get_by_ids](#get_by_ids) - Get the messages details and status by IDs
* [cancel_scheduled](#cancel_scheduled) - Cancel a scheduled messages
* [list](#list) - Lists the history of sent messages

## get_by_ids

Check the current status and details of one or more messages using their `ids`. You have to pass a `List[int]` as a `ids` named parameter containing unique message *IDs* which details you want to fetch. This method will accept maximum 50 identifiers in one call.

As a successful result a `GetMessagesResponse` object will be returned containing `result` property of type `List[Message]` with `Message` objects, each object per single found message. `GetMessagesResponse` object will also contain `headers` property where you can find `X-Success-Count` (a count of messages which were found and returned correctly) and `X-Error-Count` (count of messages which were not found) elements.

### Example Usage

<!-- UsageSnippet language="python" operationID="getMessages" method="get" path="/messages/{ids}" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.get_by_ids(ids=[
        43456,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                              | List[*int*]                                                                                                        | :heavy_check_mark:                                                                                                 | List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call. |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.GetMessagesResponse](../../models/getmessagesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 404, 4XX   | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## cancel_scheduled

Cancel messages using their `ids` which were scheduled to be sent at a specific time. You have to pass a `List[int]` as a `ids` named parameter containing the unique message IDs, which were returned after sending a message. This method will accept maximum 50 identifiers in one call. You can cancel only messages with *SCHEDULED* status.
 
As a successful result a `CancelMessagesResponse` object will be returned, with `result` property of type `List[CancelledMessage]` containing `CancelledMessage` objects. The `status` property of each `CancelledMessage` object will contain a status code of operation - `204` if a particular message was cancelled successfully and other code if an error occured.
 
`CancelMessagesResponse` object will also contain `headers` property where you can find `X-Success-Count` (a count of messages which were cancelled successfully), `X-Error-Count` (count of messages which were not cancelled) and `X-Sandbox` (if a request was made in Sandbox or Production system) elements.

### Example Usage

<!-- UsageSnippet language="python" operationID="cancelMessages" method="delete" path="/messages/{ids}" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.cancel_scheduled(ids=[
        43456,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `ids`                                                                                                              | List[*int*]                                                                                                        | :heavy_check_mark:                                                                                                 | List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call. |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.CancelMessagesResponse](../../models/cancelmessagesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 404, 4XX   | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## list

Get the details and current status of all of sent messages from your account message history. This method supports pagination so you have to pass a `page` (number of page with messages which you want to access) and a `limit` (max of messages per page) named parameters. Messages are fetched from the latest one. This method will accept maximum value of **50** as `limit` parameter value.

As a successful result a `ListMessagesResponse` object will be returned containing `result` property of type `List[Message]` with a `Message` objects, each object per single message. `ListMessagesResponse` will also contain `headers` property where you can find `X-Total-Results` (a total count of all messages which are available in history on your account), `X-Total-Pages` (a total number of all pages with results), `X-Current-Page` (A current page number) and `X-Limit` (messages count per single page) elements.

### Example Usage

<!-- UsageSnippet language="python" operationID="listMessages" method="get" path="/messages" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.list(page=1, limit=10)

    # Handle response
    print(res)

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 404, 4XX   | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |