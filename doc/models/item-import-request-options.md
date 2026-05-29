
# Item Import Request Options

An optional object to configure `/item/import` request.

*This model accepts additional fields of type Any.*

## Structure

`ItemImportRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook` | `str` | Optional | Specifies a webhook URL to associate with an Item. Plaid fires a webhook if credentials fail. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook": "webhook4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

