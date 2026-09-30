<!-- Generated file — do not edit; regenerated with the SDK. -->

# Transactions — operations

Accessor: `client.transactions` · Source: `the_plaid_api/apis/transactions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transactions.transactions_get

- **Route**: `POST /transactions/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transactions_get(body: TransactionsGetRequest | TransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsGetResponse`
- **Returns (raw)**: `ApiResult[TransactionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsGetRequest` | `the_plaid_api/models/transactions_get_request.py` |
| `TransactionsGetRequestDict` | `the_plaid_api/models/transactions_get_request.py` |
| `TransactionsGetResponse` | `the_plaid_api/models/transactions_get_response.py` |

### client.transactions.transactions_refresh

- **Route**: `POST /transactions/refresh`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def transactions_refresh(body: TransactionsRefreshRequest | TransactionsRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `TransactionsRefreshResponse`
- **Returns (raw)**: `ApiResult[TransactionsRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionsRefreshRequest` | `the_plaid_api/models/transactions_refresh_request.py` |
| `TransactionsRefreshRequestDict` | `the_plaid_api/models/transactions_refresh_request.py` |
| `TransactionsRefreshResponse` | `the_plaid_api/models/transactions_refresh_response.py` |

