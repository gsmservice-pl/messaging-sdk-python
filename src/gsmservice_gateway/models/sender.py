"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gsmservice_gateway.types import BaseModel
from typing_extensions import TypedDict


class SenderTypedDict(TypedDict):
    r"""An object with the properties of the message sender"""

    sender: str
    r"""Message sender name"""
    status: str
    r"""Sender name status"""
    is_default: bool
    r"""Is the sender default?"""


class Sender(BaseModel):
    r"""An object with the properties of the message sender"""

    sender: str
    r"""Message sender name"""

    status: str
    r"""Sender name status"""

    is_default: bool
    r"""Is the sender default?"""
