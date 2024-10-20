"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .message import Message, MessageTypedDict
from gsmservice_gateway.types import BaseModel
from gsmservice_gateway.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetMessagesRequestTypedDict(TypedDict):
    ids: List[int]
    r"""List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call."""


class GetMessagesRequest(BaseModel):
    ids: Annotated[
        List[int], FieldMetadata(path=PathParamMetadata(style="simple", explode=True))
    ]
    r"""List[str] with Message IDs assigned by the system. The system will accept a maximum of 50 identifiers in one call."""


class GetMessagesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: List[MessageTypedDict]


class GetMessagesResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: List[Message]
