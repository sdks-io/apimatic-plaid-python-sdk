<!-- Generated file — do not edit; regenerated with the SDK. -->

# Signal — operations

Accessor: `client.signal` · Source: `the_plaid_api/apis/signal.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.signal.signal_decision_report

- **Route**: `POST /signal/decision/report`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def signal_decision_report(body: SignalDecisionReportRequest | SignalDecisionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SignalDecisionReportResponse`
- **Returns (raw)**: `ApiResult[SignalDecisionReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SignalDecisionReportRequest` | `the_plaid_api/models/signal_decision_report_request.py` |
| `SignalDecisionReportRequestDict` | `the_plaid_api/models/signal_decision_report_request.py` |
| `SignalDecisionReportResponse` | `the_plaid_api/models/signal_decision_report_response.py` |

### client.signal.signal_evaluate

- **Route**: `POST /signal/evaluate`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def signal_evaluate(body: SignalEvaluateRequest | SignalEvaluateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SignalEvaluateResponse`
- **Returns (raw)**: `ApiResult[SignalEvaluateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SignalEvaluateRequest` | `the_plaid_api/models/signal_evaluate_request.py` |
| `SignalEvaluateRequestDict` | `the_plaid_api/models/signal_evaluate_request.py` |
| `SignalEvaluateResponse` | `the_plaid_api/models/signal_evaluate_response.py` |

### client.signal.signal_return_report

- **Route**: `POST /signal/return/report`
- **Auth**: `plaid_client_id` AND `plaid_secret` AND `plaid_version`
- **Signature**: `def signal_return_report(body: SignalReturnReportRequest | SignalReturnReportRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SignalReturnReportResponse`
- **Returns (raw)**: `ApiResult[SignalReturnReportResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SignalReturnReportRequest` | `the_plaid_api/models/signal_return_report_request.py` |
| `SignalReturnReportRequestDict` | `the_plaid_api/models/signal_return_report_request.py` |
| `SignalReturnReportResponse` | `the_plaid_api/models/signal_return_report_response.py` |

