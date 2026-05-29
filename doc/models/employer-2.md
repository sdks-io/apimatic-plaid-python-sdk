
# Employer 2

*This model accepts additional fields of type Any.*

## Structure

`Employer2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The name of the employer on the paystub. |
| `address` | [`Address2`](../../doc/models/address-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name8",
  "address": {
    "city": "city6",
    "street": "street6",
    "line1": "line18",
    "line2": "line20",
    "postal_code": "postal_code8",
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

