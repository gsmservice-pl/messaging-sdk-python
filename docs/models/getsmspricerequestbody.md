# GetSmsPriceRequestBody

To check the price of a single message or messages with the same content to multiple recipients, pass a single `SmsMessage` object with the properties of this message. To check the price of multiple messages with different content at the same time, pass a `List[SmsMessage]` with the properties of each message.


## Supported Types

### `models.SmsMessage`

```python
value: models.SmsMessage = /* values here */
```

### `List[models.SmsMessage]`

```python
value: List[models.SmsMessage] = /* values here */
```

