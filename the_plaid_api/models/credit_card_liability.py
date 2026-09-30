from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .apr import Apr, AprDict


class CreditCardLiability(SdkBaseModel):
    """An object representing a credit card account."""

    account_id: str | None
    """The ID of the account that this liability belongs to."""

    aprs: list[Apr]
    """The various interest rates that apply to the account."""

    is_overdue: bool | None
    """true if a payment is currently overdue. Availability for this field is limited."""

    last_payment_amount: float
    """The amount of the last payment."""

    last_payment_date: Date
    """The date of the last payment. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (YYYY-MM-DD). Availability for this field is limited."""

    last_statement_issue_date: Date
    """The date of the last statement. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format (YYYY-MM-DD)."""

    minimum_payment_amount: float
    """The minimum payment due for the next billing cycle."""

    next_payment_due_date: Date | None
    """The due date for the next payment. The due date is ``null`` if a payment is not expected. Dates are returned in
    an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""


class CreditCardLiabilityDict(TypedDict):
    account_id: str | None
    aprs: list[AprDict]
    is_overdue: bool | None
    last_payment_amount: float
    last_payment_date: Date
    last_statement_issue_date: Date
    minimum_payment_amount: float
    next_payment_due_date: Date | None
