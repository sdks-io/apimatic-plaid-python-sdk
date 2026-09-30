from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class ProcessorBalanceGetRequestOptions(SdkBaseModel):
    """An optional object to filter ``/processor/balance/get`` results."""

    min_last_updated_datetime: Optional[RFC3339DateTime] = UNSET
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (``YYYY-MM-DDTHH:mm:ssZ``) indicating the
    oldest acceptable balance when making a request to ``/accounts/balance/get``.

    If the balance that is pulled for ``ins_128026`` (Capital One) is older than the given timestamp, an
    ``INVALID_REQUEST`` error with the code of ``LAST_UPDATED_DATETIME_OUT_OF_RANGE`` will be returned with the most
    recent timestamp for the requested account contained in the response.

    This field is only used when the institution is ``ins_128026`` (Capital One), in which case a value must be provided
    or an ``INVALID_REQUEST`` error with the code of ``INVALID_FIELD`` will be returned. For all other institutions,
    this field is ignored."""


class ProcessorBalanceGetRequestOptionsDict(TypedDict):
    min_last_updated_datetime: NotRequired[RFC3339DateTime]
