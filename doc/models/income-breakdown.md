
# Income Breakdown

An object representing a breakdown of the different income types on the paystub.

*This model accepts additional fields of type Any.*

## Structure

`IncomeBreakdown`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type5`](../../doc/models/type-5.md) | Required | The type of income. Possible values include:<br>`"regular"`: regular income<br>`"overtime"`: overtime income<br>`"bonus"`: bonus income |
| `rate` | `float` | Required | The hourly rate at which the income is paid. |
| `hours` | `float` | Required | The number of hours logged for this income for this pay period. |
| `total` | `float` | Required | The total pay for this pay period. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "regular",
  "rate": 190.0,
  "hours": 102.08,
  "total": 23.2,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

