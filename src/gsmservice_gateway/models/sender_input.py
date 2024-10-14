"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gsmservice_gateway.types import BaseModel
from typing_extensions import TypedDict


class SenderInputTypedDict(TypedDict):
    r"""An object with the properties of the message sender"""

    sender: str
    r"""Message sender name"""
    description: str
    r"""Description of the purpose of the sender name (required when adding new sender name)"""


class SenderInput(BaseModel):
    r"""An object with the properties of the message sender"""

    sender: str
    r"""Message sender name"""

    description: str
    r"""Description of the purpose of the sender name (required when adding new sender name)"""
