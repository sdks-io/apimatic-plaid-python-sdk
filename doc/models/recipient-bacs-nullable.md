
# Recipient Bacs Nullable

*This model accepts additional fields of type Any.*

## Structure

`RecipientBacsNullable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Optional | The account number of the account. Maximum of 10 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `10` |
| `sort_code` | `str` | Optional | The 6-character sort code of the account.<br><br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account": "account4",
  "sort_code": "sort_code4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

