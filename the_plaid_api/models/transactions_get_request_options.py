from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransactionsGetRequestOptions(SdkBaseModel):
    """An optional object to be used with the request. If specified, ``options`` must not be ``null``."""

    account_ids: Optional[list[str]] = UNSET
    """A list of ``account_ids`` to retrieve for the Item

    Note: An error will be returned if a provided ``account_id`` is not associated with the Item."""

    count: int = 100
    """The number of transactions to fetch."""

    offset: int = 0
    """The number of transactions to skip. The default value is 0."""

    include_original_description: bool | None = False
    """Include the raw unparsed transaction description from the financial institution. This field is disabled by
    default. If you need this information in addition to the parsed data provided, contact your Plaid Account
    Manager."""

    include_personal_finance_category_beta: bool = False
    """Include the ``personal_finance_category`` object in the response. This feature is currently in beta – to request
    access, contact transactions-feedback@plaid.com."""


class TransactionsGetRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
    count: NotRequired[int]
    offset: NotRequired[int]
    include_original_description: NotRequired[bool | None]
    include_personal_finance_category_beta: NotRequired[bool]
