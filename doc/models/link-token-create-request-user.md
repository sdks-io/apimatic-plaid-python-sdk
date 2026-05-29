
# Link Token Create Request User

An object specifying information about the end user who will be linking their account.

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenCreateRequestUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_user_id` | `str` | Required | A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`. It is currently used as a means of searching logs for the given user in the Plaid Dashboard. |
| `legal_name` | `str` | Optional | The user's full legal name. This is an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user) to associate Items to the user. |
| `phone_number` | `str` | Optional | The user's phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. This field is optional, but required to enable the [returning user experience](https://plaid.com/docs/link/returning-user). |
| `phone_number_verified_time` | `datetime` | Optional | The date and time the phone number was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This field is optional, but required to enable any [returning user experience](https://plaid.com/docs/link/returning-user).<br><br>Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.<br><br>Example: `2020-01-01T00:00:00Z` |
| `email_address` | `str` | Optional | The user's email address. This field is optional, but required to enable the [pre-authenticated returning user flow](https://plaid.com/docs/link/returning-user/#enabling-the-returning-user-experience). |
| `email_address_verified_time` | `datetime` | Optional | The date and time the email address was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This is an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user).<br><br>Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.<br><br>Example: `2020-01-01T00:00:00Z` |
| `ssn` | `str` | Optional | To be provided in the format "ddd-dd-dddd". This field is optional and will support not-yet-implemented functionality for new products. |
| `date_of_birth` | `date` | Optional | To be provided in the format "yyyy-mm-dd". This field is optional and will support not-yet-implemented functionality for new products. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_user_id": "client_user_id0",
  "legal_name": "legal_name4",
  "phone_number": "phone_number4",
  "phone_number_verified_time": "2016-03-13T12:52:32.123Z",
  "email_address": "email_address4",
  "email_address_verified_time": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

