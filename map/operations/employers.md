<!-- Generated file — do not edit; regenerated with the SDK. -->

# Employers — operations

Accessor: `client.employers` · Source: `the_plaid_api/apis/employers.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.employers.employers_search

- **Route**: `POST /employers/search`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def employers_search(body: EmployersSearchRequest | EmployersSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `EmployersSearchResponse`
- **Returns (raw)**: `ApiResult[EmployersSearchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EmployersSearchRequest` | `the_plaid_api/models/employers_search_request.py` |
| `EmployersSearchRequestDict` | `the_plaid_api/models/employers_search_request.py` |
| `EmployersSearchResponse` | `the_plaid_api/models/employers_search_response.py` |

