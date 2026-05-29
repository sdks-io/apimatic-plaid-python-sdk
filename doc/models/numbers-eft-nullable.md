
# Numbers Eft Nullable

*This model accepts additional fields of type Any.*

## Structure

`NumbersEftNullable`

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
  "account_id": "account_id0",
  "account": "account8",
  "institution": "institution8",
  "branch": "branch4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

