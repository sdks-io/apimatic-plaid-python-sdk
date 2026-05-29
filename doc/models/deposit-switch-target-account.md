
# Deposit Switch Target Account

*This model accepts additional fields of type Any.*

## Structure

`DepositSwitchTargetAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | Account number for deposit switch destination |
| `routing_number` | `str` | Required | Routing number for deposit switch destination |
| `account_name` | `str` | Required | The name of the deposit switch destination account, as it will be displayed to the end user in the Deposit Switch interface. It is not required to match the name used in online banking. |
| `account_subtype` | [`AccountSubtype1`](../../doc/models/account-subtype-1.md) | Required | The account subtype of the account, either `checking` or `savings`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_number": "account_number6",
  "routing_number": "routing_number0",
  "account_name": "account_name4",
  "account_subtype": "checking",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

