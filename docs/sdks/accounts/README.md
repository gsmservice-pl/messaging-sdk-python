# Accounts
(*accounts*)

## Overview

### Available Operations

* [get](#get) - Get account details
* [get_subaccount](#get_subaccount) - Get subaccount details

## get

Get current account balance and other details of your account. You can check also account limit and if account is main one. Main accounts have unlimited privileges and using [User Panel](https://panel.gsmservice.pl) you can create as many subaccounts as you need.

As a successful result a details of current account you are logged in using an API Access Token will be returned.

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

Check account balance and other details such subcredit balance of a subaccount. Subaccounts are additional users who can access your account services and the details. You can restrict access level and setup privileges to subaccounts using [User Panel](https://panel.gsmservice.pl).

This method accepts an `user_login` named parameter of type `str` with user login. You should pass there the full subaccount login to access its data. 

As a successful result the details of subaccount with provided login will be returned.

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