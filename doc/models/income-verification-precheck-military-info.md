
# Income Verification Precheck Military Info

*This model accepts additional fields of type Any.*

## Structure

`IncomeVerificationPrecheckMilitaryInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_active_duty` | `bool` | Optional | Is the user currently active duty in the US military |
| `branch` | [`Branch`](../../doc/models/branch.md) | Optional | If the user is currently serving in the US military, the branch of the military they are serving in |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "is_active_duty": false,
  "branch": "NAVY",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

