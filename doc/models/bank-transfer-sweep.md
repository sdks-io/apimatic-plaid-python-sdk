
# Bank Transfer Sweep

BankTransferSweep describes a sweep transfer.

*This model accepts additional fields of type Any.*

## Structure

`BankTransferSweep`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | Identifier of the sweep.<br><br>**Constraints**: `>= 0` |
| `transfer_id` | `str` | Required | Identifier of the sweep transfer. |
| `created_at` | `datetime` | Required | The datetime when the sweep occurred, in RFC 3339 format. |
| `amount` | `str` | Required | The amount of the sweep. |
| `iso_currency_code` | `str` | Required | The currency of the sweep, e.g. "USD". |
| `sweep_account` | [`BankTransferSweepAccount`](../../doc/models/bank-transfer-sweep-account.md) | Required | The account where the funds are swept to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "id": 146,
  "transfer_id": "transfer_id4",
  "created_at": "2016-03-13T12:52:32.123Z",
  "amount": "amount0",
  "iso_currency_code": "iso_currency_code8",
  "sweep_account": {
    "account_number": "account_number2",
    "routing_number": "routing_number2",
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

