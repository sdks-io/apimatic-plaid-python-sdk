
# Asset Report Create Request

AssetReportCreateRequest defines the request schema for `/asset_report/create`

*This model accepts additional fields of type Any.*

## Structure

`AssetReportCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `access_tokens` | `List[str]` | Required | An array of access tokens corresponding to the Items that will be included in the report. The `assets` product must have been initialized for the Items during link; the Assets product cannot be added after initialization.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `99` |
| `days_requested` | `int` | Required | The maximum integer number of days of history to include in the Asset Report. If using Fannie Mae Day 1 Certainty, `days_requested` must be at least 61 for new originations or at least 31 for refinancings.<br><br>**Constraints**: `>= 0`, `<= 730` |
| `options` | [`AssetReportCreateRequestOptions`](../../doc/models/asset-report-create-request-options.md) | Optional | An optional object to filter `/asset_report/create` results. If provided, must be non-`null`. The optional `user` object is required for the report to be eligible for Fannie Mae's Day 1 Certainty program. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "access_tokens": [
    "access_tokens6",
    "access_tokens7",
    "access_tokens8"
  ],
  "days_requested": 234,
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

