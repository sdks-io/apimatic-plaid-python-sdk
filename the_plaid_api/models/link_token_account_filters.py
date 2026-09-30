from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_filter import CreditFilter, CreditFilterDict
from .depository_filter import DepositoryFilter, DepositoryFilterDict
from .investment_filter import InvestmentFilter, InvestmentFilterDict
from .loan_filter import LoanFilter, LoanFilterDict


class LinkTokenAccountFilters(SdkBaseModel):
    """By default, Link will provide limited account filtering: it will only display Institutions that are compatible
    with all products supplied in the ``products`` parameter of ``/link/token/create``, and, if ``auth`` is specified in
    the ``products`` array, will also filter out accounts other than ``checking`` and ``savings`` accounts on the
    Account Select pane. You can further limit the accounts shown in Link by using ``account_filters`` to specify the
    account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the
    Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected
    subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value ``"all"``. If the
    ``account_filters`` filter is used, any account type for which a filter is not specified will be entirely omitted
    from Link. For a full list of valid types and subtypes, see the `Account schema
    <https://plaid.com/docs/api/accounts#accounts-schema>`__.

    For institutions using OAuth, the filter will not affect the list of accounts shown by the bank in the OAuth
    window."""

    depository: Optional[DepositoryFilter] = UNSET
    """A filter to apply to ``depository``-type accounts"""

    credit: Optional[CreditFilter] = UNSET
    """A filter to apply to ``credit``-type accounts"""

    loan: Optional[LoanFilter] = UNSET
    """A filter to apply to ``loan``-type accounts"""

    investment: Optional[InvestmentFilter] = UNSET
    """A filter to apply to ``investment``-type accounts"""


class LinkTokenAccountFiltersDict(TypedDict):
    depository: NotRequired[DepositoryFilterDict]
    credit: NotRequired[CreditFilterDict]
    loan: NotRequired[LoanFilterDict]
    investment: NotRequired[InvestmentFilterDict]
