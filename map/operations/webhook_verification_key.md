<!-- Generated file — do not edit; regenerated with the SDK. -->

# WebhookVerificationKey — operations

Accessor: `client.webhook_verification_key` · Source: `the_plaid_api/apis/webhook_verification_key.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.webhook_verification_key.webhook_verification_key_get

- **Route**: `POST /webhook_verification_key/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def webhook_verification_key_get(body: WebhookVerificationKeyGetRequest | WebhookVerificationKeyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WebhookVerificationKeyGetResponse`
- **Returns (raw)**: `ApiResult[WebhookVerificationKeyGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WebhookVerificationKeyGetRequest` | `the_plaid_api/models/webhook_verification_key_get_request.py` |
| `WebhookVerificationKeyGetRequestDict` | `the_plaid_api/models/webhook_verification_key_get_request.py` |
| `WebhookVerificationKeyGetResponse` | `the_plaid_api/models/webhook_verification_key_get_response.py` |

