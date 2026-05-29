
# Bank Transfer Sweep Account

The account where the funds are swept to.

*This model accepts additional fields of type Any.*

## Structure

`BankTransferSweepAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | - |
| `routing_number` | `str` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_number": "account_number6",
  "routing_number": "routing_number0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

