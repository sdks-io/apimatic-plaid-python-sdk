
# Liabilities Get Request Options

An optional object to filter `/liabilities/get` results. If provided, `options` cannot be null.

*This model accepts additional fields of type Any.*

## Structure

`LiabilitiesGetRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_ids` | `List[str]` | Optional | A list of accounts to retrieve for the Item.<br><br>An error will be returned if a provided `account_id` is not associated with the Item |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_ids": [
    "account_ids9",
    "account_ids0"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

