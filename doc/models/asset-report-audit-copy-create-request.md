
# Asset Report Audit Copy Create Request

AssetReportAuditCopyCreateRequest defines the request schema for `/asset_report/audit_copy/get`

*This model accepts additional fields of type Any.*

## Structure

`AssetReportAuditCopyCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `asset_report_token` | `str` | Required | A token that can be provided to endpoints such as `/asset_report/get` or `/asset_report/pdf/get` to fetch or update an Asset Report. |
| `auditor_id` | `str` | Required | The `auditor_id` of the third party with whom you would like to share the Asset Report. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id8",
  "secret": "secret2",
  "asset_report_token": "asset_report_token4",
  "auditor_id": "auditor_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

