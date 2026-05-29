
# Student Repayment Plan

An object representing the repayment plan for the student loan

*This model accepts additional fields of type Any.*

## Structure

`StudentRepaymentPlan`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | The description of the repayment plan as provided by the servicer. |
| `mtype` | [`Type3`](../../doc/models/type-3.md) | Required | The type of the repayment plan. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "description": "description8",
  "type": "graduated",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

