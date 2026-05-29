
# Asset Report Create Request Options

An optional object to filter `/asset_report/create` results. If provided, must be non-`null`. The optional `user` object is required for the report to be eligible for Fannie Mae's Day 1 Certainty program.

*This model accepts additional fields of type Any.*

## Structure

`AssetReportCreateRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_report_id` | `str` | Optional | Client-generated identifier, which can be used by lenders to track loan applications. |
| `webhook` | `str` | Optional | URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready. |
| `user` | [`AssetReportUser`](../../doc/models/asset-report-user.md) | Optional | The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The `first_name`, `last_name`, and `ssn` fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_report_id": "client_report_id4",
  "webhook": "webhook6",
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
}
```

