<!-- Generated file — do not edit; regenerated with the SDK. -->

# ItemApi — operations

Accessor: `client.item_api` · Source: `the_plaid_api/apis/item_api.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.item_api.item_access_token_invalidate

- **Route**: `POST /item/access_token/invalidate`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_access_token_invalidate(body: ItemAccessTokenInvalidateRequest | ItemAccessTokenInvalidateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemAccessTokenInvalidateResponse`
- **Returns (raw)**: `ApiResult[ItemAccessTokenInvalidateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemAccessTokenInvalidateRequest` | `the_plaid_api/models/item_access_token_invalidate_request.py` |
| `ItemAccessTokenInvalidateRequestDict` | `the_plaid_api/models/item_access_token_invalidate_request.py` |
| `ItemAccessTokenInvalidateResponse` | `the_plaid_api/models/item_access_token_invalidate_response.py` |

### client.item_api.item_application_list

- **Route**: `POST /item/application/list`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_application_list(body: ItemApplicationListRequest | ItemApplicationListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemApplicationListResponse`
- **Returns (raw)**: `ApiResult[ItemApplicationListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemApplicationListRequest` | `the_plaid_api/models/item_application_list_request.py` |
| `ItemApplicationListRequestDict` | `the_plaid_api/models/item_application_list_request.py` |
| `ItemApplicationListResponse` | `the_plaid_api/models/item_application_list_response.py` |

### client.item_api.item_application_scopes_update

- **Route**: `POST /item/application/scopes/update`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_application_scopes_update(body: ItemApplicationScopesUpdateRequest | ItemApplicationScopesUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemApplicationScopesUpdateResponse`
- **Returns (raw)**: `ApiResult[ItemApplicationScopesUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemApplicationScopesUpdateRequest` | `the_plaid_api/models/item_application_scopes_update_request.py` |
| `ItemApplicationScopesUpdateRequestDict` | `the_plaid_api/models/item_application_scopes_update_request.py` |
| `ItemApplicationScopesUpdateResponse` | `the_plaid_api/models/item_application_scopes_update_response.py` |

### client.item_api.item_create_public_token

- **Route**: `POST /item/public_token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_create_public_token(body: ItemPublicTokenCreateRequest | ItemPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemPublicTokenCreateResponse`
- **Returns (raw)**: `ApiResult[ItemPublicTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemPublicTokenCreateRequest` | `the_plaid_api/models/item_public_token_create_request.py` |
| `ItemPublicTokenCreateRequestDict` | `the_plaid_api/models/item_public_token_create_request.py` |
| `ItemPublicTokenCreateResponse` | `the_plaid_api/models/item_public_token_create_response.py` |

### client.item_api.item_get

- **Route**: `POST /item/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_get(body: ItemGetRequest | ItemGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemGetResponse`
- **Returns (raw)**: `ApiResult[ItemGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemGetRequest` | `the_plaid_api/models/item_get_request.py` |
| `ItemGetRequestDict` | `the_plaid_api/models/item_get_request.py` |
| `ItemGetResponse` | `the_plaid_api/models/item_get_response.py` |

### client.item_api.item_import

- **Route**: `POST /item/import`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_import(body: ItemImportRequest | ItemImportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemImportResponse`
- **Returns (raw)**: `ApiResult[ItemImportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemImportRequest` | `the_plaid_api/models/item_import_request.py` |
| `ItemImportRequestDict` | `the_plaid_api/models/item_import_request.py` |
| `ItemImportResponse` | `the_plaid_api/models/item_import_response.py` |

### client.item_api.item_public_token_exchange

- **Route**: `POST /item/public_token/exchange`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_public_token_exchange(body: ItemPublicTokenExchangeRequest | ItemPublicTokenExchangeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemPublicTokenExchangeResponse`
- **Returns (raw)**: `ApiResult[ItemPublicTokenExchangeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemPublicTokenExchangeRequest` | `the_plaid_api/models/item_public_token_exchange_request.py` |
| `ItemPublicTokenExchangeRequestDict` | `the_plaid_api/models/item_public_token_exchange_request.py` |
| `ItemPublicTokenExchangeResponse` | `the_plaid_api/models/item_public_token_exchange_response.py` |

### client.item_api.item_remove

- **Route**: `POST /item/remove`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_remove(body: ItemRemoveRequest | ItemRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemRemoveResponse`
- **Returns (raw)**: `ApiResult[ItemRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemRemoveRequest` | `the_plaid_api/models/item_remove_request.py` |
| `ItemRemoveRequestDict` | `the_plaid_api/models/item_remove_request.py` |
| `ItemRemoveResponse` | `the_plaid_api/models/item_remove_response.py` |

### client.item_api.item_webhook_update

- **Route**: `POST /item/webhook/update`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def item_webhook_update(body: ItemWebhookUpdateRequest | ItemWebhookUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ItemWebhookUpdateResponse`
- **Returns (raw)**: `ApiResult[ItemWebhookUpdateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ItemWebhookUpdateRequest` | `the_plaid_api/models/item_webhook_update_request.py` |
| `ItemWebhookUpdateRequestDict` | `the_plaid_api/models/item_webhook_update_request.py` |
| `ItemWebhookUpdateResponse` | `the_plaid_api/models/item_webhook_update_response.py` |

