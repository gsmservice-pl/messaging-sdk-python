# Common
(*common*)

## Overview

### Available Operations

* [ping](#ping) - Checks API availability and version

## ping

Check the API connection and the current API availability status. Also you will get the current API version number.

As a successful result a `PingResponse` object will be returned.

### Example Usage

<!-- UsageSnippet language="python" operationID="ping" method="get" path="/ping" -->
```python
from gsmservice_gateway import Client


with Client() as client:

    res = client.common.ping()

    # Handle response
    print(res)

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
| models.ErrorResponseError | 400, 4XX                  | application/problem+json  |
| models.ErrorResponseError | 503, 5XX                  | application/problem+json  |