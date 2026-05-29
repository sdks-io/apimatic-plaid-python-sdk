
# Item Access Token Invalidate Response

ItemAccessTokenInvalidateResponse defines the response schema for `/item/access_token/invalidate`

*This model accepts additional fields of type Any.*

## Structure

`ItemAccessTokenInvalidateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "new_access_token": "new_access_token4",
  "request_id": "request_id0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

