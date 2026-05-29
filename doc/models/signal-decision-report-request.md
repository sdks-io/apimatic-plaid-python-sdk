
# Signal Decision Report Request

SignalDecisionReportRequest defines the request schema for `/signal/decision/report`

*This model accepts additional fields of type Any.*

## Structure

`SignalDecisionReportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `client_transaction_id` | `str` | Required | Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate` |
| `initiated` | `bool` | Required | `true` if the ACH transaction was initiated, `false` otherwise. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "client_transaction_id": "client_transaction_id2",
  "initiated": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

