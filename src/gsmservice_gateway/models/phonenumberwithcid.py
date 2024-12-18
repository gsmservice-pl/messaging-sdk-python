"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gsmservice_gateway.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PhoneNumberWithCidTypedDict(TypedDict):
    r"""An object defining the message recipient telephone number with the message's custom identifier assigned by the User"""

    nr: str
    r"""A telephone number in international format (with a plus sign and the country code at the beginning, e.g. +48 for Poland)"""
    cid: NotRequired[str]
    r"""Custom message ID assigned by the User"""


class PhoneNumberWithCid(BaseModel):
    r"""An object defining the message recipient telephone number with the message's custom identifier assigned by the User"""

    nr: str
    r"""A telephone number in international format (with a plus sign and the country code at the beginning, e.g. +48 for Poland)"""

    cid: Optional[str] = None
    r"""Custom message ID assigned by the User"""
