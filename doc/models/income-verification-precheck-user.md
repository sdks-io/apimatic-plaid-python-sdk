
# Income Verification Precheck User

*This model accepts additional fields of type Any.*

## Structure

`IncomeVerificationPrecheckUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The user's first name |
| `last_name` | `str` | Optional | The user's last name |
| `email_address` | `str` | Optional | The user's email address |
| `home_address` | [`AddressData1`](../../doc/models/address-data-1.md) | Optional | Data about the components comprising an address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "first_name": "first_name4",
  "last_name": "last_name2",
  "email_address": "email_address8",
  "home_address": {
    "city": "city0",
    "region": "region6",
    "street": "street0",
    "postal_code": "postal_code2",
    "country": "country4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

