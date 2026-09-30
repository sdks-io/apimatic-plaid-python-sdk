from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .signal_evaluate_core_attributes import SignalEvaluateCoreAttributes, SignalEvaluateCoreAttributesDict
from .signal_evaluate_scores import SignalEvaluateScores, SignalEvaluateScoresDict


class SignalEvaluateResponse(SdkBaseModel):
    """SignalEvaluateResponse defines the response schema for ``/signal/income/evaluate``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    scores: SignalEvaluateScores
    """Risk scoring details broken down by risk category."""

    core_attributes: SignalEvaluateCoreAttributes
    """The core attributes object contains additional data that can be used to assess the ACH return risk, such as past
    ACH return events, balance/transaction history, the Item’s connection history in the Plaid network, and identity
    change history."""


class SignalEvaluateResponseDict(TypedDict):
    request_id: str
    scores: SignalEvaluateScoresDict
    core_attributes: SignalEvaluateCoreAttributesDict
