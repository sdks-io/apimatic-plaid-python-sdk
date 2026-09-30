from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.decision import DecisionOrStr
from .transfer_authorization_decision_rationale import (
    TransferAuthorizationDecisionRationale,
    TransferAuthorizationDecisionRationaleDict,
)
from .transfer_authorization_proposed_transfer import (
    TransferAuthorizationProposedTransfer,
    TransferAuthorizationProposedTransferDict,
)


class TransferAuthorization(SdkBaseModel):
    """TransferAuthorization contains the authorization decision for a proposed transfer"""

    id: str
    """Plaid’s unique identifier for a transfer authorization."""

    created: str
    """The datetime representing when the authorization was created, in the format "2006-01-02T15:04:05Z"."""

    decision: DecisionOrStr
    """A decision regarding the proposed transfer.

    ``approved`` – The proposed transfer has received the end user's consent and has been approved for processing. Plaid
    has also reviewed the proposed transfer and has approved it for processing.

    ``permitted`` – Plaid was unable to fetch the information required to approve or decline the proposed transfer. You
    may proceed with the transfer, but further review is recommended. Plaid is awaiting further instructions from the
    client.

    ``declined`` – Plaid reviewed the proposed transfer and declined processing. Refer to the ``code`` field in the
    ``decision_rationale`` object for details."""

    decision_rationale: TransferAuthorizationDecisionRationale
    """The rationale for Plaid's decision regarding a proposed transfer. Will be null for ``approved`` decisions."""

    proposed_transfer: TransferAuthorizationProposedTransfer
    """Details regarding the proposed transfer."""


class TransferAuthorizationDict(TypedDict):
    id: str
    created: str
    decision: DecisionOrStr
    decision_rationale: TransferAuthorizationDecisionRationaleDict
    proposed_transfer: TransferAuthorizationProposedTransferDict
