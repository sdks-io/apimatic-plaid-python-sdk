from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .income_verification_precheck_employer import (
    IncomeVerificationPrecheckEmployer,
    IncomeVerificationPrecheckEmployerDict,
)
from .income_verification_precheck_military_info import (
    IncomeVerificationPrecheckMilitaryInfo,
    IncomeVerificationPrecheckMilitaryInfoDict,
)
from .income_verification_precheck_user import IncomeVerificationPrecheckUser, IncomeVerificationPrecheckUserDict


class IncomeVerificationPrecheckRequest(SdkBaseModel):
    """IncomeVerificationPrecheckRequest defines the request schema for ``/income/verification/precheck``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user: Optional[IncomeVerificationPrecheckUser] = UNSET
    employer: Optional[IncomeVerificationPrecheckEmployer] = UNSET
    transactions_access_token: OptionalNullable[str] = UNSET
    """The access token associated with the Item data is being requested for."""

    us_military_info: Optional[IncomeVerificationPrecheckMilitaryInfo] = UNSET


class IncomeVerificationPrecheckRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user: NotRequired[IncomeVerificationPrecheckUserDict]
    employer: NotRequired[IncomeVerificationPrecheckEmployerDict]
    transactions_access_token: NotRequired[str | None]
    us_military_info: NotRequired[IncomeVerificationPrecheckMilitaryInfoDict]
