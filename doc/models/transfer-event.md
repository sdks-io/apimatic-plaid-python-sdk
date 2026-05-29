
# Transfer Event

Represents an event in the Transfers API.

*This model accepts additional fields of type Any.*

## Structure

`TransferEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_id` | `int` | Required | Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers.<br><br>**Constraints**: `>= 0` |
| `timestamp` | `datetime` | Required | The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`. |
| `event_type` | [`TransferEventType`](../../doc/models/transfer-event-type.md) | Required | The type of event that this transfer represents.<br><br>`pending`: A new transfer was created; it is in the pending state.<br><br>`cancelled`: The transfer was cancelled by the client.<br><br>`failed`: The transfer failed, no funds were moved.<br><br>`posted`: The transfer has been successfully submitted to the payment network.<br><br>`reversed`: A posted transfer was reversed. |
| `account_id` | `str` | Required | The account ID associated with the transfer. |
| `transfer_id` | `str` | Required | Plaid’s unique identifier for a transfer. |
| `origination_account_id` | `str` | Required | The ID of the origination account that this balance belongs to. |
| `transfer_type` | [`TransferType1`](../../doc/models/transfer-type-1.md) | Required | The type of transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account. |
| `transfer_amount` | `str` | Required | The amount of the transfer (decimal string with two digits of precision e.g. “10.00”). |
| `failure_reason` | [`TransferFailure`](../../doc/models/transfer-failure.md) | Required | The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "event_id": 82,
  "timestamp": "2016-03-13T12:52:32.123Z",
  "event_type": "pending",
  "account_id": "account_id2",
  "transfer_id": "transfer_id6",
  "origination_account_id": "origination_account_id0",
  "transfer_type": "debit",
  "transfer_amount": "transfer_amount4",
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

