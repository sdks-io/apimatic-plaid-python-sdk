from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SignalDecisionReportRequest(SdkBaseModel):
    """SignalDecisionReportRequest defines the request schema for ``/signal/decision/report``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_transaction_id: str
    """Must be the same as the ``client_transaction_id`` supplied when calling ``/signal/evaluate``"""

    initiated: bool
    """``true`` if the ACH transaction was initiated, ``false`` otherwise."""


class SignalDecisionReportRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    client_transaction_id: str
    initiated: bool
