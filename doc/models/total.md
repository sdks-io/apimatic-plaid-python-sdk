
# Total

An object representing both the current pay period and year to date amount for a category.

*This model accepts additional fields of type Any.*

## Structure

`Total`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `canonical_description` | [`CanonicalDescription`](../../doc/models/canonical-description.md) | Optional | Commonly used term to describe the line item. |
| `description` | `str` | Optional | Text of the line item as printed on the paystub. |
| `current_pay` | [`Pay`](../../doc/models/pay.md) | Optional | An object representing a monetary amount. |
| `ytd_pay` | [`Pay`](../../doc/models/pay.md) | Optional | An object representing a monetary amount. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "canonical_description": "SOCIAL SECURITY EMPLOYEE TAX",
  "description": "description0",
  "current_pay": {
    "amount": 45.16,
    "currency": "currency4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "ytd_pay": {
    "amount": 28.98,
    "currency": "currency0",
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

