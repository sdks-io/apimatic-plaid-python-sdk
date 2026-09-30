from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_network import TransferNetworkOrStr
from .enums.transfer_status import TransferStatusOrStr
from .enums.transfer_type1 import TransferType1OrStr
from .transfer_failure import TransferFailure, TransferFailureDict
from .transfer_user_in_response import TransferUserInResponse, TransferUserInResponseDict


class Transfer(SdkBaseModel):
    """Represents a transfer within the Transfers API."""

    id: str
    """Plaid’s unique identifier for a transfer."""

    ach_class: AchclassOrStr
    """Specifies the use case of the transfer. Required for transfers on an ACH network.

    ``"arc"`` - Accounts Receivable Entry

    ``"cbr``" - Cross Border Entry

    ``"ccd"`` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    ``"cie"`` - Customer Initiated Entry

    ``"cor"`` - Automated Notification of Change

    ``"ctx"`` - Corporate Trade Exchange

    ``"iat"`` - International

    ``"mte"`` - Machine Transfer Entry

    ``"pbr"`` - Cross Border Entry

    ``"pop"`` - Point-of-Purchase Entry

    ``"pos"`` - Point-of-Sale Entry

    ``"ppd"`` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer,
    eg. bill payment

    ``"rck"`` - Re-presented Check Entry

    ``"tel"`` - Telephone-Initiated Entry

    ``"web"`` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over
    the Internet"""

    account_id: str
    """The account ID that should be credited/debited for this transfer."""

    type_: TransferType1OrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. “10.00”)."""

    description: str
    """The description of the transfer."""

    created: RFC3339DateTime
    """The datetime when this transfer was created. This will be of the form ``2006-01-02T15:04:05Z``"""

    status: TransferStatusOrStr
    """The status of the transfer."""

    network: TransferNetworkOrStr
    """The network or rails used for the transfer. Valid options are ``ach`` or ``same-day-ach``."""

    cancellable: bool
    """When ``true``, you can still cancel this transfer."""

    failure_reason: TransferFailure
    """The failure reason if the type of this transfer is ``"failed"`` or ``"reversed"``. Null value otherwise."""

    metadata: dict[str, str]
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations
    apply:
    - The JSON values must be Strings (no nested JSON objects allowed)
    - Only ASCII characters may be used
    - Maximum of 50 key/value pairs
    - Maximum key length of 40 characters
    - Maximum value length of 500 characters"""

    origination_account_id: str
    """Plaid’s unique identifier for the origination account that was used for this transfer."""


class TransferDict(TypedDict):
    id: str
    ach_class: AchclassOrStr
    account_id: str
    type_: TransferType1OrStr
    user: TransferUserInResponseDict
    amount: str
    description: str
    created: RFC3339DateTime
    status: TransferStatusOrStr
    network: TransferNetworkOrStr
    cancellable: bool
    failure_reason: TransferFailureDict
    metadata: dict[str, str]
    origination_account_id: str
