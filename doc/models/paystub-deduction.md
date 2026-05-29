
# Paystub Deduction

*This model accepts additional fields of type Any.*

## Structure

`PaystubDeduction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | The description of the deduction, as provided on the paystub. For example: `"401(k)"`, `"FICA MED TAX"`. |
| `is_pretax` | `bool` | Required | `true` if the deduction is pre-tax; `false` otherwise. |
| `total` | `float` | Required | The amount of the deduction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "type2",
  "is_pretax": false,
  "total": 221.52,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

