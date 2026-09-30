<!-- Generated file — do not edit; regenerated with the SDK. -->

# Income — operations

Accessor: `client.income` · Source: `the_plaid_api/apis/income.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.income.income_verification_create

- **Route**: `POST /income/verification/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def income_verification_create(body: IncomeVerificationCreateRequest | IncomeVerificationCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationCreateResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationCreateRequest` | `the_plaid_api/models/income_verification_create_request.py` |
| `IncomeVerificationCreateRequestDict` | `the_plaid_api/models/income_verification_create_request.py` |
| `IncomeVerificationCreateResponse` | `the_plaid_api/models/income_verification_create_response.py` |

### client.income.income_verification_documents_download

- **Route**: `POST /income/verification/documents/download`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def income_verification_documents_download(body: IncomeVerificationDocumentsDownloadRequest | IncomeVerificationDocumentsDownloadRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationDocumentsDownloadRequest` | `the_plaid_api/models/income_verification_documents_download_request.py` |
| `IncomeVerificationDocumentsDownloadRequestDict` | `the_plaid_api/models/income_verification_documents_download_request.py` |

### client.income.income_verification_paystub_get

- **Route**: `POST /income/verification/paystub/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def income_verification_paystub_get(body: IncomeVerificationPaystubGetRequest | IncomeVerificationPaystubGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationPaystubGetResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationPaystubGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationPaystubGetRequest` | `the_plaid_api/models/income_verification_paystub_get_request.py` |
| `IncomeVerificationPaystubGetRequestDict` | `the_plaid_api/models/income_verification_paystub_get_request.py` |
| `IncomeVerificationPaystubGetResponse` | `the_plaid_api/models/income_verification_paystub_get_response.py` |

### client.income.income_verification_paystubs_get

- **Route**: `POST /income/verification/paystubs/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def income_verification_paystubs_get(body: IncomeVerificationPaystubsGetRequest | IncomeVerificationPaystubsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationPaystubsGetResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationPaystubsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationPaystubsGetRequest` | `the_plaid_api/models/income_verification_paystubs_get_request.py` |
| `IncomeVerificationPaystubsGetRequestDict` | `the_plaid_api/models/income_verification_paystubs_get_request.py` |
| `IncomeVerificationPaystubsGetResponse` | `the_plaid_api/models/income_verification_paystubs_get_response.py` |

### client.income.income_verification_precheck

- **Route**: `POST /income/verification/precheck`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def income_verification_precheck(body: IncomeVerificationPrecheckRequest | IncomeVerificationPrecheckRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationPrecheckResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationPrecheckResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationPrecheckRequest` | `the_plaid_api/models/income_verification_precheck_request.py` |
| `IncomeVerificationPrecheckRequestDict` | `the_plaid_api/models/income_verification_precheck_request.py` |
| `IncomeVerificationPrecheckResponse` | `the_plaid_api/models/income_verification_precheck_response.py` |

### client.income.income_verification_refresh

- **Route**: `POST /income/verification/refresh`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def income_verification_refresh(body: IncomeVerificationRefreshRequest | IncomeVerificationRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationRefreshResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationRefreshRequest` | `the_plaid_api/models/income_verification_refresh_request.py` |
| `IncomeVerificationRefreshRequestDict` | `the_plaid_api/models/income_verification_refresh_request.py` |
| `IncomeVerificationRefreshResponse` | `the_plaid_api/models/income_verification_refresh_response.py` |

### client.income.income_verification_summary_get

- **Route**: `POST /income/verification/summary/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def income_verification_summary_get(body: IncomeVerificationSummaryGetRequest | IncomeVerificationSummaryGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationSummaryGetResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationSummaryGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationSummaryGetRequest` | `the_plaid_api/models/income_verification_summary_get_request.py` |
| `IncomeVerificationSummaryGetRequestDict` | `the_plaid_api/models/income_verification_summary_get_request.py` |
| `IncomeVerificationSummaryGetResponse` | `the_plaid_api/models/income_verification_summary_get_response.py` |

### client.income.income_verification_taxforms_get

- **Route**: `POST /income/verification/taxforms/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def income_verification_taxforms_get(body: IncomeVerificationTaxformsGetRequest | IncomeVerificationTaxformsGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `IncomeVerificationTaxformsGetResponse`
- **Returns (raw)**: `ApiResult[IncomeVerificationTaxformsGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `IncomeVerificationTaxformsGetRequest` | `the_plaid_api/models/income_verification_taxforms_get_request.py` |
| `IncomeVerificationTaxformsGetRequestDict` | `the_plaid_api/models/income_verification_taxforms_get_request.py` |
| `IncomeVerificationTaxformsGetResponse` | `the_plaid_api/models/income_verification_taxforms_get_response.py` |

