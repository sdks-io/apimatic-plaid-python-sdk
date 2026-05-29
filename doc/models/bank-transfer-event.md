
# Bank Transfer Event

Represents an event in the Bank Transfers API.

*This model accepts additional fields of type Any.*

## Structure

`BankTransferEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_id` | `int` | Required | Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers.<br><br>**Constraints**: `>= 0` |
| `timestamp` | `datetime` | Required | The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`. |
| `event_type` | [`BankTransferEventType`](../../doc/models/bank-transfer-event-type.md) | Required | The type of event that this bank transfer represents.<br><br>`pending`: A new transfer was created; it is in the pending state.<br><br>`cancelled`: The transfer was cancelled by the client.<br><br>`failed`: The transfer failed, no funds were moved.<br><br>`posted`: The transfer has been successfully submitted to the payment network.<br><br>`reversed`: A posted transfer was reversed.<br><br>`receiver_pending`: The matching transfer was found as a pending transaction in the receiver's account<br><br>`receiver_posted`: The matching transfer was found as a posted transaction in the receiver's account |
| `account_id` | `str` | Required | The account ID associated with the bank transfer. |
| `bank_transfer_id` | `str` | Required | Plaid’s unique identifier for a bank transfer. |
| `origination_account_id` | `str` | Required | The ID of the origination account that this balance belongs to. |
| `bank_transfer_type` | [`BankTransferType`](../../doc/models/bank-transfer-type.md) | Required | The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into the origination account; a `credit` indicates a transfer of money out of the origination account. |
| `bank_transfer_amount` | `str` | Required | The bank transfer amount. |
| `bank_transfer_iso_currency_code` | `str` | Required | The currency of the bank transfer amount. |
| `failure_reason` | [`BankTransferFailure`](../../doc/models/bank-transfer-failure.md) | Required | The failure reason if the type of this transfer is `"failed"` or `"reversed"`. Null value otherwise. |
| `direction` | [`BankTransferDirection`](../../doc/models/bank-transfer-direction.md) | Required | Indicates the direction of the transfer: `outbound` for API-initiated transfers, or `inbound` for payments received by the FBO account. |
| `receiver_details` | [`BankTransferReceiverDetails`](../../doc/models/bank-transfer-receiver-details.md) | Required | The receiver details if the type of this event is `reciever_pending` or `reciever_posted`. Null value otherwise. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "event_id": 112,
  "timestamp": "2016-03-13T12:52:32.123Z",
  "event_type": "failed",
  "account_id": "account_id0",
  "bank_transfer_id": "bank_transfer_id4",
  "origination_account_id": "origination_account_id8",
  "bank_transfer_type": "debit",
  "bank_transfer_amount": "bank_transfer_amount8",
  "bank_transfer_iso_currency_code": "bank_transfer_iso_currency_code6",
  "failure_reason": {
    "ach_return_code": "ach_return_code6",
    "description": "description0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "direction": "outbound",
  "receiver_details": {
    "available_balance": "positive",
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

