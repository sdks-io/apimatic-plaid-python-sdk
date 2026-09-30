<!-- Generated file — do not edit; regenerated with the SDK. -->

# AssetReportApi — operations

Accessor: `client.asset_report_api` · Source: `the_plaid_api/apis/asset_report_api.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.asset_report_api.asset_report_audit_copy_create

- **Route**: `POST /asset_report/audit_copy/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_audit_copy_create(body: AssetReportAuditCopyCreateRequest | AssetReportAuditCopyCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportAuditCopyCreateResponse`
- **Returns (raw)**: `ApiResult[AssetReportAuditCopyCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportAuditCopyCreateRequest` | `the_plaid_api/models/asset_report_audit_copy_create_request.py` |
| `AssetReportAuditCopyCreateRequestDict` | `the_plaid_api/models/asset_report_audit_copy_create_request.py` |
| `AssetReportAuditCopyCreateResponse` | `the_plaid_api/models/asset_report_audit_copy_create_response.py` |

### client.asset_report_api.asset_report_audit_copy_get

- **Route**: `POST /asset_report/audit_copy/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_audit_copy_get(body: AssetReportAuditCopyGetRequest | AssetReportAuditCopyGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportGetResponse`
- **Returns (raw)**: `ApiResult[AssetReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportAuditCopyGetRequest` | `the_plaid_api/models/asset_report_audit_copy_get_request.py` |
| `AssetReportAuditCopyGetRequestDict` | `the_plaid_api/models/asset_report_audit_copy_get_request.py` |
| `AssetReportGetResponse` | `the_plaid_api/models/asset_report_get_response.py` |

### client.asset_report_api.asset_report_audit_copy_remove

- **Route**: `POST /asset_report/audit_copy/remove`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_audit_copy_remove(body: AssetReportAuditCopyRemoveRequest | AssetReportAuditCopyRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportAuditCopyRemoveResponse`
- **Returns (raw)**: `ApiResult[AssetReportAuditCopyRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportAuditCopyRemoveRequest` | `the_plaid_api/models/asset_report_audit_copy_remove_request.py` |
| `AssetReportAuditCopyRemoveRequestDict` | `the_plaid_api/models/asset_report_audit_copy_remove_request.py` |
| `AssetReportAuditCopyRemoveResponse` | `the_plaid_api/models/asset_report_audit_copy_remove_response.py` |

### client.asset_report_api.asset_report_create

- **Route**: `POST /asset_report/create`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_create(body: AssetReportCreateRequest | AssetReportCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportCreateResponse`
- **Returns (raw)**: `ApiResult[AssetReportCreateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportCreateRequest` | `the_plaid_api/models/asset_report_create_request.py` |
| `AssetReportCreateRequestDict` | `the_plaid_api/models/asset_report_create_request.py` |
| `AssetReportCreateResponse` | `the_plaid_api/models/asset_report_create_response.py` |

### client.asset_report_api.asset_report_filter

- **Route**: `POST /asset_report/filter`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_filter(body: AssetReportFilterRequest | AssetReportFilterRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportFilterResponse`
- **Returns (raw)**: `ApiResult[AssetReportFilterResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportFilterRequest` | `the_plaid_api/models/asset_report_filter_request.py` |
| `AssetReportFilterRequestDict` | `the_plaid_api/models/asset_report_filter_request.py` |
| `AssetReportFilterResponse` | `the_plaid_api/models/asset_report_filter_response.py` |

### client.asset_report_api.asset_report_get

- **Route**: `POST /asset_report/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_get(body: AssetReportGetRequest | AssetReportGetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportGetResponse`
- **Returns (raw)**: `ApiResult[AssetReportGetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportGetRequest` | `the_plaid_api/models/asset_report_get_request.py` |
| `AssetReportGetRequestDict` | `the_plaid_api/models/asset_report_get_request.py` |
| `AssetReportGetResponse` | `the_plaid_api/models/asset_report_get_response.py` |

### client.asset_report_api.asset_report_pdf_get

- **Route**: `POST /asset_report/pdf/get`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_pdf_get(body: AssetReportPdfgetRequest | AssetReportPdfgetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportPdfgetRequest` | `the_plaid_api/models/asset_report_pdfget_request.py` |
| `AssetReportPdfgetRequestDict` | `the_plaid_api/models/asset_report_pdfget_request.py` |

### client.asset_report_api.asset_report_refresh

- **Route**: `POST /asset_report/refresh`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_refresh(body: AssetReportRefreshRequest | AssetReportRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportRefreshResponse`
- **Returns (raw)**: `ApiResult[AssetReportRefreshResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportRefreshRequest` | `the_plaid_api/models/asset_report_refresh_request.py` |
| `AssetReportRefreshRequestDict` | `the_plaid_api/models/asset_report_refresh_request.py` |
| `AssetReportRefreshResponse` | `the_plaid_api/models/asset_report_refresh_response.py` |

### client.asset_report_api.asset_report_remove

- **Route**: `POST /asset_report/remove`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def asset_report_remove(body: AssetReportRemoveRequest | AssetReportRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AssetReportRemoveResponse`
- **Returns (raw)**: `ApiResult[AssetReportRemoveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssetReportRemoveRequest` | `the_plaid_api/models/asset_report_remove_request.py` |
| `AssetReportRemoveRequestDict` | `the_plaid_api/models/asset_report_remove_request.py` |
| `AssetReportRemoveResponse` | `the_plaid_api/models/asset_report_remove_response.py` |

