
# Item Webhook Update Request

ItemWebhookUpdateRequest defines the request schema for `/item/webhook/update`

*This model accepts additional fields of type Any.*

## Structure

`ItemWebhookUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `webhook` | `str` | Required | The new webhook URL to associate with the Item. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id2",
  "secret": "secret4",
  "access_token": "access_token8",
  "webhook": "webhook8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

