# Senders
(*senders*)

## Overview

### Available Operations

* [list](#list) - List allowed senders names
* [add](#add) - Add a new sender name
* [delete](#delete) - Delete a sender name
* [set_default](#set_default) - Set default sender name

## list

Get a list of allowed senders defined in your account.

As a successful result a `List[Sender]` containing `Sender` objects will be returned, each object per single sender.

### Example Usage

```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.senders.list()

    # Handle response
    print(res)

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
| models.ErrorResponseError | 400, 401, 403, 4XX        | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## add

Define a new allowed sender on your account. You should pass as `request` named parameter a `SenderInput` object with two properties: `sender` (defines sender name) and `description`. Please carefully fill this property with the extensive description of a sender name (what will be its use, what the name mean, etc).

As a successful result a `AddSenderResponse` object will be returned with a `result` property containing a `Sender` object with details and status of added sender name.

### Example Usage

```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.senders.add(request={
        "sender": "Bramka SMS",
        "description": "This is our company name. It contains our registered trademark.",
    })

    # Handle response
    print(res)

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
| models.ErrorResponseError | 400, 401, 403, 4XX        | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## delete

Removes defined sender name from your account. This method accepts a `sender` named parameter with a **sender name** you want to remove. Sender name will be deleted immediately.

As a successful response a `DeleteSenderResponse` object will be returned with no Exception thrown.

### Example Usage

```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.senders.delete(sender="Podpis")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sender`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Sender name to be removed                                           | Podpis                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteSenderResponse](../../models/deletesenderresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 404, 4XX   | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## set_default

Set default sender name to one of the senders names already defined on your account. This method accepts a `sender` named parameter containing a **sender name** to be set as default on your account.

As a successful response a `SetDefaultSenderResponse` object will be returned with no exception to be thrown.

### Example Usage

```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.senders.set_default(sender="Podpis")

    # Handle response
    print(res)

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
| models.ErrorResponseError | 404                       | application/json          |
| models.ErrorResponseError | 400, 401, 403, 4XX        | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |