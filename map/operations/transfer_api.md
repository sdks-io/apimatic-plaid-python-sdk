<!-- Generated file — do not edit; regenerated with the SDK. -->

# TransferApi — operations

Accessor: `client.transfer_api` · Source: `the_plaid_api/apis/transfer_api.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transfer_api.transfer_authorization_create

- **Route**: `POST /transfer/authorization/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transfer_authorization_create(body: TransferAuthorizationCreateRequest | TransferAuthorizationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferAuthorizationCreateResponse`
- **Returns (raw)**: `ApiResult[TransferAuthorizationCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferAuthorizationCreateRequest` | `the_plaid_api/models/transfer_authorization_create_request.py` |
| `TransferAuthorizationCreateRequestDict` | `the_plaid_api/models/transfer_authorization_create_request.py` |
| `TransferAuthorizationCreateResponse` | `the_plaid_api/models/transfer_authorization_create_response.py` |

### client.transfer_api.transfer_cancel

- **Route**: `POST /transfer/cancel`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transfer_cancel(body: TransferCancelRequest | TransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferCancelResponse`
- **Returns (raw)**: `ApiResult[TransferCancelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferCancelRequest` | `the_plaid_api/models/transfer_cancel_request.py` |
| `TransferCancelRequestDict` | `the_plaid_api/models/transfer_cancel_request.py` |
| `TransferCancelResponse` | `the_plaid_api/models/transfer_cancel_response.py` |

### client.transfer_api.transfer_create

- **Route**: `POST /transfer/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transfer_create(body: TransferCreateRequest | TransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferCreateResponse`
- **Returns (raw)**: `ApiResult[TransferCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferCreateRequest` | `the_plaid_api/models/transfer_create_request.py` |
| `TransferCreateRequestDict` | `the_plaid_api/models/transfer_create_request.py` |
| `TransferCreateResponse` | `the_plaid_api/models/transfer_create_response.py` |

### client.transfer_api.transfer_event_list

- **Route**: `POST /transfer/event/list`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transfer_event_list(body: TransferEventListRequest | TransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferEventListResponse`
- **Returns (raw)**: `ApiResult[TransferEventListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferEventListRequest` | `the_plaid_api/models/transfer_event_list_request.py` |
| `TransferEventListRequestDict` | `the_plaid_api/models/transfer_event_list_request.py` |
| `TransferEventListResponse` | `the_plaid_api/models/transfer_event_list_response.py` |

### client.transfer_api.transfer_event_sync

- **Route**: `POST /transfer/event/sync`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transfer_event_sync(body: TransferEventSyncRequest | TransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferEventSyncResponse`
- **Returns (raw)**: `ApiResult[TransferEventSyncResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferEventSyncRequest` | `the_plaid_api/models/transfer_event_sync_request.py` |
| `TransferEventSyncRequestDict` | `the_plaid_api/models/transfer_event_sync_request.py` |
| `TransferEventSyncResponse` | `the_plaid_api/models/transfer_event_sync_response.py` |

### client.transfer_api.transfer_get

- **Route**: `POST /transfer/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transfer_get(body: TransferGetRequest | TransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferGetResponse`
- **Returns (raw)**: `ApiResult[TransferGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferGetRequest` | `the_plaid_api/models/transfer_get_request.py` |
| `TransferGetRequestDict` | `the_plaid_api/models/transfer_get_request.py` |
| `TransferGetResponse` | `the_plaid_api/models/transfer_get_response.py` |

### client.transfer_api.transfer_list

- **Route**: `POST /transfer/list`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transfer_list(body: TransferListRequest | TransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransferListResponse`
- **Returns (raw)**: `ApiResult[TransferListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransferListRequest` | `the_plaid_api/models/transfer_list_request.py` |
| `TransferListRequestDict` | `the_plaid_api/models/transfer_list_request.py` |
| `TransferListResponse` | `the_plaid_api/models/transfer_list_response.py` |

