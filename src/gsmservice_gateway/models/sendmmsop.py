"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .message import Message, MessageTypedDict
from .mmsmessage import MmsMessage, MmsMessageTypedDict
from gsmservice_gateway.types import BaseModel
from typing import Dict, List, Union
from typing_extensions import TypeAliasType, TypedDict


SendMmsRequestBodyTypedDict = TypeAliasType(
    "SendMmsRequestBodyTypedDict", Union[MmsMessageTypedDict, List[MmsMessageTypedDict]]
)
r"""To send a single MMS or messages with the same content to multiple recipients, please pass a single `MmsMessage` object with the properties of this message. To send multiple messages with different content at the same time, please pass `List[MmsMessage]` with the properties of each message."""


SendMmsRequestBody = TypeAliasType(
    "SendMmsRequestBody", Union[MmsMessage, List[MmsMessage]]
)
r"""To send a single MMS or messages with the same content to multiple recipients, please pass a single `MmsMessage` object with the properties of this message. To send multiple messages with different content at the same time, please pass `List[MmsMessage]` with the properties of each message."""


class SendMmsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: List[MessageTypedDict]


class SendMmsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: List[Message]
