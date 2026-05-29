
# Institutions Search Account Filter

*This model accepts additional fields of type Any.*

## Structure

`InstitutionsSearchAccountFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loan` | [`List[AccountSubtype]`](../../doc/models/account-subtype.md) | Optional | - |
| `depository` | [`List[AccountSubtype]`](../../doc/models/account-subtype.md) | Optional | - |
| `credit` | [`List[AccountSubtype]`](../../doc/models/account-subtype.md) | Optional | - |
| `investment` | [`List[AccountSubtype]`](../../doc/models/account-subtype.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "loan": [
    "cd",
    "paypal"
  ],
  "depository": [
    "retirement",
    "roth",
    "roth 401k"
  ],
  "credit": [
    "rrsp",
    "sep ira"
  ],
  "investment": [
    "construction"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

