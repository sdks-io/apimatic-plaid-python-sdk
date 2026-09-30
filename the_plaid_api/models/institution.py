from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .auth_metadata import AuthMetadata, AuthMetadataDict
from .enums.country_code import CountryCodeOrStr
from .enums.products import ProductsOrStr
from .institution_status import InstitutionStatus, InstitutionStatusDict
from .payment_initiation_metadata import PaymentInitiationMetadata, PaymentInitiationMetadataDict


class Institution(SdkBaseModel):
    """Details relating to a specific financial institution"""

    institution_id: str
    """Unique identifier for the institution"""

    name: str
    """The official name of the institution"""

    products: list[ProductsOrStr]
    """A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth
    will return ``auth`` in the product array; institutions that do not list ``auth`` may still support other Auth
    methods such as Instant Match or Automated Micro-deposit Verification. For more details, see `Full Auth coverage
    <https://plaid.com/docs/auth/coverage/>`__."""

    country_codes: list[CountryCodeOrStr]
    """A list of the country codes supported by the institution."""

    url: OptionalNullable[str] = UNSET
    """The URL for the institution's website"""

    primary_color: OptionalNullable[str] = UNSET
    """Hexadecimal representation of the primary color used by the institution"""

    logo: OptionalNullable[str] = UNSET
    """Base64 encoded representation of the institution's logo"""

    routing_numbers: list[str | None]
    """A partial list of routing numbers associated with the institution. This list is provided for the purpose of
    looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of
    routing numbers for an institution."""

    oauth: bool
    """Indicates that the institution has an OAuth login flow. This is primarily relevant to institutions with European
    country codes."""

    status: Optional[InstitutionStatus] = UNSET
    """The status of an institution is determined by the health of its Item logins, Transactions updates, Investments
    updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and
    Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough
    traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate
    data.

    Institution status is accessible in the Dashboard and via the API using the ``/institutions/get_by_id`` endpoint
    with the ``include_status`` option set to true. Note that institution status is not available in the Sandbox
    environment."""

    payment_initiation_metadata: Optional[PaymentInitiationMetadata] = UNSET
    """Metadata that captures what specific payment configurations an institution supports when making Payment
    Initiation requests."""

    auth_metadata: Optional[AuthMetadata] = UNSET
    """Metadata that captures information about the Auth features of an institution."""


class InstitutionDict(TypedDict):
    institution_id: str
    name: str
    products: list[ProductsOrStr]
    country_codes: list[CountryCodeOrStr]
    url: NotRequired[str | None]
    primary_color: NotRequired[str | None]
    logo: NotRequired[str | None]
    routing_numbers: list[str | None]
    oauth: bool
    status: NotRequired[InstitutionStatusDict]
    payment_initiation_metadata: NotRequired[PaymentInitiationMetadataDict]
    auth_metadata: NotRequired[AuthMetadataDict]
