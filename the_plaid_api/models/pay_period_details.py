from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class PayPeriodDetails(SdkBaseModel):
    """Details about the pay period."""

    start_date: Date | None
    """The pay period start date, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format: "yyyy-mm-dd"."""

    end_date: Date | None
    """The pay period end date, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format: "yyyy-mm-dd"."""

    pay_day: Date | None
    """The date on which the paystub was issued, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    ("yyyy-mm-dd")."""

    gross_earnings: float | None
    """Total earnings before tax."""

    check_amount: float | None
    """The net amount of the paycheck."""


class PayPeriodDetailsDict(TypedDict):
    start_date: Date | None
    end_date: Date | None
    pay_day: Date | None
    gross_earnings: float | None
    check_amount: float | None
