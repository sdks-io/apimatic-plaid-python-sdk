<!-- Generated file — do not edit; regenerated with the SDK. -->

# Accounts — operations

Accessor: `client.accounts` · Source: `the_plaid_api/apis/accounts.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.accounts.accounts_balance_get

- **Route**: `POST /accounts/balance/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def accounts_balance_get(body: AccountsBalanceGetRequest | AccountsBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountsGetResponse`
- **Returns (raw)**: `ApiResult[AccountsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountsBalanceGetRequest` | `the_plaid_api/models/accounts_balance_get_request.py` |
| `AccountsBalanceGetRequestDict` | `the_plaid_api/models/accounts_balance_get_request.py` |
| `AccountsGetResponse` | `the_plaid_api/models/accounts_get_response.py` |

### client.accounts.accounts_get

- **Route**: `POST /accounts/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def accounts_get(body: AccountsGetRequest | AccountsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountsGetResponse`
- **Returns (raw)**: `ApiResult[AccountsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccountsGetRequest` | `the_plaid_api/models/accounts_get_request.py` |
| `AccountsGetRequestDict` | `the_plaid_api/models/accounts_get_request.py` |
| `AccountsGetResponse` | `the_plaid_api/models/accounts_get_response.py` |

