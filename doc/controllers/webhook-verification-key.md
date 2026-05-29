# Webhook Verification Key

```python
webhook_verification_key_api = client.webhook_verification_key
```

## Class Name

`WebhookVerificationKeyApi`


# Webhook Verification Key Get

Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.

The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

Find out more here: [/api/webhooks/webhook-verification/#webhook_verification_keyget](/api/webhooks/webhook-verification/#webhook_verification_keyget)

```python
def webhook_verification_key_get(self,
                                body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookVerificationKeyGetRequest`](../../doc/models/webhook-verification-key-get-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WebhookVerificationKeyGetResponse`](../../doc/models/webhook-verification-key-get-response.md).

## Example Usage

```python
body = WebhookVerificationKeyGetRequest(
    key_id='key_id2'
)

result = webhook_verification_key_api.webhook_verification_key_get(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "key": {
    "alg": "ES256",
    "created_at": 1560466150,
    "crv": "P-256",
    "expired_at": null,
    "kid": "bfbd5111-8e33-4643-8ced-b2e642a72f3c",
    "kty": "EC",
    "use": "sig",
    "x": "hKXLGIjWvCBv-cP5euCTxl8g9GLG9zHo_3pO5NN1DwQ",
    "y": "shhexqPB7YffGn6fR6h2UhTSuCtPmfzQJ6ENVIoO4Ys"
  },
  "request_id": "RZ6Omi1bzzwDaLo"
}
```

