from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.achclass import AchclassOrStr
from .enums.transfer_network import TransferNetworkOrStr
from .enums.transfer_type1 import TransferType1OrStr
from .transfer_user_in_request import TransferUserInRequest, TransferUserInRequestDict


class TransferCreateRequest(SdkBaseModel):
    """Defines the request schema for ``/transfer/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    idempotency_key: str
    """A random key provided by the client, per unique transfer. Maximum of 50 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    For example, if a request to create a transfer fails due to a network connection error, you can retry the request
    with the same idempotency key to guarantee that only a single transfer is created."""

    access_token: str
    """The Plaid ``access_token`` for the account that will be debited or credited."""

    account_id: str
    """The Plaid ``account_id`` for the account that will be debited or credited."""

    authorization_id: str
    """Plaid’s unique identifier for a transfer authorization."""

    type_: TransferType1OrStr = Field(alias="type")
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    network: TransferNetworkOrStr
    """The network or rails used for the transfer. Valid options are ``ach`` or ``same-day-ach``."""

    amount: str
    """The amount of the transfer (decimal string with two digits of precision e.g. “10.00”)."""

    description: str
    """The transfer description. Maximum of 10 characters."""

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

    metadata: Optional[dict[str, str]] = UNSET
    """The Metadata object is a mapping of client-provided string fields to any string value. The following limitations
    apply:
    - The JSON values must be Strings (no nested JSON objects allowed)
    - Only ASCII characters may be used
    - Maximum of 50 key/value pairs
    - Maximum key length of 40 characters
    - Maximum value length of 500 characters"""

    origination_account_id: OptionalNullable[str] = UNSET
    """Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination
    account, this value must be specified."""


class TransferCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    idempotency_key: str
    access_token: str
    account_id: str
    authorization_id: str
    type_: TransferType1OrStr
    network: TransferNetworkOrStr
    amount: str
    description: str
    ach_class: AchclassOrStr
    user: TransferUserInRequestDict
    metadata: NotRequired[dict[str, str]]
    origination_account_id: NotRequired[str | None]
