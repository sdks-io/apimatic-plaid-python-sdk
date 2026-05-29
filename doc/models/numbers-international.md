
# Numbers International

Identifying information for transferring money to or from an international bank account via wire transfer.

*This model accepts additional fields of type Any.*

## Structure

`NumbersInternational`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | The Plaid account ID associated with the account numbers |
| `iban` | `str` | Required | The International Bank Account Number (IBAN) for the account |
| `bic` | `str` | Required | The Bank Identifier Code (BIC) for the account |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_id": "account_id2",
  "iban": "iban4",
  "bic": "bic2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

