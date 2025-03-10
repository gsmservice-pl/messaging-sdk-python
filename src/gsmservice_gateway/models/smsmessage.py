"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .phonenumberwithcid import PhoneNumberWithCid, PhoneNumberWithCidTypedDict
from .smstype import SmsType
from datetime import datetime
from gsmservice_gateway.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET_SENTINEL,
)
from gsmservice_gateway.utils import validate_open_enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


SmsMessageRecipientsTypedDict = TypeAliasType(
    "SmsMessageRecipientsTypedDict",
    Union[
        PhoneNumberWithCidTypedDict, str, List[str], List[PhoneNumberWithCidTypedDict]
    ],
)
r"""The recipient number or multiple recipients numbers of single message. To set one recipient, simply pass a `str` with his phone number. To set multiple recipients, please pass `List[str]`. Optionally you can also set custom id (user identifier) for each message - pass `PhoneNumberWithCid` object (in case of single recipient) or List[PhoneNumberWithCid] (in case of multiple recipients)."""


SmsMessageRecipients = TypeAliasType(
    "SmsMessageRecipients",
    Union[PhoneNumberWithCid, str, List[str], List[PhoneNumberWithCid]],
)
r"""The recipient number or multiple recipients numbers of single message. To set one recipient, simply pass a `str` with his phone number. To set multiple recipients, please pass `List[str]`. Optionally you can also set custom id (user identifier) for each message - pass `PhoneNumberWithCid` object (in case of single recipient) or List[PhoneNumberWithCid] (in case of multiple recipients)."""


class SmsMessageTypedDict(TypedDict):
    r"""An object with a new SMS message properties"""

    recipients: SmsMessageRecipientsTypedDict
    r"""The recipient number or multiple recipients numbers of single message. To set one recipient, simply pass a `str` with his phone number. To set multiple recipients, please pass `List[str]`. Optionally you can also set custom id (user identifier) for each message - pass `PhoneNumberWithCid` object (in case of single recipient) or List[PhoneNumberWithCid] (in case of multiple recipients)."""
    message: str
    r"""SMS message content"""
    sender: NotRequired[str]
    r"""SMS sender name"""
    type: NotRequired[SmsType]
    r"""SMS type (1 -> SMS PRO, 3 -> SMS ECO, 4 -> SMS 2WAY)"""
    unicode: NotRequired[bool]
    r"""Should the message be sent with special characters, e.g. Polish diacritics (if any)? If *false*, those characters will be automatically replaced with their equivalents. If *true* your message will be sent as **unicode** but the message will be able to consist of fewer characters."""
    flash: NotRequired[bool]
    r"""Should the message to be sent with class 0 (FLASH)?"""
    date_: NotRequired[Nullable[datetime]]
    r"""Scheduled future date and time of sending the message (in ISO 8601 format). If missing or null - message will be sent immediately"""


class SmsMessage(BaseModel):
    r"""An object with a new SMS message properties"""

    recipients: SmsMessageRecipients
    r"""The recipient number or multiple recipients numbers of single message. To set one recipient, simply pass a `str` with his phone number. To set multiple recipients, please pass `List[str]`. Optionally you can also set custom id (user identifier) for each message - pass `PhoneNumberWithCid` object (in case of single recipient) or List[PhoneNumberWithCid] (in case of multiple recipients)."""

    message: str
    r"""SMS message content"""

    sender: Optional[str] = "Bramka SMS"
    r"""SMS sender name"""

    type: Annotated[Optional[SmsType], PlainValidator(validate_open_enum(True))] = 1
    r"""SMS type (1 -> SMS PRO, 3 -> SMS ECO, 4 -> SMS 2WAY)"""

    unicode: Optional[bool] = False
    r"""Should the message be sent with special characters, e.g. Polish diacritics (if any)? If *false*, those characters will be automatically replaced with their equivalents. If *true* your message will be sent as **unicode** but the message will be able to consist of fewer characters."""

    flash: Optional[bool] = False
    r"""Should the message to be sent with class 0 (FLASH)?"""

    date_: Annotated[OptionalNullable[datetime], pydantic.Field(alias="date")] = None
    r"""Scheduled future date and time of sending the message (in ISO 8601 format). If missing or null - message will be sent immediately"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["sender", "type", "unicode", "flash", "date"]
        nullable_fields = ["date"]
        null_default_fields = ["date"]

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
