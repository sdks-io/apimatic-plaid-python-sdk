
# Item Public Token Exchange Response

ItemPublicTokenExchangeResponse defines the response schema for `/item/public_token/exchange`

*This model accepts additional fields of type Any.*

## Structure

`ItemPublicTokenExchangeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `item_id` | `str` | Required | The `item_id` value of the Item associated with the returned `access_token` |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "access_token": "access_token4",
  "item_id": "item_id6",
  "request_id": "request_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

