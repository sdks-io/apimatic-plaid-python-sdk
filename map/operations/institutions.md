<!-- Generated file — do not edit; regenerated with the SDK. -->

# Institutions — operations

Accessor: `client.institutions` · Source: `the_plaid_api/apis/institutions.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.institutions.institutions_get

- **Route**: `POST /institutions/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def institutions_get(body: InstitutionsGetRequest | InstitutionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InstitutionsGetResponse`
- **Returns (raw)**: `ApiResult[InstitutionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionsGetRequest` | `the_plaid_api/models/institutions_get_request.py` |
| `InstitutionsGetRequestDict` | `the_plaid_api/models/institutions_get_request.py` |
| `InstitutionsGetResponse` | `the_plaid_api/models/institutions_get_response.py` |

### client.institutions.institutions_get_by_id

- **Route**: `POST /institutions/get_by_id`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def institutions_get_by_id(body: InstitutionsGetByIdRequest | InstitutionsGetByIdRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InstitutionsGetByIdResponse`
- **Returns (raw)**: `ApiResult[InstitutionsGetByIdResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionsGetByIdRequest` | `the_plaid_api/models/institutions_get_by_id_request.py` |
| `InstitutionsGetByIdRequestDict` | `the_plaid_api/models/institutions_get_by_id_request.py` |
| `InstitutionsGetByIdResponse` | `the_plaid_api/models/institutions_get_by_id_response.py` |

### client.institutions.institutions_search

- **Route**: `POST /institutions/search`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def institutions_search(body: InstitutionsSearchRequest | InstitutionsSearchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InstitutionsSearchResponse`
- **Returns (raw)**: `ApiResult[InstitutionsSearchResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InstitutionsSearchRequest` | `the_plaid_api/models/institutions_search_request.py` |
| `InstitutionsSearchRequestDict` | `the_plaid_api/models/institutions_search_request.py` |
| `InstitutionsSearchResponse` | `the_plaid_api/models/institutions_search_response.py` |

