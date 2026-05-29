
# Distribution Details

An object representing information about a distribution from the paycheck (for example, the amount distributed to a specific checking account, or to a retirement plan).

*This model accepts additional fields of type Any.*

## Structure

`DistributionDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | The account number of the account being deposited to. |
| `bank_account_type` | `str` | Optional | The type of bank account (e.g. Checking or Savings) |
| `bank_name` | `str` | Optional | The name of the bank that the payment is being deposited to. |
| `current_pay` | [`Pay`](../../doc/models/pay.md) | Optional | An object representing a monetary amount. |
| `description` | `str` | Optional | A description of the distribution type. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_number": "account_number8",
  "bank_account_type": "bank_account_type0",
  "bank_name": "bank_name2",
  "current_pay": {
    "amount": 45.16,
    "currency": "currency4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "description": "description2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

