
# Transaction Location

A representation of where a transaction took place

*This model accepts additional fields of type Any.*

## Structure

`TransactionLocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `str` | Required | The street address where the transaction occurred. |
| `city` | `str` | Required | The city where the transaction occurred. |
| `region` | `str` | Required | The region or state where the transaction occurred. |
| `postal_code` | `str` | Required | The postal code where the transaction occurred. |
| `country` | `str` | Required | The ISO 3166-1 alpha-2 country code where the transaction occurred. |
| `lat` | `float` | Required | The latitude where the transaction occurred. |
| `lon` | `float` | Required | The longitude where the transaction occurred. |
| `store_number` | `str` | Required | The merchant defined store number where the transaction occurred. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "address": "address8",
  "city": "city8",
  "region": "region8",
  "postal_code": "postal_code4",
  "country": "country6",
  "lat": 198.3,
  "lon": 224.6,
  "store_number": "store_number8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

