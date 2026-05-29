
# Signal Return Report Request

SignalReturnReportRequest defines the request schema for `/signal/return/report`

*This model accepts additional fields of type Any.*

## Structure

`SignalReturnReportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `client_transaction_id` | `str` | Required | Must be the same as the `client_transaction_id` supplied when calling `/signal/evaluate` |
| `return_code` | `str` | Required | Must be a valid ACH return code (e.g. "R01") |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id8",
  "secret": "secret8",
  "client_transaction_id": "client_transaction_id6",
  "return_code": "return_code6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

