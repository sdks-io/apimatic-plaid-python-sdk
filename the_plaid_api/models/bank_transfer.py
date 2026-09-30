from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .bank_transfer_failure import BankTransferFailure, BankTransferFailureDict
from .bank_transfer_user import BankTransferUser, BankTransferUserDict
from .enums.achclass import AchclassOrStr
from .enums.bank_transfer_direction import BankTransferDirectionOrStr
from .enums.bank_transfer_network import BankTransferNetworkOrStr
from .enums.bank_transfer_status import BankTransferStatusOrStr
from .enums.bank_transfer_type import BankTransferTypeOrStr


class BankTransfer(SdkBaseModel):
    """Represents a bank transfer within the Bank Transfers API."""

    id: str
    """Plaid’s unique identifier for a bank transfer."""

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
    """The account ID that should be credited/debited for this bank transfer."""

    type_: BankTransferTypeOrStr = Field(alias="type")
    """The type of bank transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money
    into the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    user: BankTransferUser
    """The legal name and other information for the account holder."""

    amount: str
    """The amount of the bank transfer (decimal string with two digits of precision e.g. “10.00”)."""

    iso_currency_code: str
    """The currency of the transfer amount, e.g. "USD"
    """

    description: str
    """The description of the transfer."""

    created: RFC3339DateTime
    """The datetime when this bank transfer was created. This will be of the form ``2006-01-02T15:04:05Z``"""

    status: BankTransferStatusOrStr
    """The status of the transfer."""

    network: BankTransferNetworkOrStr
    """The network or rails used for the transfer. Valid options are ``ach``, ``same-day-ach``, or ``wire``."""

    cancellable: bool
    """When ``true``, you can still cancel this bank transfer."""

    failure_reason: BankTransferFailure
    """The failure reason if the type of this transfer is ``"failed"`` or ``"reversed"``. Null value otherwise."""

    custom_tag: str | None
    """A string containing the custom tag provided by the client in the create request. Will be null if not provided."""

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

    direction: BankTransferDirectionOrStr
    """Indicates the direction of the transfer: ``outbound`` for API-initiated transfers, or ``inbound`` for payments
    received by the FBO account."""


class BankTransferDict(TypedDict):
    id: str
    ach_class: AchclassOrStr
    account_id: str
    type_: BankTransferTypeOrStr
    user: BankTransferUserDict
    amount: str
    iso_currency_code: str
    description: str
    created: RFC3339DateTime
    status: BankTransferStatusOrStr
    network: BankTransferNetworkOrStr
    cancellable: bool
    failure_reason: BankTransferFailureDict
    custom_tag: str | None
    metadata: dict[str, str]
    origination_account_id: str
    direction: BankTransferDirectionOrStr
