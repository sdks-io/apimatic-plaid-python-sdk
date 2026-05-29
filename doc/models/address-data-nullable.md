
# Address Data Nullable

*This model accepts additional fields of type Any.*

## Structure

`AddressDataNullable`

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
  "city": "city2",
  "region": "region8",
  "street": "street2",
  "postal_code": "postal_code4",
  "country": "country6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

