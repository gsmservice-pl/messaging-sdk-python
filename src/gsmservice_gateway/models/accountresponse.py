"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gsmservice_gateway.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AccountType(str, Enum):
    r"""Account type"""

    PRE_PAID = "PRE-PAID"
    POST_PAID = "POST-PAID"


class AccountResponseTypedDict(TypedDict):
    r"""An object containing information about the User's account and balance"""

    login: NotRequired[str]
    r"""User Login"""
    account_type: NotRequired[AccountType]
    r"""Account type"""
    limit: NotRequired[float]
    r"""Acount limit"""
    credit: NotRequired[float]
    r"""Current account balance"""
    subcredit: NotRequired[Nullable[float]]
    r"""Subaccount credit balance (null if unlimited)"""
    currency: NotRequired[str]
    r"""Account currency"""
    name: NotRequired[str]
    r"""User name and surname"""
    is_main: NotRequired[bool]
    r"""Is main account?"""


class AccountResponse(BaseModel):
    r"""An object containing information about the User's account and balance"""

    login: Optional[str] = None
    r"""User Login"""

    account_type: Optional[AccountType] = None
    r"""Account type"""

    limit: Optional[float] = None
    r"""Acount limit"""

    credit: Optional[float] = None
    r"""Current account balance"""

    subcredit: OptionalNullable[float] = UNSET
    r"""Subaccount credit balance (null if unlimited)"""

    currency: Optional[str] = None
    r"""Account currency"""

    name: Optional[str] = None
    r"""User name and surname"""

    is_main: Optional[bool] = None
    r"""Is main account?"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "login",
            "account_type",
            "limit",
            "credit",
            "subcredit",
            "currency",
            "name",
            "is_main",
        ]
        nullable_fields = ["subcredit"]
        null_default_fields = []

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
