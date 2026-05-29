
# Asset Report Refresh Request

AssetReportRefreshRequest defines the request schema for `/asset_report/refresh`

*This model accepts additional fields of type Any.*

## Structure

`AssetReportRefreshRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `asset_report_token` | `str` | Required | The `asset_report_token` returned by the original call to `/asset_report/create` |
| `days_requested` | `int` | Optional | The maximum number of days of history to include in the Asset Report. Must be an integer. If not specified, the value from the original call to `/asset_report/create` will be used.<br><br>**Constraints**: `>= 0`, `<= 730` |
| `options` | [`AssetReportRefreshRequestOptions`](../../doc/models/asset-report-refresh-request-options.md) | Optional | An optional object to filter `/asset_report/refresh` results. If provided, cannot be `null`. If not specified, the `options` from the original call to `/asset_report/create` will be used. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "asset_report_token": "asset_report_token2",
  "days_requested": 246,
  "options": {
    "client_report_id": "client_report_id8",
    "webhook": "webhook0",
    "user": {
      "client_user_id": "client_user_id4",
      "first_name": "first_name0",
      "middle_name": "middle_name0",
      "last_name": "last_name8",
      "ssn": "ssn6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
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

