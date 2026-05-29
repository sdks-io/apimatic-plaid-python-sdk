
# Address 2

*This model accepts additional fields of type Any.*

## Structure

`Address2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The full city name. |
| `street` | `str` | Optional | The listed street address. |
| `line_1` | `str` | Optional | Street address line 1. |
| `line_2` | `str` | Optional | Street address line 2. |
| `postal_code` | `str` | Optional | 5 digit postal code. |
| `region` | `str` | Optional | The region or state<br>Example: `"NC"` |
| `state_code` | `str` | Optional | The region or state<br>Example: `"NC"` |
| `country` | `str` | Optional | The country of the address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "city": "city0",
  "street": "street0",
  "line1": "line12",
  "line2": "line24",
  "postal_code": "postal_code2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

