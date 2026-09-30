from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item import Item, ItemDict
from .item_status_nullable import ItemStatusNullable, ItemStatusNullableDict


class ItemGetResponse(SdkBaseModel):
    """ItemGetResponse defines the response schema for ``/item/get`` and ``/item/webhook/update``"""

    item: Item
    """Metadata about the Item."""

    status: Optional[ItemStatusNullable] = UNSET
    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ItemGetResponseDict(TypedDict):
    item: ItemDict
    status: NotRequired[ItemStatusNullableDict]
    request_id: str
