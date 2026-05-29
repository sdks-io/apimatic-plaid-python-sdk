
# Signal User

Details about the end user initiating the transaction (i.e., the account holder).

*This model accepts additional fields of type Any.*

## Structure

`SignalUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`SignalPersonName`](../../doc/models/signal-person-name.md) | Optional | The user's legal name |
| `phone_number` | `str` | Optional | The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567" |
| `email_address` | `str` | Optional | The user's email address. |
| `address` | [`AddressData1`](../../doc/models/address-data-1.md) | Optional | Data about the components comprising an address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": {
    "prefix": "prefix8",
    "given_name": "given_name2",
    "middle_name": "middle_name0",
    "family_name": "family_name4",
    "suffix": "suffix0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "phone_number": "phone_number6",
  "email_address": "email_address6",
  "address": {
    "city": "city6",
    "region": "region2",
    "street": "street6",
    "postal_code": "postal_code8",
    "country": "country0",
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

