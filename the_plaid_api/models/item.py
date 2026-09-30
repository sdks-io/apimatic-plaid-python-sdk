from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.products import ProductsOrStr
from .enums.update_type import UpdateTypeOrStr
from .error import Error, ErrorDict


class Item(SdkBaseModel):
    """Metadata about the Item."""

    item_id: str
    """The Plaid Item ID. The ``item_id`` is always unique; linking the same account at the same institution twice will
    result in two Items with different ``item_id`` values. Like all Plaid identifiers, the ``item_id`` is
    case-sensitive."""

    institution_id: OptionalNullable[str] = UNSET
    """The Plaid Institution ID associated with the Item. Field is ``null`` for Items created via Same Day
    Micro-deposits."""

    webhook: str | None
    """The URL registered to receive webhooks for the Item."""

    error: Error
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    available_products: list[ProductsOrStr]
    """A list of products available for the Item that have not yet been accessed."""

    billed_products: list[ProductsOrStr]
    """A list of products that have been billed for the Item. Note - ``billed_products`` is populated in all
    environments but only requests in Production are billed."""

    consent_expiration_time: RFC3339DateTime | None
    """The RFC 3339 timestamp after which the consent provided by the end user will expire. Upon consent expiration, the
    item will enter the ``ITEM_LOGIN_REQUIRED`` error state. To circumvent the ``ITEM_LOGIN_REQUIRED`` error and
    maintain continuous consent, the end user can reauthenticate via Link’s update mode in advance of the consent
    expiration time.

    Note - This is only relevant for certain OAuth-based institutions. For all other institutions, this field will be
    null."""

    update_type: UpdateTypeOrStr
    """Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some
    forms of two-factor authentication.

    ``background`` - Item can be updated in the background

    ``user_present_required`` - Item requires user interaction to be updated"""


class ItemDict(TypedDict):
    item_id: str
    institution_id: NotRequired[str | None]
    webhook: str | None
    error: ErrorDict
    available_products: list[ProductsOrStr]
    billed_products: list[ProductsOrStr]
    consent_expiration_time: RFC3339DateTime | None
    update_type: UpdateTypeOrStr
