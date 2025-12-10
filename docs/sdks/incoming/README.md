# Incoming

## Overview

### Available Operations

* [list](#list) - List the received SMS messages
* [get_by_ids](#get_by_ids) - Get the incoming messages by IDs
* [remove_by_ids](#remove_by_ids) - Remove the incoming messages from your inbox

## list

Get the details of all received messages from your account incoming messages box. This method supports pagination so you have to pass `page` (number of page with received messages which you want to access) and a `limit` (max of received messages per page) named parameters. Messages are fetched from the latest one. This method will accept maximum **50** as `limit` parameter value.

As a successful result a `ListIncomingMessagesResponse` object will be returned with `result` property of type `List[IncomingMessage]` containing `IncomingMessage` objects, each object per single received message. `ListIncomingMessagesResponse` object will contain also a `headers` property where you can find `X-Total-Results` (a total count of all received messages which are available in incoming box on your account), `X-Total-Pages` (a total number of all pages with results), `X-Current-Page` (A current page number) and `X-Limit` (messages count per single page) elements.

### Example Usage

<!-- UsageSnippet language="python" operationID="listIncomingMessages" method="get" path="/incoming" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.incoming.list(page=1, limit=10)

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

**[models.ListIncomingMessagesResponse](../../models/listincomingmessagesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 404, 4XX   | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## get_by_ids

Get the details of one or more received messages using their `ids`. This method accepts a `List[int]` as a `ids` named parameter containing unique incoming message *IDs*, which were given while receiving a messages. The method will accept maximum 50 identifiers in one call.

As a successful result a `GetIncomingMessagesResponse` object will be returned with an `result` property of type `List[IncomingMessage]` containing `IncomingMessage` objects, each object per single received message. `GetIncomingMessagesResponse` object will contain also a `headers` property where you can find `X-Success-Count` (a count of incoming messages which were found and returned correctly) and `X-Error-Count` (count of incoming messages which were not found) elements.

### Example Usage

<!-- UsageSnippet language="python" operationID="getIncomingMessages" method="get" path="/incoming/{ids}" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.incoming.get_by_ids(ids=[
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

**[models.GetIncomingMessagesResponse](../../models/getincomingmessagesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 404, 4XX        | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## remove_by_ids

Remove incoming messages from your inbox using their `ids`. You have to pass the unique incoming message IDs as path parameter. If you want to remove multiple incoming messages at once, please separate their IDs with a comma. The system will accept maximum 50 identifiers in one call. If you need to remove larger volume of incoming messages, please split it to several separate requests.
 
As a successful result an array with `RemovedIncomingMessage` objects will be returned, each object per single incoming message id. The `status` property will contain a status code of operation - `204` if incoming message was removed successfully and other code if an error occured with removing a given incoming message. In case of an error, an `error` property will contain `ErrorResponse` object with the details of an error.
 
Response will also include meta-data headers: `X-Success-Count` (a count of incoming messages which were removed successfully), `X-Error-Count` (count of incoming messages which were not removed) and `X-Sandbox` (if a request was made in Sandbox or Production system).
 
If you pass duplicated incoming message IDs in one call, API will process them only once. This request have to be authenticated using **API Access Token**.

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

<!-- UsageSnippet language="python" operationID="removeIncomingMessages" method="delete" path="/incoming/{ids}" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.incoming.remove_by_ids(ids=[
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

**[models.RemoveIncomingMessagesResponse](../../models/removeincomingmessagesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 404, 4XX   | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |