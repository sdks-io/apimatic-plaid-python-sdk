from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ProductAccess(SdkBaseModel):
    """The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to
    all products allowed."""

    statements: bool | None = True
    """Allow access to statements. If unset, defaults to ``true``."""

    identity: bool | None = True
    """Allow access to the Identity product (name, email, phone, address). If unset, defaults to ``true``."""

    auth: bool | None = True
    """Allow access to account number details. If unset, defaults to ``true``."""

    transactions: bool | None = True
    """Allow access to transaction details. If unset, defaults to ``true``."""


class ProductAccessDict(TypedDict):
    statements: NotRequired[bool | None]
    identity: NotRequired[bool | None]
    auth: NotRequired[bool | None]
    transactions: NotRequired[bool | None]
