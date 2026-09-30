from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .signal_evaluate_device import SignalEvaluateDevice, SignalEvaluateDeviceDict
from .signal_user import SignalUser, SignalUserDict


class SignalEvaluateRequest(SdkBaseModel):
    """SignalEvaluateRequest defines the request schema for ``/signal/evaluate``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item data is being requested for."""

    account_id: str
    """The ``account_id`` of the account whose verification status is to be modified"""

    client_transaction_id: str
    """The unique ID that you would like to use to refer to this transaction. For your convenience mapping your internal
    data, you could use your internal ID/identifier for this transaction. The max length for this field is 36
    characters."""

    amount: float
    """The transaction amount, in USD (e.g. ``102.05``)"""

    client_user_id: Optional[str] = UNSET
    """A unique ID that identifies the end user in your system. This ID is used to correlate requests by a user with
    multiple Items. The max length for this field is 36 characters."""

    user: Optional[SignalUser] = UNSET
    """Details about the end user initiating the transaction (i.e., the account holder)."""

    device: Optional[SignalEvaluateDevice] = UNSET
    """Details about the end user's device"""


class SignalEvaluateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    account_id: str
    client_transaction_id: str
    amount: float
    client_user_id: NotRequired[str]
    user: NotRequired[SignalUserDict]
    device: NotRequired[SignalEvaluateDeviceDict]
