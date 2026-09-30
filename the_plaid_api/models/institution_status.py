from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .health_incident import HealthIncident, HealthIncidentDict
from .product_status import ProductStatus, ProductStatusDict


class InstitutionStatus(SdkBaseModel):
    """The status of an institution is determined by the health of its Item logins, Transactions updates, Investments
    updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and
    Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough
    traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate
    data.

    Institution status is accessible in the Dashboard and via the API using the ``/institutions/get_by_id`` endpoint
    with the ``include_status`` option set to true. Note that institution status is not available in the Sandbox
    environment."""

    item_logins: ProductStatus
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    transactions_updates: ProductStatus
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    auth: ProductStatus
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    balance: ProductStatus
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    identity: ProductStatus
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    investments_updates: ProductStatus
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    liabilities_updates: Optional[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    liabilities: Optional[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    investments: Optional[ProductStatus] = UNSET
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    health_incidents: Optional[list[HealthIncident | None]] = UNSET
    """Details of recent health incidents associated with the institution."""


class InstitutionStatusDict(TypedDict):
    item_logins: ProductStatusDict
    transactions_updates: ProductStatusDict
    auth: ProductStatusDict
    balance: ProductStatusDict
    identity: ProductStatusDict
    investments_updates: ProductStatusDict
    liabilities_updates: NotRequired[ProductStatusDict]
    liabilities: NotRequired[ProductStatusDict]
    investments: NotRequired[ProductStatusDict]
    health_incidents: NotRequired[list[HealthIncidentDict | None]]
