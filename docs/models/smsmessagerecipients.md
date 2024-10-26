# SmsMessageRecipients

The recipient number or multiple recipients numbers of single message. To set one recipient, simply pass a `str` with his phone number. To set multiple recipients, please pass `List[str]`. Optionally you can also set custom id (user identifier) for each message - pass `PhoneNumberWithCid` object (in case of single recipient) or List[PhoneNumberWithCid] (in case of multiple recipients).


## Supported Types

### `str`

```python
value: str = /* values here */
```

### `List[str]`

```python
value: List[str] = /* values here */
```

### `models.PhoneNumberWithCid`

```python
value: models.PhoneNumberWithCid = /* values here */
```

### `List[models.PhoneNumberWithCid]`

```python
value: List[models.PhoneNumberWithCid] = /* values here */
```

