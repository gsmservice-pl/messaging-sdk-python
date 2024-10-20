# Common
(*common*)

## Overview

### Available Operations

* [ping](#ping) - Checks API availability and version

## ping

Check the API connection and the current API availability status. Also you will get the current API version number.

As a successful result a `PingResponse` object will be returned.

### Example Usage

```python
from gsmservice_gateway import Client

s = Client()

res = s.common.ping()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PingResponse](../../models/pingresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 4XX, 503, 5XX        | application/problem+json  |