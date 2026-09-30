<!-- Generated file — do not edit; regenerated with the SDK. -->

# BankTransferApi — operations

Accessor: `client.bank_transfer_api` · Source: `the_plaid_api/apis/bank_transfer_api.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.bank_transfer_api.bank_transfer_balance_get

- **Route**: `POST /bank_transfer/balance/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_balance_get(body: BankTransferBalanceGetRequest | BankTransferBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferBalanceGetResponse`
- **Returns (raw)**: `ApiResult[BankTransferBalanceGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferBalanceGetRequest` | `the_plaid_api/models/bank_transfer_balance_get_request.py` |
| `BankTransferBalanceGetRequestDict` | `the_plaid_api/models/bank_transfer_balance_get_request.py` |
| `BankTransferBalanceGetResponse` | `the_plaid_api/models/bank_transfer_balance_get_response.py` |

### client.bank_transfer_api.bank_transfer_cancel

- **Route**: `POST /bank_transfer/cancel`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_cancel(body: BankTransferCancelRequest | BankTransferCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferCancelResponse`
- **Returns (raw)**: `ApiResult[BankTransferCancelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferCancelRequest` | `the_plaid_api/models/bank_transfer_cancel_request.py` |
| `BankTransferCancelRequestDict` | `the_plaid_api/models/bank_transfer_cancel_request.py` |
| `BankTransferCancelResponse` | `the_plaid_api/models/bank_transfer_cancel_response.py` |

### client.bank_transfer_api.bank_transfer_create

- **Route**: `POST /bank_transfer/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_create(body: BankTransferCreateRequest | BankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferCreateResponse`
- **Returns (raw)**: `ApiResult[BankTransferCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferCreateRequest` | `the_plaid_api/models/bank_transfer_create_request.py` |
| `BankTransferCreateRequestDict` | `the_plaid_api/models/bank_transfer_create_request.py` |
| `BankTransferCreateResponse` | `the_plaid_api/models/bank_transfer_create_response.py` |

### client.bank_transfer_api.bank_transfer_event_list

- **Route**: `POST /bank_transfer/event/list`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_event_list(body: BankTransferEventListRequest | BankTransferEventListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferEventListResponse`
- **Returns (raw)**: `ApiResult[BankTransferEventListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferEventListRequest` | `the_plaid_api/models/bank_transfer_event_list_request.py` |
| `BankTransferEventListRequestDict` | `the_plaid_api/models/bank_transfer_event_list_request.py` |
| `BankTransferEventListResponse` | `the_plaid_api/models/bank_transfer_event_list_response.py` |

### client.bank_transfer_api.bank_transfer_event_sync

- **Route**: `POST /bank_transfer/event/sync`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_event_sync(body: BankTransferEventSyncRequest | BankTransferEventSyncRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferEventSyncResponse`
- **Returns (raw)**: `ApiResult[BankTransferEventSyncResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferEventSyncRequest` | `the_plaid_api/models/bank_transfer_event_sync_request.py` |
| `BankTransferEventSyncRequestDict` | `the_plaid_api/models/bank_transfer_event_sync_request.py` |
| `BankTransferEventSyncResponse` | `the_plaid_api/models/bank_transfer_event_sync_response.py` |

### client.bank_transfer_api.bank_transfer_get

- **Route**: `POST /bank_transfer/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_get(body: BankTransferGetRequest | BankTransferGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferGetResponse`
- **Returns (raw)**: `ApiResult[BankTransferGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferGetRequest` | `the_plaid_api/models/bank_transfer_get_request.py` |
| `BankTransferGetRequestDict` | `the_plaid_api/models/bank_transfer_get_request.py` |
| `BankTransferGetResponse` | `the_plaid_api/models/bank_transfer_get_response.py` |

### client.bank_transfer_api.bank_transfer_list

- **Route**: `POST /bank_transfer/list`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_list(body: BankTransferListRequest | BankTransferListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferListResponse`
- **Returns (raw)**: `ApiResult[BankTransferListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferListRequest` | `the_plaid_api/models/bank_transfer_list_request.py` |
| `BankTransferListRequestDict` | `the_plaid_api/models/bank_transfer_list_request.py` |
| `BankTransferListResponse` | `the_plaid_api/models/bank_transfer_list_response.py` |

### client.bank_transfer_api.bank_transfer_migrate_account

- **Route**: `POST /bank_transfer/migrate_account`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_migrate_account(body: BankTransferMigrateAccountRequest | BankTransferMigrateAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferMigrateAccountResponse`
- **Returns (raw)**: `ApiResult[BankTransferMigrateAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferMigrateAccountRequest` | `the_plaid_api/models/bank_transfer_migrate_account_request.py` |
| `BankTransferMigrateAccountRequestDict` | `the_plaid_api/models/bank_transfer_migrate_account_request.py` |
| `BankTransferMigrateAccountResponse` | `the_plaid_api/models/bank_transfer_migrate_account_response.py` |

### client.bank_transfer_api.bank_transfer_sweep_get

- **Route**: `POST /bank_transfer/sweep/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_sweep_get(body: BankTransferSweepGetRequest | BankTransferSweepGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferSweepGetResponse`
- **Returns (raw)**: `ApiResult[BankTransferSweepGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferSweepGetRequest` | `the_plaid_api/models/bank_transfer_sweep_get_request.py` |
| `BankTransferSweepGetRequestDict` | `the_plaid_api/models/bank_transfer_sweep_get_request.py` |
| `BankTransferSweepGetResponse` | `the_plaid_api/models/bank_transfer_sweep_get_response.py` |

### client.bank_transfer_api.bank_transfer_sweep_list

- **Route**: `POST /bank_transfer/sweep/list`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def bank_transfer_sweep_list(body: BankTransferSweepListRequest | BankTransferSweepListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BankTransferSweepListResponse`
- **Returns (raw)**: `ApiResult[BankTransferSweepListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BankTransferSweepListRequest` | `the_plaid_api/models/bank_transfer_sweep_list_request.py` |
| `BankTransferSweepListRequestDict` | `the_plaid_api/models/bank_transfer_sweep_list_request.py` |
| `BankTransferSweepListResponse` | `the_plaid_api/models/bank_transfer_sweep_list_response.py` |

