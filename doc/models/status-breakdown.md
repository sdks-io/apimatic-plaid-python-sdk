
# Status Breakdown

A detailed breakdown of the institution's performance for a request type. The values for `success`, `error_plaid`, and `error_institution` sum to 1.

*This model accepts additional fields of type Any.*

## Structure

`StatusBreakdown`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `success` | `float` | Required | The percentage of login attempts that are successful, expressed as a decimal. |
| `error_plaid` | `float` | Required | The percentage of logins that are failing due to an internal Plaid issue, expressed as a decimal. |
| `error_institution` | `float` | Required | The percentage of logins that are failing due to an issue in the institution's system, expressed as a decimal. |
| `refresh_interval` | [`RefreshInterval`](../../doc/models/refresh-interval.md) | Optional | The `refresh_interval` may be `DELAYED` or `STOPPED` even when the success rate is high. This value is only returned for Transactions status breakdowns. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "success": 66.52,
  "error_plaid": 103.46,
  "error_institution": 133.82,
  "refresh_interval": "STOPPED",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

