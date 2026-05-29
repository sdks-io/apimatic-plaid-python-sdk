
# Bank Transfer Balance Get Response

Defines the response schema for `/bank_transfer/balance/get`

*This model accepts additional fields of type Any.*

## Structure

`BankTransferBalanceGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance` | [`BankTransferBalance`](../../doc/models/bank-transfer-balance.md) | Required | - |
| `origination_account_id` | `str` | Required | The ID of the origination account that this balance belongs to. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "balance": {
    "available": "available8",
    "transactable": "transactable6",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "origination_account_id": "origination_account_id6",
  "request_id": "request_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

