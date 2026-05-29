
# Employee

Data about the employee.

*This model accepts additional fields of type Any.*

## Structure

`Employee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The name of the employee. |
| `address` | [`Address2`](../../doc/models/address-2.md) | Required | - |
| `marital_status` | `str` | Optional | Marital status of the employee. |
| `taxpayer_id` | [`TaxpayerId`](../../doc/models/taxpayer-id.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name6",
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
  "marital_status": "marital_status4",
  "taxpayer_id": {
    "id_type": "id_type8",
    "last_4_digits": "last_4_digits6",
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

