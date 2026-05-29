
# Address 1

The address of the employee.

*This model accepts additional fields of type Any.*

## Structure

`Address1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The full city name. |
| `region` | `str` | Optional | The region or state<br>Example: `"NC"` |
| `street` | `str` | Optional | The full street address<br>Example: `"564 Main Street, APT 15"` |
| `postal_code` | `str` | Optional | 5 digit postal code. |
| `country` | `str` | Optional | The country of the address. |
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

