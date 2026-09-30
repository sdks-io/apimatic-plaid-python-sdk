<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApplicationApi — operations

Accessor: `client.application_api` · Source: `the_plaid_api/apis/application_api.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.application_api.application_get

- **Route**: `POST /application/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def application_get(body: ApplicationGetRequest | ApplicationGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ApplicationGetResponse`
- **Returns (raw)**: `ApiResult[ApplicationGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ApplicationGetRequest` | `the_plaid_api/models/application_get_request.py` |
| `ApplicationGetRequestDict` | `the_plaid_api/models/application_get_request.py` |
| `ApplicationGetResponse` | `the_plaid_api/models/application_get_response.py` |

