# Senders
(*senders*)

## Overview

### Available Operations

* [list](#list) - List allowed senders names
* [add](#add) - Add a new sender name
* [delete](#delete) - Delete a sender name
* [set_default](#set_default) - Set default sender name

## list

Get a list of allowed senders defined in your account. The request doesn't contain a body or any parameters. 
        
As a successful result an array with `Sender` objects will be returned, each object per single sender. Senders are being registered by providers and operators. Registered senders get *Active* status and can be used then to send messages. *Pending* senders are also returned by API (with proper `status`) but until registration they cannot be used. This request have to be authenticated using **API Access Token**.

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.senders.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.Sender]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 4XX, 5XX   | application/problem+json  |

## add

Define a new allowed sender on your account. The request body should contain a `Sender` object with two properties: `sender` (defines sender name) and `description`. The secont parameter is very important - sender names are being registered by providers and operators. Only fully registered sender names can be used to send messages. Providers need sometimes detailed description of case in which the sender will be used to eliminate frauds. After verifing it they make a decisions if such sender name can be registered. Please carefully fill this property with the extensive description of a sender name (what will be its use, what the name mean, etc). 
        
As a successful result a single `Sender` object will be returned. Registered senders get *Active* status and can be used then to send messages. Pending Senders are also returned by API (with proper `status`) but until registration they cannot be used. Response will also include meta-data header: `X-Sandbox` (if a request was made in Sandbox or Production system). This request have to be authenticated using **API Access Token**.

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.senders.add(request={
    "sender": "Bramka SMS",
    "description": "This is our company name. It contains our registered trademark.",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SenderInput](../../models/senderinput.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AddSenderResponse](../../models/addsenderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 4XX, 5XX   | application/problem+json  |

## delete

Removes defined sender name from your account. This endpoint accepts a path `sender` parameter with empty request body. You should pass the full sender name to delete it. Sender name will be deleted immediately.

As a successful response only HTTP status code of *204* will be returned in header with empty response body. Response will also include meta-data header: `X-Sandbox` (if a request was made in Sandbox or Production system).
This request have to be authenticated using **API Access Token**.

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.senders.delete(sender="Podpis")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sender`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Sender name to be removed                                           | Podpis                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteSenderResponse](../../models/deletesenderresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ErrorResponseError    | 400, 401, 403, 404, 4XX, 5XX | application/problem+json     |

## set_default

Set default sender name to one of the senders names already defined on your account. Default sender name can be used while sending messages when you not pass any other defined sender to `Sms` object while sending message. 

This endpoint accepts a path `sender` parameter with empty request body. You should pass the full sender name to set it as default on your account.

As a successful response only HTTP status code of *204* will be returned in header with empty response body. Response will also include meta-data header: `X-Sandbox` (if a request was made in Sandbox or Production system).
This request have to be authenticated using **API Access Token**.

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.senders.set_default(sender="Podpis")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sender`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Sender name to set as default                                       | Podpis                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SetDefaultSenderResponse](../../models/setdefaultsenderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 4XX, 5XX   | application/problem+json  |
| models.ErrorResponseError | 404                       | application/json          |