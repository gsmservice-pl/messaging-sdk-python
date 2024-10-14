# gsmservice-gateway

Developer-friendly & type-safe Python SDK specifically catered to leverage *gsmservice-gateway* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=gsmservice-gateway&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/intermedia/gsmservice-pl). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Messaging Gateway GSMService.pl: 
# Introduction

This document was created to explain the process of integration any application or system with the **GSMService.pl** SMS Gateway via the *REST API*. Currently, there are several ways to send messages with the GSMService.pl platform:

* Directly from the [https://bramka.gsmservice.pl](https://bramka.gsmservice.pl) website [User Panel](https://panel.gsmservice.pl)
* Via this *REST API* and provided *SDKs*
* Via the legacy (deprecated) versions API: *Webservices (SOAP)* and *HTTP* 
* Via the *MAIL2SMS* service

This document describes the possibilities offered by **REST API**.

> **We kindly ask you to read this documentation carefully before starting the integration. This will make the whole process easier and will help you avoid many problems.**

## Documentation and Try Outs

This documentation is available in two formats: [**REDOC**](https://api.gsmservice.pl/rest/) and [**SWAGGER**](https://api.gsmservice.pl/rest/swagger). You can test any endpoint directly from documentation using **Try Out** feature of Swagger. Also you can [download a **YAML** file](https://api.gsmservice.pl/rest/swagger/messaging.yaml) with doc in OpenApi 3.0 format.

## Account signup and setup

Firstly, it is necessary to create your personal account at the GSMService.pl SMS Gateway platform if you haven't one and activate access to the API. To register a new account please [signup the form](https://panel.gsmservice.pl/rejestracja). After signing up and fully activation of an account you have to activate an access to the API.

To do it please use [this site](https://panel.gsmservice.pl/api) - fill the *New API Access* form with your preferred API login, set your API password, select which API standard you want to activate for this account (select **REST API** there). Optionally you can add IP adresses (or IP pool with CIDR notation) from which access to your API account will be possible. You can also set a callback address there to collect any messages status updates automatically. When a status of a messaga changes, the callback address will be called with passing parameters with new message status.

After setup an API access you will get an unique **API Access Token** - please write it down as there won't be possible to display it again (you will have the possibility to regenerate it only). This token will be required to authenticate all the requests made with API on your account.

## Authentication of API requests

All the endpoints of this REST API have to be authenticated using your API Access Token with one exception: */rest/ping* endpoint which doesn't need an authentication. 

To make an authenticated request you should add to all requests an ***Authorization* header** which you have generated in previous step:

```
Authorization: Bearer &lt;YOUR_API_ACCESS_TOKEN&gt;
```

## URLs to connect to API

Please use this SSL secured adresses to connect to REST API:

* ```https://api.gsmservice.pl/rest``` - for production system

* ```https://api.gsmservice.pl/rest-sandbox``` - for test system (Sandbox)

> [!NOTE]
> **When calling our API, make sure you are using TLS version 1.2 or higher. Older versions are no longer supported.**

# SDK Client Libraries

For developers integrating SMS functionality into their app, we provide a convenient SDK Libraries.

Our SDKs allow you to quickly start interacting with the Gateway using your favorite programming language. Currently we support the following languages:

## PHP 8

To install PHP SDK issue the following command:

```shell
composer require gsmservice-pl/messaging-sdk-php
```
More information and documentation you can find at our [GitHub](https://github.com/gsmservice-pl/messaging-sdk-php) 

## Typescript

To install Typescript SDK issue the following command:

### NPM

```shell
npm add @gsmservice-pl/messaging-sdk-typescript
```

More information and documentation you can find at our [GitHub](https://github.com/gsmservice-pl/messaging-sdk-typescript)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Sending single SMS Message

This example demonstrates simple sending SMS message to a single recipient:

```python
# Synchronous Example
import gsmservice_gateway
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.outgoing.sms.send(request=[
    {
        "recipients": [
            "+48999999999",
        ],
        "message": "To jest treść wiadomości",
        "sender": "Bramka SMS",
        "type": gsmservice_gateway.SmsType.SMS_PRO,
        "unicode": True,
        "flash": False,
        "date_": None,
    },
])

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import gsmservice_gateway
from gsmservice_gateway import Client
import os

async def main():
    s = Client(
        bearer=os.getenv("CLIENT_BEARER", ""),
    )
    res = await s.outgoing.sms.send_async(request=[
        {
            "recipients": "+48999999999",
            "message": "To jest treść wiadomości",
            "sender": "Bramka SMS",
            "type": gsmservice_gateway.SmsType.SMS_PRO,
            "unicode": True,
            "flash": False,
            "date_": None,
        },
    ])
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [accounts](docs/sdks/accounts/README.md)

* [get](docs/sdks/accounts/README.md#get) - Get account details
* [get_subaccount](docs/sdks/accounts/README.md#get_subaccount) - Get subaccount details


### [common](docs/sdks/common/README.md)

* [ping](docs/sdks/common/README.md#ping) - Checks API availability and version

### [incoming](docs/sdks/incoming/README.md)

* [list](docs/sdks/incoming/README.md#list) - List the received SMS messages
* [get_by_ids](docs/sdks/incoming/README.md#get_by_ids) - Get the incoming messages by IDs

### [outgoing](docs/sdks/outgoing/README.md)

* [get_by_ids](docs/sdks/outgoing/README.md#get_by_ids) - Get the messages details and status by IDs
* [cancel_scheduled](docs/sdks/outgoing/README.md#cancel_scheduled) - Cancel a scheduled messages
* [list](docs/sdks/outgoing/README.md#list) - Lists the history of sent messages

#### [outgoing.sms](docs/sdks/smssdk/README.md)

* [get_price](docs/sdks/smssdk/README.md#get_price) - Check the price of SMS Messages
* [send](docs/sdks/smssdk/README.md#send) - Send SMS Messages

### [senders](docs/sdks/senders/README.md)

* [list](docs/sdks/senders/README.md#list) - List allowed senders names
* [add](docs/sdks/senders/README.md#add) - Add a new sender name
* [delete](docs/sdks/senders/README.md#delete) - Delete a sender name
* [set_default](docs/sdks/senders/README.md#set_default) - Set default sender name

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from client.utils import BackoffStrategy, RetryConfig
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.accounts.get(,
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from client.utils import BackoffStrategy, RetryConfig
from gsmservice_gateway import Client
import os

s = Client(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.accounts.get()

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_async` method may raise the following exceptions:

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 401, 403, 4XX, 5XX        | application/problem+json  |

### Example

```python
from gsmservice_gateway import Client, models
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = None
try:
    res = s.accounts.get()

    if res is not None:
        # handle response
        pass

except models.ErrorResponseError as e:
    # handle e.data: models.ErrorResponseErrorData
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `prod` | `https://api.gsmservice.pl/rest` | None |
| `sandbox` | `https://api.gsmservice.pl/rest-sandbox` | None |

#### Example

```python
from gsmservice_gateway import Client
import os

s = Client(
    server="sandbox",
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.accounts.get()

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from gsmservice_gateway import Client
import os

s = Client(
    server_url="https://api.gsmservice.pl/rest",
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.accounts.get()

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from gsmservice_gateway import Client
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Client(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from gsmservice_gateway import Client
from gsmservice_gateway.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Client(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                 | Type                 | Scheme               | Environment Variable |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `bearer`             | http                 | HTTP Bearer          | `CLIENT_BEARER`      |

To authenticate with the API the `bearer` parameter must be set when initializing the SDK client instance. For example:
```python
from gsmservice_gateway import Client
import os

s = Client(
    bearer=os.getenv("CLIENT_BEARER", ""),
)

res = s.accounts.get()

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from gsmservice_gateway import Client
import logging

logging.basicConfig(level=logging.DEBUG)
s = Client(debug_logger=logging.getLogger("gsmservice_gateway"))
```

You can also enable a default debug logger by setting an environment variable `CLIENT_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=gsmservice-gateway&utm_campaign=python)
