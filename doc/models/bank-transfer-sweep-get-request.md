
# Bank Transfer Sweep Get Request

BankTransferSweepGetRequest defines the request schema for `/bank_transfer/sweep/get`

*This model accepts additional fields of type Any.*

## Structure

`BankTransferSweepGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `sweep_id` | `int` | Required | Identifier of the sweep.<br><br>**Constraints**: `>= 0` |
| `origination_account_id` | `str` | Optional | If multiple origination accounts are available, `origination_account_id` must be used to specify the account that the sweep belongs to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id8",
  "secret": "secret2",
  "sweep_id": 40,
  "origination_account_id": "origination_account_id6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

