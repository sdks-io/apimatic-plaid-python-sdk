
# Asset Report Audit Copy Get Request

AssetReportAuditCopyGetRequest defines the request schema for `/asset_report/audit_copy/get`

*This model accepts additional fields of type Any.*

## Structure

`AssetReportAuditCopyGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `audit_copy_token` | `str` | Required | The `audit_copy_token` granting access to the Audit Copy you would like to get. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id8",
  "secret": "secret2",
  "audit_copy_token": "audit_copy_token4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

