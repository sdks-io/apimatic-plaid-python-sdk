
# Address Data

Data about the components comprising an address.

*This model accepts additional fields of type Any.*

## Structure

`AddressData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Required | The full city name |
| `region` | `str` | Required | The region or state<br>Example: `"NC"` |
| `street` | `str` | Required | The full street address<br>Example: `"564 Main Street, APT 15"` |
| `postal_code` | `str` | Required | The postal code |
| `country` | `str` | Required | The ISO 3166-1 alpha-2 country code |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "city": "city4",
  "region": "region0",
  "street": "street4",
  "postal_code": "postal_code6",
  "country": "country8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

