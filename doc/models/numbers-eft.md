
# Numbers Eft

Identifying information for transferring money to or from a Canadian bank account via EFT.

*This model accepts additional fields of type Any.*

## Structure

`NumbersEft`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | The Plaid account ID associated with the account numbers |
| `account` | `str` | Required | The EFT account number for the account |
| `institution` | `str` | Required | The EFT institution number for the account |
| `branch` | `str` | Required | The EFT branch number for the account |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_id": "account_id8",
  "account": "account6",
  "institution": "institution6",
  "branch": "branch2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

