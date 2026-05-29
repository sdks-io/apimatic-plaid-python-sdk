
# Bank Transfer Event List Request

Defines the request schema for `/bank_transfer/event/list`

*This model accepts additional fields of type Any.*

## Structure

`BankTransferEventListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `start_date` | `datetime` | Optional | The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`) |
| `end_date` | `datetime` | Optional | The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. `2019-12-06T22:35:49Z`) |
| `bank_transfer_id` | `str` | Optional | Plaid’s unique identifier for a bank transfer. |
| `account_id` | `str` | Optional | The account ID to get events for all transactions to/from an account. |
| `bank_transfer_type` | [`BankTransferType1`](../../doc/models/bank-transfer-type-1.md) | Optional | The type of bank transfer. This will be either `debit` or `credit`.  A `debit` indicates a transfer of money into your origination account; a `credit` indicates a transfer of money out of your origination account. |
| `event_types` | [`List[BankTransferEventType]`](../../doc/models/bank-transfer-event-type.md) | Optional | Filter events by event type. |
| `count` | `int` | Optional | The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.<br><br>**Default**: `25`<br><br>**Constraints**: `>= 1`, `<= 25` |
| `offset` | `int` | Optional | The offset into the list of bank transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |
| `origination_account_id` | `str` | Optional | The origination account ID to get events for transfers from a specific origination account. |
| `direction` | [`BankTransferDirection1`](../../doc/models/bank-transfer-direction-1.md) | Optional | Indicates the direction of the transfer: `outbound`: for API-initiated transfers<br>`inbound`: for payments received by the FBO account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "count": 25,
  "offset": 0,
  "client_id": "client_id8",
  "secret": "secret8",
  "start_date": "2016-03-13T12:52:32.123Z",
  "end_date": "2016-03-13T12:52:32.123Z",
  "bank_transfer_id": "bank_transfer_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

