from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.state import StateOrStr
from .enums.switch_method import SwitchMethodOrStr


class DepositSwitchGetResponse(SdkBaseModel):
    """DepositSwitchGetResponse defines the response schema for ``/deposit_switch/get``"""

    deposit_switch_id: str
    """The ID of the deposit switch."""

    target_account_id: str | None
    """The ID of the bank account the direct deposit was switched to."""

    target_item_id: str | None
    """The ID of the Item the direct deposit was switched to."""

    state: StateOrStr
    """The state, or status, of the deposit switch.

    - ``initialized`` – The deposit switch has been initialized with the user entering the information required to
        submit the deposit switch request.

    - ``processing`` – The deposit switch request has been submitted and is being processed.

    - ``completed`` – The user's employer has fulfilled the deposit switch request.

    - ``error`` – There was an error processing the deposit switch request."""

    switch_method: Optional[SwitchMethodOrStr] = UNSET
    """The method used to make the deposit switch.

    - ``instant`` – User instantly switched their direct deposit to a new or existing bank account by connecting their
        payroll or employer account.

    - ``mail`` – User requested that Plaid contact their employer by mail to make the direct deposit switch.

    - ``pdf`` – User generated a PDF or email to be sent to their employer with the information necessary to make the
        deposit switch.'"""

    account_has_multiple_allocations: bool | None
    """When ``true``, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the
    target account. Always ``null`` if the deposit switch has not been completed."""

    is_allocated_remainder: bool | None
    """When ``true``, the target account is allocated the remainder of direct deposit after all other allocations have
    been deducted. When ``false``, user’s direct deposit is allocated as a percent or amount. Always ``null`` if the
    deposit switch has not been completed."""

    percent_allocated: float | None
    """The percentage of direct deposit allocated to the target account. Always ``null`` if the target account is not
    allocated a percentage or if the deposit switch has not been completed or if ``is_allocated_remainder`` is true."""

    amount_allocated: float | None
    """The dollar amount of direct deposit allocated to the target account. Always ``null`` if the target account is not
    allocated an amount or if the deposit switch has not been completed."""

    employer_name: OptionalNullable[str] = UNSET
    """The name of the employer selected by the user. If the user did not select an employer, the value returned is
    ``null``."""

    employer_id: OptionalNullable[str] = UNSET
    """The ID of the employer selected by the user. If the user did not select an employer, the value returned is
    ``null``."""

    institution_name: OptionalNullable[str] = UNSET
    """The name of the institution selected by the user. If the user did not select an institution, the value returned
    is ``null``."""

    institution_id: OptionalNullable[str] = UNSET
    """The ID of the institution selected by the user. If the user did not select an institution, the value returned is
    ``null``."""

    date_created: Date
    """`ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ date the deposit switch was created."""

    date_completed: Date | None
    """`ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ date the deposit switch was completed. Always ``null`` if the
    deposit switch has not been completed."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class DepositSwitchGetResponseDict(TypedDict):
    deposit_switch_id: str
    target_account_id: str | None
    target_item_id: str | None
    state: StateOrStr
    switch_method: NotRequired[SwitchMethodOrStr]
    account_has_multiple_allocations: bool | None
    is_allocated_remainder: bool | None
    percent_allocated: float | None
    amount_allocated: float | None
    employer_name: NotRequired[str | None]
    employer_id: NotRequired[str | None]
    institution_name: NotRequired[str | None]
    institution_id: NotRequired[str | None]
    date_created: Date
    date_completed: Date | None
    request_id: str
