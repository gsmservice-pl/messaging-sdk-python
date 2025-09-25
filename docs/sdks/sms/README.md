# Sms
(*outgoing.sms*)

## Overview

### Available Operations

* [get_price](#get_price) - Check the price of SMS Messages
* [send](#send) - Send SMS Messages

## get_price

Check the price of single or multiple SMS messages at the same time before sending them. You can pass as a `request` named parameter a single `SmsMessage` (for single message) or `List[SmsMessage]` (for multiple messages). Each `SmsMessage` object has several properties, describing message parameters such as recipient phone number, content of the message, type, etc.
The method will accept maximum **100** messages in one call.

As a successful result a `GetSmsPriceResponse` object will be returned with `result` property of type `List[Price]` containing a `Price` objects, one object per each single message. You should check the `error` property of each `Price` object to make sure which messages were priced successfully and which finished with an error. Successfully priced messages will have `null` value of `error` property.

`GetSmsPriceResponse` object will include also `headers` property with `X-Success-Count` (a count of messages which were processed successfully) and `X-Error-Count` (count of messages which were rejected) elements.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSmsPrice" method="post" path="/messages/sms/price" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.sms.get_price(request={
        "recipients": "+48999999999",
        "message": "This is SMS message content.",
        "sender": "Bramka SMS",
        "type": 1,
        "unicode": True,
        "flash": False,
        "date_": None,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.GetSmsPriceRequestBody](../../models/getsmspricerequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.GetSmsPriceResponse](../../models/getsmspriceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 4XX             | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |

## send

Send single or multiple SMS messages at the same time. You can pass as a `request` named parameter a single `SmsMessage` object (for single message) or `List[SmsMessage]` (for multiple messages). Each `SmsMessage` object has several properties, describing message parameters such recipient phone number, content of the message, type or scheduled sending date, etc. This method will accept maximum 100 messages in one call.

As a successful result a `SendSmsResponse` object will be returned with `result` property of type `List[Message]` containing `Message` objects, one object per each single message. You should check the `status_code` property of each `Message` object to make sure which messages were accepted by gateway (queued) and which were rejected. In case of rejection, `status_description` property will include a reason.

`SendSmsResponse` will also include `headers` property with `X-Success-Count` (a count of messages which were processed successfully), `X-Error-Count` (count of messages which were rejected) and `X-Sandbox` (if a request was made in Sandbox or Production system) elements.

### Example Usage

<!-- UsageSnippet language="python" operationID="sendSms" method="post" path="/messages/sms" -->
```python
from gsmservice_gateway import Client


with Client(
    bearer="<YOUR API ACCESS TOKEN>",
) as client:

    res = client.outgoing.sms.send(request={
        "recipients": "+48999999999",
        "message": "This is SMS message content.",
        "sender": "Bramka SMS",
        "type": 1,
        "unicode": True,
        "flash": False,
        "date_": None,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SendSmsRequestBody](../../models/sendsmsrequestbody.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SendSmsResponse](../../models/sendsmsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorResponseError | 400, 401, 403, 4XX        | application/problem+json  |
| models.ErrorResponseError | 5XX                       | application/problem+json  |