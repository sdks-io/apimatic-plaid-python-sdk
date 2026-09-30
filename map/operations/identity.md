<!-- Generated file — do not edit; regenerated with the SDK. -->

# Identity — operations

Accessor: `client.identity` · Source: `the_plaid_api/apis/identity.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.identity.identity_get

- **Route**: `POST /identity/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def identity_get(body: IdentityGetRequest | IdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IdentityGetResponse`
- **Returns (raw)**: `ApiResult[IdentityGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IdentityGetRequest` | `the_plaid_api/models/identity_get_request.py` |
| `IdentityGetRequestDict` | `the_plaid_api/models/identity_get_request.py` |
| `IdentityGetResponse` | `the_plaid_api/models/identity_get_response.py` |

