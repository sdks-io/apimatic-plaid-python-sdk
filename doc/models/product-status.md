
# Product Status

A representation of the status health of a request type. Auth requests, Balance requests, Identity requests, Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item logins each have their own status object.

*This model accepts additional fields of type Any.*

## Structure

`ProductStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status`](../../doc/models/status.md) | Required | `HEALTHY`: the majority of requests are successful<br>`DEGRADED`: only some requests are successful<br>`DOWN`: all requests are failing |
| `last_status_change` | `datetime` | Required | [ISO 8601](https://wikipedia.org/wiki/ISO_8601) formatted timestamp of the last status change for the institution. |
| `breakdown` | [`StatusBreakdown`](../../doc/models/status-breakdown.md) | Required | A detailed breakdown of the institution's performance for a request type. The values for `success`, `error_plaid`, and `error_institution` sum to 1. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "status": "DEGRADED",
  "last_status_change": "2016-03-13T12:52:32.123Z",
  "breakdown": {
    "success": 164.84,
    "error_plaid": 201.78,
    "error_institution": 35.5,
    "refresh_interval": "NORMAL",
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

