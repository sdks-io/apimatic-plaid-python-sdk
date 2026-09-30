<!-- Generated file — do not edit; regenerated with the SDK. -->

# Investments — operations

Accessor: `client.investments` · Source: `the_plaid_api/apis/investments.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.investments.investments_holdings_get

- **Route**: `POST /investments/holdings/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def investments_holdings_get(body: InvestmentsHoldingsGetRequest | InvestmentsHoldingsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InvestmentsHoldingsGetResponse`
- **Returns (raw)**: `ApiResult[InvestmentsHoldingsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvestmentsHoldingsGetRequest` | `the_plaid_api/models/investments_holdings_get_request.py` |
| `InvestmentsHoldingsGetRequestDict` | `the_plaid_api/models/investments_holdings_get_request.py` |
| `InvestmentsHoldingsGetResponse` | `the_plaid_api/models/investments_holdings_get_response.py` |

### client.investments.investments_transactions_get

- **Route**: `POST /investments/transactions/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def investments_transactions_get(body: InvestmentsTransactionsGetRequest | InvestmentsTransactionsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `InvestmentsTransactionsGetResponse`
- **Returns (raw)**: `ApiResult[InvestmentsTransactionsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `InvestmentsTransactionsGetRequest` | `the_plaid_api/models/investments_transactions_get_request.py` |
| `InvestmentsTransactionsGetRequestDict` | `the_plaid_api/models/investments_transactions_get_request.py` |
| `InvestmentsTransactionsGetResponse` | `the_plaid_api/models/investments_transactions_get_response.py` |

