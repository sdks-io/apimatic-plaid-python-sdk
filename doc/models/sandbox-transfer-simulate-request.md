
# Sandbox Transfer Simulate Request

Defines the request schema for `/sandbox/transfer/simulate`

*This model accepts additional fields of type Any.*

## Structure

`SandboxTransferSimulateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `transfer_id` | `str` | Required | Plaid’s unique identifier for a transfer. |
| `event_type` | `str` | Required | The asynchronous event to be simulated. May be: `posted`, `failed`, or `reversed`.<br><br>An error will be returned if the event type is incompatible with the current transfer status. Compatible status --> event type transitions include:<br><br>`pending` --> `failed`<br><br>`pending` --> `posted`<br><br>`posted` --> `reversed` |
| `failure_reason` | [`TransferFailure`](../../doc/models/transfer-failure.md) | Optional | The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "transfer_id": "transfer_id0",
  "event_type": "event_type6",
  "failure_reason": {
    "ach_return_code": "ach_return_code6",
    "description": "description0",
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

