<!-- Generated file — do not edit; regenerated with the SDK. -->

# Liabilities — operations

Accessor: `client.liabilities` · Source: `the_plaid_api/apis/liabilities.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.liabilities.liabilities_get

- **Route**: `POST /liabilities/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def liabilities_get(body: LiabilitiesGetRequest | LiabilitiesGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `LiabilitiesGetResponse`
- **Returns (raw)**: `ApiResult[LiabilitiesGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LiabilitiesGetRequest` | `the_plaid_api/models/liabilities_get_request.py` |
| `LiabilitiesGetRequestDict` | `the_plaid_api/models/liabilities_get_request.py` |
| `LiabilitiesGetResponse` | `the_plaid_api/models/liabilities_get_response.py` |

