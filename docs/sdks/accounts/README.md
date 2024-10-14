# Accounts
(*accounts*)

## Overview

### Available Operations

* [get](#get) - Get account details
* [get_subaccount](#get_subaccount) - Get subaccount details

## get

Get current account balance and other details of your account. You can check also account limit and if account is main one. Main accounts have unlimited privileges and using [User Panel](https://panel.gsmservice.pl) you can create as many subaccounts as you need.
 
The request doesn't contain a body or any parameters. As a successful result an `AccountResponse` object will be returned with properties describing details of current account you are logged in to using API Access Token. This request have to be authenticated using **API Access Token**.

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("GATEWAY_API_BEARER", ""),
)

res = s.accounts.get()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AccountResponse](../../models/accountresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 401, 403, 4XX, 5XX        | application/problem+json  |

## get_subaccount

Check account balance and other details such subcredit balance of a subaccount. Subaccounts are additional users who can access your account services and the details. You can restrict access level and setup privileges to subaccounts using [user panel](https://panel.gsmservice.pl).
    
This endpoint accepts a path `user_login` parameter with empty request body. You should pass the full subaccount login to access its data. 

As a successful result an `AccountResponse` object will be returned with properties describing details of subaccount with provided login. This request have to be authenticated using **API Access Token**.

In case of an error, the `ErrorResponse` object will be returned with proper HTTP header status code (our error response complies with [RFC 9457](https://www.rfc-editor.org/rfc/rfc7807)).

### Example Usage

```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("GATEWAY_API_BEARER", ""),
)

res = s.accounts.get_subaccount(user_login="some-login")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_login`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Login of the subaccount (user) to get the data for                  | some-login                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AccountResponse](../../models/accountresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 401, 403, 404, 4XX, 5XX   | application/problem+json  |