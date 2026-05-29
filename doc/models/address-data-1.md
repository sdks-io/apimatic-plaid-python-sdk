
# Address Data 1

Data about the components comprising an address.

*This model accepts additional fields of type Any.*

## Structure

`AddressData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The full city name |
| `region` | `str` | Optional | The region or state<br>Example: `"NC"` |
| `street` | `str` | Optional | The full street address<br>Example: `"564 Main Street, APT 15"` |
| `postal_code` | `str` | Optional | The postal code |
| `country` | `str` | Optional | The ISO 3166-1 alpha-2 country code |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "city": "city4",
  "region": "region2",
  "street": "street6",
  "postal_code": "postal_code8",
  "country": "country0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

