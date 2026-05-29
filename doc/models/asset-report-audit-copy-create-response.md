
# Asset Report Audit Copy Create Response

AssetReportAuditCopyCreateResponse defines the response schema for `/asset_report/audit_copy/get`

*This model accepts additional fields of type Any.*

## Structure

`AssetReportAuditCopyCreateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `audit_copy_token` | `str` | Required | A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "audit_copy_token": "audit_copy_token8",
  "request_id": "request_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

