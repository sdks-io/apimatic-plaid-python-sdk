from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_filter import AccountFilter, AccountFilterDict
from .enums.account_selection_cardinality import AccountSelectionCardinalityOrStr
from .product_access import ProductAccess, ProductAccessDict


class RequestedScopes(SdkBaseModel):
    """Scope of required and optional account features or content from a ConnectedApplication."""

    required_product_access: ProductAccess
    """The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to
    all products allowed."""

    optional_product_access: ProductAccess
    """The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to
    all products allowed."""

    account_filters: Optional[AccountFilter] = UNSET
    """Enumerates the account subtypes that the application wishes for the user to be able to select from. For more
    details refer to Plaid documentation on account filters."""

    account_selection_cardinality: AccountSelectionCardinalityOrStr
    """The application requires that accounts be limited to a specific cardinality. ``MULTI_SELECT``: indicates that the
    user should be allowed to pick multiple accounts. ``SINGLE_SELECT``: indicates that the user should be allowed to
    pick only a single account. ``ALL``: indicates that the user must share all of their accounts and should not be
    given the opportunity to de-select"""


class RequestedScopesDict(TypedDict):
    required_product_access: ProductAccessDict
    optional_product_access: ProductAccessDict
    account_filters: NotRequired[AccountFilterDict]
    account_selection_cardinality: AccountSelectionCardinalityOrStr
