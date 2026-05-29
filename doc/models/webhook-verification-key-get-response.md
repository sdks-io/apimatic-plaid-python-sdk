
# Webhook Verification Key Get Response

WebhookVerificationKeyGetResponse defines the response schema for `/webhook_verification_key/get`

*This model accepts additional fields of type Any.*

## Structure

`WebhookVerificationKeyGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | [`JwkPublicKey`](../../doc/models/jwk-public-key.md) | Required | A JSON Web Key (JWK) that can be used in conjunction with [JWT libraries](https://jwt.io/#libraries-io) to verify Plaid webhooks |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "key": {
    "alg": "alg6",
    "crv": "crv8",
    "kid": "kid6",
    "kty": "kty8",
    "use": "use0",
    "x": "x6",
    "y": "y4",
    "created_at": 114,
    "expired_at": 68,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "request_id": "request_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

