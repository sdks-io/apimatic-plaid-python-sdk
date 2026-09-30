from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SignalReturnReportRequest(SdkBaseModel):
    """SignalReturnReportRequest defines the request schema for ``/signal/return/report``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_transaction_id: str
    """Must be the same as the ``client_transaction_id`` supplied when calling ``/signal/evaluate``"""

    return_code: str
    """Must be a valid ACH return code (e.g. "R01")"""


class SignalReturnReportRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    client_transaction_id: str
    return_code: str
