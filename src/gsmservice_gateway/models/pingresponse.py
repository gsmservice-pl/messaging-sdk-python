"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gsmservice_gateway.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PingResponseTypedDict(TypedDict):
    r"""'Ping' response object"""

    status: NotRequired[str]
    r"""API service status: OK - API available, ERR - API unavailable"""
    version: NotRequired[str]
    r"""Current API Version"""
    sandbox: NotRequired[bool]
    r"""Was the connection established with the test system (SANDBOX)?"""


class PingResponse(BaseModel):
    r"""'Ping' response object"""

    status: Optional[str] = None
    r"""API service status: OK - API available, ERR - API unavailable"""

    version: Optional[str] = None
    r"""Current API Version"""

    sandbox: Optional[bool] = None
    r"""Was the connection established with the test system (SANDBOX)?"""
