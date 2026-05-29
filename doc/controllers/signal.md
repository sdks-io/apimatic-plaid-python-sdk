# Signal

```python
signal_api = client.signal
```

## Class Name

`SignalApi`

## Methods

* [Signal Evaluate](../../doc/controllers/signal.md#signal-evaluate)
* [Signal Decision Report](../../doc/controllers/signal.md#signal-decision-report)
* [Signal Return Report](../../doc/controllers/signal.md#signal-return-report)


# Signal Evaluate

Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause.

Find out more here: [/signal/reference#signalevaluate](/signal/reference#signalevaluate)

```python
def signal_evaluate(self,
                   body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SignalEvaluateRequest`](../../doc/models/signal-evaluate-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SignalEvaluateResponse`](../../doc/models/signal-evaluate-response.md).

## Example Usage

```python
body = SignalEvaluateRequest(
    access_token='access_token4',
    account_id='account_id8',
    client_transaction_id='client_transaction_id6',
    amount=78.98
)

result = signal_api.signal_evaluate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "scores": {
    "customer_initiated_return_risk": {
      "score": 9,
      "risk_tier": 1
    },
    "bank_initiated_return_risk": {
      "score": 72,
      "risk_tier": 7
    }
  },
  "core_attributes": {
    "unauthorized_transactions_count_7d": 0,
    "unauthorized_transactions_count_30d": 0,
    "unauthorized_transactions_count_60d": 0,
    "unauthorized_transactions_count_90d": 0,
    "nsf_overdraft_transactions_count_7d": 1,
    "nsf_overdraft_transactions_count_30d": 1,
    "nsf_overdraft_transactions_count_60d": 2,
    "nsf_overdraft_transactions_count_90d": 2,
    "days_since_first_plaid_connection": 510,
    "plaid_connections_count_7d": 6,
    "plaid_connections_count_30d": 7,
    "total_plaid_connections_count": 15,
    "is_savings_or_money_market_account": false,
    "total_credit_transactions_amount_10d": 507.04,
    "total_debit_transactions_amount_10d": 590.14,
    "p50_credit_transactions_amount_28d": 46.79,
    "p50_debit_transactions_amount_28d": 75,
    "p95_credit_transactions_amount_28d": 155.95,
    "p95_debit_transactions_amount_28d": 799.59,
    "days_with_negative_balance_count_90d": 0,
    "p90_eod_balance_30d": 555.71,
    "p90_eod_balance_60d": 449.96,
    "p90_eod_balance_90d": 434.38,
    "p10_eod_balance_30d": 320.44,
    "p10_eod_balance_60d": 320.46,
    "p10_eod_balance_90d": 320.23,
    "available_balance": 420.22,
    "current_balance": 476,
    "balance_last_updated": "2021-02-25T09:18:21Z",
    "phone_change_count_28d": 0,
    "phone_change_count_90d": 0,
    "email_change_count_28d": 0,
    "email_change_count_90d": 0,
    "address_change_count_28d": 0,
    "address_change_count_90d": 0
  },
  "request_id": "mdqfuVxeoza6mhu"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Signal Decision Report

After calling `/signal/evaluate`, call `/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an `INVALID_REQUEST` error if called a second time with a different value for `initiated`.

Find out more here: [/signal/reference#signaldecisionreport](/signal/reference#signaldecisionreport)

```python
def signal_decision_report(self,
                          body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SignalDecisionReportRequest`](../../doc/models/signal-decision-report-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SignalDecisionReportResponse`](../../doc/models/signal-decision-report-response.md).

## Example Usage

```python
body = SignalDecisionReportRequest(
    client_transaction_id='client_transaction_id6',
    initiated=False
)

result = signal_api.signal_decision_report(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "request_id": "mdqfuVxeoza6mhu"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Signal Return Report

Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

Find out more here: [/signal/reference#signalreturnreport](/signal/reference#signalreturnreport)

```python
def signal_return_report(self,
                        body)
```

## Authentication

This endpoint requires [PLAID-CLIENT-ID](../../doc/auth/custom-header-signature.md) **AND** [PLAID-SECRET](../../doc/auth/custom-header-signature-1.md) **AND** [Plaid-Version](../../doc/auth/custom-header-signature-2.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SignalReturnReportRequest`](../../doc/models/signal-return-report-request.md) | Body, Required | - |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SignalReturnReportResponse`](../../doc/models/signal-return-report-response.md).

## Example Usage

```python
body = SignalReturnReportRequest(
    client_transaction_id='client_transaction_id6',
    return_code='return_code6'
)

result = signal_api.signal_return_report(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "request_id": "mdqfuVxeoza6mhu"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

