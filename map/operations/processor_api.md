<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProcessorApi — operations

Accessor: `client.processor_api` · Source: `the_plaid_api/apis/processor_api.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.processor_api.processor_apex_processor_token_create

- **Route**: `POST /processor/apex/processor_token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def processor_apex_processor_token_create(body: ProcessorApexProcessorTokenCreateRequest | ProcessorApexProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTokenCreateResponse`
- **Returns (raw)**: `ApiResult[ProcessorTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorApexProcessorTokenCreateRequest` | `the_plaid_api/models/processor_apex_processor_token_create_request.py` |
| `ProcessorApexProcessorTokenCreateRequestDict` | `the_plaid_api/models/processor_apex_processor_token_create_request.py` |
| `ProcessorTokenCreateResponse` | `the_plaid_api/models/processor_token_create_response.py` |

### client.processor_api.processor_auth_get

- **Route**: `POST /processor/auth/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def processor_auth_get(body: ProcessorAuthGetRequest | ProcessorAuthGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorAuthGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorAuthGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorAuthGetRequest` | `the_plaid_api/models/processor_auth_get_request.py` |
| `ProcessorAuthGetRequestDict` | `the_plaid_api/models/processor_auth_get_request.py` |
| `ProcessorAuthGetResponse` | `the_plaid_api/models/processor_auth_get_response.py` |

### client.processor_api.processor_balance_get

- **Route**: `POST /processor/balance/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def processor_balance_get(body: ProcessorBalanceGetRequest | ProcessorBalanceGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorBalanceGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorBalanceGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorBalanceGetRequest` | `the_plaid_api/models/processor_balance_get_request.py` |
| `ProcessorBalanceGetRequestDict` | `the_plaid_api/models/processor_balance_get_request.py` |
| `ProcessorBalanceGetResponse` | `the_plaid_api/models/processor_balance_get_response.py` |

### client.processor_api.processor_bank_transfer_create

- **Route**: `POST /processor/bank_transfer/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def processor_bank_transfer_create(body: ProcessorBankTransferCreateRequest | ProcessorBankTransferCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorBankTransferCreateResponse`
- **Returns (raw)**: `ApiResult[ProcessorBankTransferCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorBankTransferCreateRequest` | `the_plaid_api/models/processor_bank_transfer_create_request.py` |
| `ProcessorBankTransferCreateRequestDict` | `the_plaid_api/models/processor_bank_transfer_create_request.py` |
| `ProcessorBankTransferCreateResponse` | `the_plaid_api/models/processor_bank_transfer_create_response.py` |

### client.processor_api.processor_identity_get

- **Route**: `POST /processor/identity/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def processor_identity_get(body: ProcessorIdentityGetRequest | ProcessorIdentityGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorIdentityGetResponse`
- **Returns (raw)**: `ApiResult[ProcessorIdentityGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorIdentityGetRequest` | `the_plaid_api/models/processor_identity_get_request.py` |
| `ProcessorIdentityGetRequestDict` | `the_plaid_api/models/processor_identity_get_request.py` |
| `ProcessorIdentityGetResponse` | `the_plaid_api/models/processor_identity_get_response.py` |

### client.processor_api.processor_stripe_bank_account_token_create

- **Route**: `POST /processor/stripe/bank_account_token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def processor_stripe_bank_account_token_create(body: ProcessorStripeBankAccountTokenCreateRequest | ProcessorStripeBankAccountTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorStripeBankAccountTokenCreateResponse`
- **Returns (raw)**: `ApiResult[ProcessorStripeBankAccountTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorStripeBankAccountTokenCreateRequest` | `the_plaid_api/models/processor_stripe_bank_account_token_create_request.py` |
| `ProcessorStripeBankAccountTokenCreateRequestDict` | `the_plaid_api/models/processor_stripe_bank_account_token_create_request.py` |
| `ProcessorStripeBankAccountTokenCreateResponse` | `the_plaid_api/models/processor_stripe_bank_account_token_create_response.py` |

### client.processor_api.processor_token_create

- **Route**: `POST /processor/token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def processor_token_create(body: ProcessorTokenCreateRequest | ProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ProcessorTokenCreateResponse`
- **Returns (raw)**: `ApiResult[ProcessorTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProcessorTokenCreateRequest` | `the_plaid_api/models/processor_token_create_request.py` |
| `ProcessorTokenCreateRequestDict` | `the_plaid_api/models/processor_token_create_request.py` |
| `ProcessorTokenCreateResponse` | `the_plaid_api/models/processor_token_create_response.py` |

