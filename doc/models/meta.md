
# Meta

Allows specifying the metadata of the test account

*This model accepts additional fields of type Any.*

## Structure

`Meta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The account's name |
| `official_name` | `str` | Required | The account's official name |
| `limit` | `float` | Required | The account's limit |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name8",
  "official_name": "official_name0",
  "limit": 109.44,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

