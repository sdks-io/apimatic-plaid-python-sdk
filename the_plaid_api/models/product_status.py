from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.status import StatusOrStr
from .status_breakdown import StatusBreakdown, StatusBreakdownDict


class ProductStatus(SdkBaseModel):
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    status: StatusOrStr
    """``HEALTHY``: the majority of requests are successful ``DEGRADED``: only some requests are successful ``DOWN``:
    all requests are failing"""

    last_status_change: RFC3339DateTime
    """`ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ formatted timestamp of the last status change for the
    institution."""

    breakdown: StatusBreakdown
    """A detailed breakdown of the institution's performance for a request type. The values for ``success``,
    ``error_plaid``, and ``error_institution`` sum to 1."""


class ProductStatusDict(TypedDict):
    status: StatusOrStr
    last_status_change: RFC3339DateTime
    breakdown: StatusBreakdownDict
