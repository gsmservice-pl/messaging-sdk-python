# SendSmsRequestBody

To send a single SMS or messages with the same content to multiple recipients, please pass a single `SmsMessage` object with the properties of this message. To send multiple messages with different content at the same time, please pass `List[SmsMessage]` with the properties of each message.


## Supported Types

### `models.SmsMessage`

```python
value: models.SmsMessage = /* values here */
```

### `List[models.SmsMessage]`

```python
value: List[models.SmsMessage] = /* values here */
```

