
# Bank Transfer Event List Response

Defines the response schema for `/bank_transfer/event/list`

*This model accepts additional fields of type Any.*

## Structure

`BankTransferEventListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_transfer_events` | [`List[BankTransferEvent]`](../../doc/models/bank-transfer-event.md) | Required | - |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "bank_transfer_events": [
    {
      "event_id": 98,
      "timestamp": "2016-03-13T12:52:32.123Z",
      "event_type": "pending",
      "account_id": "account_id8",
      "bank_transfer_id": "bank_transfer_id8",
      "origination_account_id": "origination_account_id6",
      "bank_transfer_type": "debit",
      "bank_transfer_amount": "bank_transfer_amount4",
      "bank_transfer_iso_currency_code": "bank_transfer_iso_currency_code4",
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
  ],
  "request_id": "request_id4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

