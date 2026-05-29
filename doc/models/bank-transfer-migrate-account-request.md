
# Bank Transfer Migrate Account Request

Defines the request schema for `/bank_transfer/migrate_account`

*This model accepts additional fields of type Any.*

## Structure

`BankTransferMigrateAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `account_number` | `str` | Required | The user's account number. |
| `routing_number` | `str` | Required | The user's routing number. |
| `account_type` | `str` | Required | The type of the bank account (`checking` or `savings`). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id6",
  "secret": "secret0",
  "account_number": "account_number4",
  "routing_number": "routing_number8",
  "account_type": "account_type0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

