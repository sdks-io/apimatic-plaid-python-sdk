
# Transaction Data

Information about the matched direct deposit transaction used to verify a user's payroll information.

*This model accepts additional fields of type Any.*

## Structure

`TransactionData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | The description of the transaction. |
| `amount` | `float` | Required | The amount of the transaction. |
| `date` | `date` | Required | The date of the transaction, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd"). |
| `account_id` | `str` | Required | A unique identifier for the end user's account. |
| `transaction_id` | `str` | Required | A unique identifier for the transaction. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "description": "description2",
  "amount": 102.84,
  "date": "2016-03-13",
  "account_id": "account_id4",
  "transaction_id": "transaction_id0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

