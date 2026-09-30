from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_type1 import TransferType1OrStr
from .transfer_user_in_response import TransferUserInResponse, TransferUserInResponseDict


class TransferAuthorizationProposedTransfer(SdkBaseModel):
    """Details regarding the proposed transfer."""

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
    """The Plaid ``account_id`` for the account that will be debited or credited."""

    type_: TransferType1OrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    user: TransferUserInResponse
    """The legal name and other information for the account holder."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. “10.00”)."""

    network: str
    """The network or rails used for the transfer."""

    origination_account_id: str
    """Plaid's unique identifier for the origination account that was used for this transfer."""


class TransferAuthorizationProposedTransferDict(TypedDict):
    ach_class: AchclassOrStr
    account_id: str
    type_: TransferType1OrStr
    user: TransferUserInResponseDict
    amount: str
    network: str
    origination_account_id: str
