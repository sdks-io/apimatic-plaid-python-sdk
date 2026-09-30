<!-- Generated file — do not edit; regenerated with the SDK. -->

# Sandbox — operations

Accessor: `client.sandbox` · Source: `the_plaid_api/apis/sandbox.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sandbox.sandbox_bank_transfer_fire_webhook

- **Route**: `POST /sandbox/bank_transfer/fire_webhook`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_bank_transfer_fire_webhook(body: SandboxBankTransferFireWebhookRequest | SandboxBankTransferFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxBankTransferFireWebhookResponse`
- **Returns (raw)**: `ApiResult[SandboxBankTransferFireWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxBankTransferFireWebhookRequest` | `the_plaid_api/models/sandbox_bank_transfer_fire_webhook_request.py` |
| `SandboxBankTransferFireWebhookRequestDict` | `the_plaid_api/models/sandbox_bank_transfer_fire_webhook_request.py` |
| `SandboxBankTransferFireWebhookResponse` | `the_plaid_api/models/sandbox_bank_transfer_fire_webhook_response.py` |

### client.sandbox.sandbox_bank_transfer_simulate

- **Route**: `POST /sandbox/bank_transfer/simulate`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_bank_transfer_simulate(body: SandboxBankTransferSimulateRequest | SandboxBankTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxBankTransferSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxBankTransferSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxBankTransferSimulateRequest` | `the_plaid_api/models/sandbox_bank_transfer_simulate_request.py` |
| `SandboxBankTransferSimulateRequestDict` | `the_plaid_api/models/sandbox_bank_transfer_simulate_request.py` |
| `SandboxBankTransferSimulateResponse` | `the_plaid_api/models/sandbox_bank_transfer_simulate_response.py` |

### client.sandbox.sandbox_income_fire_webhook

- **Route**: `POST /sandbox/income/fire_webhook`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_income_fire_webhook(body: SandboxIncomeFireWebhookRequest | SandboxIncomeFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxIncomeFireWebhookResponse`
- **Returns (raw)**: `ApiResult[SandboxIncomeFireWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxIncomeFireWebhookRequest` | `the_plaid_api/models/sandbox_income_fire_webhook_request.py` |
| `SandboxIncomeFireWebhookRequestDict` | `the_plaid_api/models/sandbox_income_fire_webhook_request.py` |
| `SandboxIncomeFireWebhookResponse` | `the_plaid_api/models/sandbox_income_fire_webhook_response.py` |

### client.sandbox.sandbox_item_fire_webhook

- **Route**: `POST /sandbox/item/fire_webhook`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_item_fire_webhook(body: SandboxItemFireWebhookRequest | SandboxItemFireWebhookRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxItemFireWebhookResponse`
- **Returns (raw)**: `ApiResult[SandboxItemFireWebhookResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxItemFireWebhookRequest` | `the_plaid_api/models/sandbox_item_fire_webhook_request.py` |
| `SandboxItemFireWebhookRequestDict` | `the_plaid_api/models/sandbox_item_fire_webhook_request.py` |
| `SandboxItemFireWebhookResponse` | `the_plaid_api/models/sandbox_item_fire_webhook_response.py` |

### client.sandbox.sandbox_item_reset_login

- **Route**: `POST /sandbox/item/reset_login`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_item_reset_login(body: SandboxItemResetLoginRequest | SandboxItemResetLoginRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxItemResetLoginResponse`
- **Returns (raw)**: `ApiResult[SandboxItemResetLoginResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxItemResetLoginRequest` | `the_plaid_api/models/sandbox_item_reset_login_request.py` |
| `SandboxItemResetLoginRequestDict` | `the_plaid_api/models/sandbox_item_reset_login_request.py` |
| `SandboxItemResetLoginResponse` | `the_plaid_api/models/sandbox_item_reset_login_response.py` |

### client.sandbox.sandbox_item_set_verification_status

- **Route**: `POST /sandbox/item/set_verification_status`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_item_set_verification_status(body: SandboxItemSetVerificationStatusRequest | SandboxItemSetVerificationStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxItemSetVerificationStatusResponse`
- **Returns (raw)**: `ApiResult[SandboxItemSetVerificationStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxItemSetVerificationStatusRequest` | `the_plaid_api/models/sandbox_item_set_verification_status_request.py` |
| `SandboxItemSetVerificationStatusRequestDict` | `the_plaid_api/models/sandbox_item_set_verification_status_request.py` |
| `SandboxItemSetVerificationStatusResponse` | `the_plaid_api/models/sandbox_item_set_verification_status_response.py` |

### client.sandbox.sandbox_oauth_select_accounts

- **Route**: `POST /sandbox/oauth/select_accounts`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_oauth_select_accounts(body: SandboxOauthSelectAccountsRequest | SandboxOauthSelectAccountsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxOauthSelectAccountsRequest` | `the_plaid_api/models/sandbox_oauth_select_accounts_request.py` |
| `SandboxOauthSelectAccountsRequestDict` | `the_plaid_api/models/sandbox_oauth_select_accounts_request.py` |

### client.sandbox.sandbox_processor_token_create

- **Route**: `POST /sandbox/processor_token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_processor_token_create(body: SandboxProcessorTokenCreateRequest | SandboxProcessorTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxProcessorTokenCreateResponse`
- **Returns (raw)**: `ApiResult[SandboxProcessorTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxProcessorTokenCreateRequest` | `the_plaid_api/models/sandbox_processor_token_create_request.py` |
| `SandboxProcessorTokenCreateRequestDict` | `the_plaid_api/models/sandbox_processor_token_create_request.py` |
| `SandboxProcessorTokenCreateResponse` | `the_plaid_api/models/sandbox_processor_token_create_response.py` |

### client.sandbox.sandbox_public_token_create

- **Route**: `POST /sandbox/public_token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_public_token_create(body: SandboxPublicTokenCreateRequest | SandboxPublicTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxPublicTokenCreateResponse`
- **Returns (raw)**: `ApiResult[SandboxPublicTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxPublicTokenCreateRequest` | `the_plaid_api/models/sandbox_public_token_create_request.py` |
| `SandboxPublicTokenCreateRequestDict` | `the_plaid_api/models/sandbox_public_token_create_request.py` |
| `SandboxPublicTokenCreateResponse` | `the_plaid_api/models/sandbox_public_token_create_response.py` |

### client.sandbox.sandbox_transfer_simulate

- **Route**: `POST /sandbox/transfer/simulate`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def sandbox_transfer_simulate(body: SandboxTransferSimulateRequest | SandboxTransferSimulateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SandboxTransferSimulateResponse`
- **Returns (raw)**: `ApiResult[SandboxTransferSimulateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SandboxTransferSimulateRequest` | `the_plaid_api/models/sandbox_transfer_simulate_request.py` |
| `SandboxTransferSimulateRequestDict` | `the_plaid_api/models/sandbox_transfer_simulate_request.py` |
| `SandboxTransferSimulateResponse` | `the_plaid_api/models/sandbox_transfer_simulate_response.py` |

