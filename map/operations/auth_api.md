<!-- Generated file — do not edit; regenerated with the SDK. -->

# AuthApi — operations

Accessor: `client.auth_api` · Source: `the_plaid_api/apis/auth_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.auth_api.auth_get

- **Route**: `POST /auth/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def auth_get(body: AuthGetRequest | AuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AuthGetResponse`
- **Returns (raw)**: `ApiResult[AuthGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AuthGetRequest` | `the_plaid_api/models/auth_get_request.py` |
| `AuthGetRequestDict` | `the_plaid_api/models/auth_get_request.py` |
| `AuthGetResponse` | `the_plaid_api/models/auth_get_response.py` |

