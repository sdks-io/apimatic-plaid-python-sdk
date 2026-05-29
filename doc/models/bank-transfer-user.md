
# Bank Transfer User

The legal name and other information for the account holder.

*This model accepts additional fields of type Any.*

## Structure

`BankTransferUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_name` | `str` | Required | The account holder’s full legal name. If the transfer description is `ccd`, this should be the business name of the account holder. |
| `email_address` | `str` | Optional | The account holder’s email. |
| `routing_number` | `str` | Optional | The account holder's routing number. This field is only used in response data. Do not provide this field when making requests. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "legal_name": "legal_name8",
  "email_address": "email_address8",
  "routing_number": "routing_number4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

