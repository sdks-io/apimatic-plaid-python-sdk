<!-- Generated file — do not edit; regenerated with the SDK. -->

# DepositSwitch — operations

Accessor: `client.deposit_switch` · Source: `the_plaid_api/apis/deposit_switch.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.deposit_switch.deposit_switch_alt_create

- **Route**: `POST /deposit_switch/alt/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def deposit_switch_alt_create(body: DepositSwitchAltCreateRequest | DepositSwitchAltCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DepositSwitchAltCreateResponse`
- **Returns (raw)**: `ApiResult[DepositSwitchAltCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DepositSwitchAltCreateRequest` | `the_plaid_api/models/deposit_switch_alt_create_request.py` |
| `DepositSwitchAltCreateRequestDict` | `the_plaid_api/models/deposit_switch_alt_create_request.py` |
| `DepositSwitchAltCreateResponse` | `the_plaid_api/models/deposit_switch_alt_create_response.py` |

### client.deposit_switch.deposit_switch_create

- **Route**: `POST /deposit_switch/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def deposit_switch_create(body: DepositSwitchCreateRequest | DepositSwitchCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DepositSwitchCreateResponse`
- **Returns (raw)**: `ApiResult[DepositSwitchCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DepositSwitchCreateRequest` | `the_plaid_api/models/deposit_switch_create_request.py` |
| `DepositSwitchCreateRequestDict` | `the_plaid_api/models/deposit_switch_create_request.py` |
| `DepositSwitchCreateResponse` | `the_plaid_api/models/deposit_switch_create_response.py` |

### client.deposit_switch.deposit_switch_get

- **Route**: `POST /deposit_switch/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def deposit_switch_get(body: DepositSwitchGetRequest | DepositSwitchGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DepositSwitchGetResponse`
- **Returns (raw)**: `ApiResult[DepositSwitchGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DepositSwitchGetRequest` | `the_plaid_api/models/deposit_switch_get_request.py` |
| `DepositSwitchGetRequestDict` | `the_plaid_api/models/deposit_switch_get_request.py` |
| `DepositSwitchGetResponse` | `the_plaid_api/models/deposit_switch_get_response.py` |

### client.deposit_switch.deposit_switch_token_create

- **Route**: `POST /deposit_switch/token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def deposit_switch_token_create(body: DepositSwitchTokenCreateRequest | DepositSwitchTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DepositSwitchTokenCreateResponse`
- **Returns (raw)**: `ApiResult[DepositSwitchTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DepositSwitchTokenCreateRequest` | `the_plaid_api/models/deposit_switch_token_create_request.py` |
| `DepositSwitchTokenCreateRequestDict` | `the_plaid_api/models/deposit_switch_token_create_request.py` |
| `DepositSwitchTokenCreateResponse` | `the_plaid_api/models/deposit_switch_token_create_response.py` |

