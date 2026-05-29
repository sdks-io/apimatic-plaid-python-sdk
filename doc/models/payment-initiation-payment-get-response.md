
# Payment Initiation Payment Get Response

PaymentInitiationPaymentGetResponse defines the response schema for `/payment_initation/payment/get`

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationPaymentGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `str` | Required | The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive. |
| `amount` | [`PaymentAmount`](../../doc/models/payment-amount.md) | Required | The amount and currency of a payment |
| `status` | [`Status3`](../../doc/models/status-3.md) | Required | The status of the payment.<br><br>`PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.<br><br>`PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.<br><br>`PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.<br><br>`PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.<br><br>`PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.<br><br>`PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.<br><br>`PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.<br><br>`PAYMENT_STATUS_UNKNOWN`: The payment status is unknown. |
| `recipient_id` | `str` | Required | The ID of the recipient |
| `reference` | `str` | Required | A reference for the payment. |
| `adjusted_reference` | `str` | Optional | The value of the reference sent to the bank after adjustment to pass bank validation rules. |
| `last_status_update` | `datetime` | Required | The date and time of the last time the `status` was updated, in IS0 8601 format |
| `schedule` | [`ExternalPaymentScheduleGet`](../../doc/models/external-payment-schedule-get.md) | Optional | The schedule that the payment will be executed on. If a schedule is provided, the payment is automatically set up as a standing order. If no schedule is specified, the payment will be executed only once. |
| `refund_details` | [`ExternalPaymentRefundDetails`](../../doc/models/external-payment-refund-details.md) | Optional | - |
| `bacs` | [`SenderBacsNullable`](../../doc/models/sender-bacs-nullable.md) | Required | - |
| `iban` | `str` | Required | The International Bank Account Number (IBAN) for the sender, if specified in the `/payment_initiation/payment/create` call. |
| `initiated_refunds` | [`List[PaymentInitiationRefund]`](../../doc/models/payment-initiation-refund.md) | Optional | Initiated refunds associated with the payment. |
| `emi_account_id` | `str` | Optional | The EMI (E-Money Institution) account that this payment is associated with, if any. This EMI account is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests.<br><br>**Constraints**: *Minimum Length*: `1` |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "payment_id": "payment_id8",
  "amount": {
    "currency": "GBP",
    "value": 52.3,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "status": "PAYMENT_STATUS_INITIATED",
  "recipient_id": "recipient_id2",
  "reference": "reference6",
  "adjusted_reference": "adjusted_reference2",
  "last_status_update": "2016-03-13T12:52:32.123Z",
  "schedule": {
    "interval": "WEEKLY",
    "interval_execution_day": 88,
    "start_date": "2016-03-13",
    "end_date": "2016-03-13",
    "adjusted_start_date": "2016-03-13",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "refund_details": {
    "name": "name8",
    "iban": "iban2",
    "bacs": {
      "account": "account4",
      "sort_code": "sort_code4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "bacs": {
    "account": "account4",
    "sort_code": "sort_code4",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "iban": "iban2",
  "initiated_refunds": [
    {
      "refund_id": "refund_id0",
      "amount": {
        "currency": "GBP",
        "value": 52.3,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "status": "INITIATED",
      "last_status_update": "2016-03-13T12:52:32.123Z",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "emi_account_id": "emi_account_id8",
  "request_id": "request_id0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

