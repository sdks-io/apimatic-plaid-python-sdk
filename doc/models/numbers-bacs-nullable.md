
# Numbers Bacs Nullable

*This model accepts additional fields of type Any.*

## Structure

`NumbersBacsNullable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | The Plaid account ID associated with the account numbers |
| `account` | `str` | Required | The BACS account number for the account |
| `sort_code` | `str` | Required | The BACS sort code for the account |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_id": "account_id8",
  "account": "account6",
  "sort_code": "sort_code6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

