
# Mortgage Property Address

Object containing fields describing property address.

*This model accepts additional fields of type Any.*

## Structure

`MortgagePropertyAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Required | The city name. |
| `country` | `str` | Required | The ISO 3166-1 alpha-2 country code. |
| `postal_code` | `str` | Required | The five or nine digit postal code. |
| `region` | `str` | Required | The region or state (example "NC"). |
| `street` | `str` | Required | The full street address (example "564 Main Street, Apt 15"). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "city": "city6",
  "country": "country0",
  "postal_code": "postal_code8",
  "region": "region2",
  "street": "street6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

