from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class Pslfstatus(SdkBaseModel):
    """Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned
    if the institution is Fedloan (``ins_116527``)."""

    estimated_eligibility_date: Date | None
    """The estimated date borrower will have completed 120 qualifying monthly payments. Returned in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    payments_made: float | None
    """The number of qualifying payments that have been made."""

    payments_remaining: float | None
    """The number of qualifying payments remaining."""


class PslfstatusDict(TypedDict):
    estimated_eligibility_date: Date | None
    payments_made: float | None
    payments_remaining: float | None
