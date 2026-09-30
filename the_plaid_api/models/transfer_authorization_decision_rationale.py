from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.code import CodeOrStr


class TransferAuthorizationDecisionRationale(SdkBaseModel):
    """The rationale for Plaid's decision regarding a proposed transfer. Will be null for ``approved`` decisions."""

    code: CodeOrStr
    """A code representing the rationale for permitting or declining the proposed transfer. Possible values are:

    ``NSF`` – Transaction likely to result in a return due to insufficient funds.

    ``RISK`` - Transaction is high-risk.

    ``MANUALLY_VERIFIED_ITEM`` – Item created via same-day micro deposits, limited information available. Plaid can only
    offer ``permitted`` as a transaction decision.

    ``LOGIN_REQUIRED`` – Unable to collect the account information required for an authorization decision due to Item
    staleness. Can be rectified using Link update mode.

    ``ERROR`` – Unable to collect the account information required for an authorization decision due to an error."""

    description: str
    """A human-readable description of the code associated with a permitted transfer or transfer decline."""


class TransferAuthorizationDecisionRationaleDict(TypedDict):
    code: CodeOrStr
    description: str
