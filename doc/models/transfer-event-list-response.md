
# Transfer Event List Response

Defines the response schema for `/transfer/event/list`

*This model accepts additional fields of type Any.*

## Structure

`TransferEventListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_events` | [`List[TransferEvent]`](../../doc/models/transfer-event.md) | Required | - |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "transfer_events": [
    {
      "event_id": 90,
      "timestamp": "2016-03-13T12:52:32.123Z",
      "event_type": "reversed",
      "account_id": "account_id8",
      "transfer_id": "transfer_id2",
      "origination_account_id": "origination_account_id6",
      "transfer_type": "debit",
      "transfer_amount": "transfer_amount8",
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
  ],
  "request_id": "request_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

