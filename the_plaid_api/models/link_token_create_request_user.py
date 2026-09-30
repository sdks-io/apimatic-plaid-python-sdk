from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel


class LinkTokenCreateRequestUser(SdkBaseModel):
    """An object specifying information about the end user who will be linking their account."""

    client_user_id: str
    """A unique ID representing the end user. Typically this will be a user ID number from your application. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``. It
    is currently used as a means of searching logs for the given user in the Plaid Dashboard."""

    legal_name: Optional[str] = UNSET
    """The user's full legal name. This is an optional field used in the `returning user experience
    <https://plaid.com/docs/link/returning-user>`__ to associate Items to the user."""

    phone_number: Optional[str] = UNSET
    """The user's phone number in `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format. This field is optional, but
    required to enable the `returning user experience <https://plaid.com/docs/link/returning-user>`__."""

    phone_number_verified_time: Optional[RFC3339DateTime] = UNSET
    """The date and time the phone number was verified in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (``YYYY-MM-DDThh:mm:ssZ``). This field is optional, but required to enable any `returning user experience
    <https://plaid.com/docs/link/returning-user>`__.

     Only pass a verification time for a phone number that you have verified. If you have performed verification but
        don’t have the time, you may supply a signal value of the start of the UNIX epoch.

     Example: ``2020-01-01T00:00:00Z``"""

    email_address: Optional[str] = UNSET
    """The user's email address. This field is optional, but required to enable the `pre-authenticated returning user
    flow <https://plaid.com/docs/link/returning-user/#enabling-the-returning-user-experience>`__."""

    email_address_verified_time: Optional[RFC3339DateTime] = UNSET
    """The date and time the email address was verified in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (``YYYY-MM-DDThh:mm:ssZ``). This is an optional field used in the `returning user experience
    <https://plaid.com/docs/link/returning-user>`__.

     Only pass a verification time for an email address that you have verified. If you have performed verification but
        don’t have the time, you may supply a signal value of the start of the UNIX epoch.

     Example: ``2020-01-01T00:00:00Z``"""

    ssn: Optional[str] = UNSET
    """To be provided in the format "ddd-dd-dddd". This field is optional and will support not-yet-implemented
    functionality for new products."""

    date_of_birth: Optional[Date] = UNSET
    """To be provided in the format "yyyy-mm-dd". This field is optional and will support not-yet-implemented
    functionality for new products."""


class LinkTokenCreateRequestUserDict(TypedDict):
    client_user_id: str
    legal_name: NotRequired[str]
    phone_number: NotRequired[str]
    phone_number_verified_time: NotRequired[RFC3339DateTime]
    email_address: NotRequired[str]
    email_address_verified_time: NotRequired[RFC3339DateTime]
    ssn: NotRequired[str]
    date_of_birth: NotRequired[Date]
