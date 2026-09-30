<!-- Generated file — do not edit; regenerated with the SDK. -->

# Link — operations

Accessor: `client.link` · Source: `the_plaid_api/apis/link.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.link.link_token_create

- **Route**: `POST /link/token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def link_token_create(body: LinkTokenCreateRequest | LinkTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LinkTokenCreateResponse`
- **Returns (raw)**: `ApiResult[LinkTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LinkTokenCreateRequest` | `the_plaid_api/models/link_token_create_request.py` |
| `LinkTokenCreateRequestDict` | `the_plaid_api/models/link_token_create_request.py` |
| `LinkTokenCreateResponse` | `the_plaid_api/models/link_token_create_response.py` |

### client.link.link_token_get

- **Route**: `POST /link/token/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def link_token_get(body: LinkTokenGetRequest | LinkTokenGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LinkTokenGetResponse`
- **Returns (raw)**: `ApiResult[LinkTokenGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LinkTokenGetRequest` | `the_plaid_api/models/link_token_get_request.py` |
| `LinkTokenGetRequestDict` | `the_plaid_api/models/link_token_get_request.py` |
| `LinkTokenGetResponse` | `the_plaid_api/models/link_token_get_response.py` |

