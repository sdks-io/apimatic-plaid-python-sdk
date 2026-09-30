<!-- Generated file — do not edit; regenerated with the SDK. -->

# PaymentInitiation — operations

Accessor: `client.payment_initiation` · Source: `the_plaid_api/apis/payment_initiation.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payment_initiation.create_payment_token

- **Route**: `POST /payment_initiation/payment/token/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def create_payment_token(body: PaymentInitiationPaymentTokenCreateRequest | PaymentInitiationPaymentTokenCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentTokenCreateResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentTokenCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentTokenCreateRequest` | `the_plaid_api/models/payment_initiation_payment_token_create_request.py` |
| `PaymentInitiationPaymentTokenCreateRequestDict` | `the_plaid_api/models/payment_initiation_payment_token_create_request.py` |
| `PaymentInitiationPaymentTokenCreateResponse` | `the_plaid_api/models/payment_initiation_payment_token_create_response.py` |

### client.payment_initiation.payment_initiation_payment_create

- **Route**: `POST /payment_initiation/payment/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def payment_initiation_payment_create(body: PaymentInitiationPaymentCreateRequest | PaymentInitiationPaymentCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentCreateResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentCreateRequest` | `the_plaid_api/models/payment_initiation_payment_create_request.py` |
| `PaymentInitiationPaymentCreateRequestDict` | `the_plaid_api/models/payment_initiation_payment_create_request.py` |
| `PaymentInitiationPaymentCreateResponse` | `the_plaid_api/models/payment_initiation_payment_create_response.py` |

### client.payment_initiation.payment_initiation_payment_get

- **Route**: `POST /payment_initiation/payment/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def payment_initiation_payment_get(body: PaymentInitiationPaymentGetRequest | PaymentInitiationPaymentGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentGetResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentGetRequest` | `the_plaid_api/models/payment_initiation_payment_get_request.py` |
| `PaymentInitiationPaymentGetRequestDict` | `the_plaid_api/models/payment_initiation_payment_get_request.py` |
| `PaymentInitiationPaymentGetResponse` | `the_plaid_api/models/payment_initiation_payment_get_response.py` |

### client.payment_initiation.payment_initiation_payment_list

- **Route**: `POST /payment_initiation/payment/list`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def payment_initiation_payment_list(body: PaymentInitiationPaymentListRequest | PaymentInitiationPaymentListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentListResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentListRequest` | `the_plaid_api/models/payment_initiation_payment_list_request.py` |
| `PaymentInitiationPaymentListRequestDict` | `the_plaid_api/models/payment_initiation_payment_list_request.py` |
| `PaymentInitiationPaymentListResponse` | `the_plaid_api/models/payment_initiation_payment_list_response.py` |

### client.payment_initiation.payment_initiation_payment_reverse

- **Route**: `POST /payment_initiation/payment/reverse`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def payment_initiation_payment_reverse(body: PaymentInitiationPaymentReverseRequest | PaymentInitiationPaymentReverseRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationPaymentReverseResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationPaymentReverseResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationPaymentReverseRequest` | `the_plaid_api/models/payment_initiation_payment_reverse_request.py` |
| `PaymentInitiationPaymentReverseRequestDict` | `the_plaid_api/models/payment_initiation_payment_reverse_request.py` |
| `PaymentInitiationPaymentReverseResponse` | `the_plaid_api/models/payment_initiation_payment_reverse_response.py` |

### client.payment_initiation.payment_initiation_recipient_create

- **Route**: `POST /payment_initiation/recipient/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def payment_initiation_recipient_create(body: PaymentInitiationRecipientCreateRequest | PaymentInitiationRecipientCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationRecipientCreateResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationRecipientCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationRecipientCreateRequest` | `the_plaid_api/models/payment_initiation_recipient_create_request.py` |
| `PaymentInitiationRecipientCreateRequestDict` | `the_plaid_api/models/payment_initiation_recipient_create_request.py` |
| `PaymentInitiationRecipientCreateResponse` | `the_plaid_api/models/payment_initiation_recipient_create_response.py` |

### client.payment_initiation.payment_initiation_recipient_get

- **Route**: `POST /payment_initiation/recipient/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def payment_initiation_recipient_get(body: PaymentInitiationRecipientGetRequest | PaymentInitiationRecipientGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationRecipientGetResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationRecipientGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationRecipientGetRequest` | `the_plaid_api/models/payment_initiation_recipient_get_request.py` |
| `PaymentInitiationRecipientGetRequestDict` | `the_plaid_api/models/payment_initiation_recipient_get_request.py` |
| `PaymentInitiationRecipientGetResponse` | `the_plaid_api/models/payment_initiation_recipient_get_response.py` |

### client.payment_initiation.payment_initiation_recipient_list

- **Route**: `POST /payment_initiation/recipient/list`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def payment_initiation_recipient_list(body: PaymentInitiationRecipientListRequest | PaymentInitiationRecipientListRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PaymentInitiationRecipientListResponse`
- **Returns (raw)**: `ApiResult[PaymentInitiationRecipientListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PaymentInitiationRecipientListRequest` | `the_plaid_api/models/payment_initiation_recipient_list_request.py` |
| `PaymentInitiationRecipientListRequestDict` | `the_plaid_api/models/payment_initiation_recipient_list_request.py` |
| `PaymentInitiationRecipientListResponse` | `the_plaid_api/models/payment_initiation_recipient_list_response.py` |

