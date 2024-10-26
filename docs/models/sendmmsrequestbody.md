# SendMmsRequestBody

To send a single MMS or messages with the same content to multiple recipients, please pass a single `MmsMessage` object with the properties of this message. To send multiple messages with different content at the same time, please pass `List[MmsMessage]` with the properties of each message.


## Supported Types

### `models.MmsMessage`

```python
value: models.MmsMessage = /* values here */
```

### `List[models.MmsMessage]`

```python
value: List[models.MmsMessage] = /* values here */
```

