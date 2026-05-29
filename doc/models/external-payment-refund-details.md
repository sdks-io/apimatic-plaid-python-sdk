
# External Payment Refund Details

*This model accepts additional fields of type Any.*

## Structure

`ExternalPaymentRefundDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The name of the account holder. |
| `iban` | `str` | Required | The International Bank Account Number (IBAN) for the account. |
| `bacs` | [`RecipientBacsNullable`](../../doc/models/recipient-bacs-nullable.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name0",
  "iban": "iban4",
  "bacs": {
    "account": "account4",
    "sort_code": "sort_code4",
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

