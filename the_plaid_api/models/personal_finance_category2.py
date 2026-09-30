from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PersonalFinanceCategory2(SdkBaseModel):
    primary: str
    """A high level category that communicates the broad category of the transaction."""

    detailed: str
    """Provides additional granularity to the primary categorization."""


class PersonalFinanceCategory2Dict(TypedDict):
    primary: str
    detailed: str
