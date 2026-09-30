from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_network import TransferNetworkOrStr
from .enums.transfer_type1 import TransferType1OrStr
from .transfer_authorization_device import TransferAuthorizationDevice, TransferAuthorizationDeviceDict
from .transfer_user_in_request import TransferUserInRequest, TransferUserInRequestDict


class TransferAuthorizationCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/authorization/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The Plaid ``access_token`` for the account that will be debited or credited."""

    account_id: str
    """The Plaid ``account_id`` for the account that will be debited or credited."""

    type_: TransferType1OrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    network: TransferNetworkOrStr
    """The network or rails used for the transfer. Valid options are ``ach`` or ``same-day-ach``."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. “10.00”)."""

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

    user: TransferUserInRequest
    """The legal name and other information for the account holder."""

    device: Optional[TransferAuthorizationDevice] = UNSET
    """Information about the device being used to initiate the authorization."""

    origination_account_id: Optional[str] = UNSET
    """Plaid's unique identifier for the origination account for this authorization. If not specified, the default
    account will be used."""


class TransferAuthorizationCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    account_id: str
    type_: TransferType1OrStr
    network: TransferNetworkOrStr
    amount: str
    ach_class: AchclassOrStr
    user: TransferUserInRequestDict
    device: NotRequired[TransferAuthorizationDeviceDict]
    origination_account_id: NotRequired[str]
