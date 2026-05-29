
# Payment Status Update Webhook

Fired when the status of a payment has changed.

*This model accepts additional fields of type Any.*

## Structure

`PaymentStatusUpdateWebhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_type` | `str` | Required | `PAYMENT_INITIATION` |
| `webhook_code` | `str` | Required | `PAYMENT_STATUS_UPDATE` |
| `payment_id` | `str` | Required | The `payment_id` for the payment being updated |
| `new_payment_status` | [`NewPaymentStatus`](../../doc/models/new-payment-status.md) | Required | The new status of the payment.<br><br>`PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.<br><br>`PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.<br><br>`PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.<br><br>`PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.<br><br>`PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.<br><br>`PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.<br><br>`PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.<br><br>`PAYMENT_STATUS_UNKNOWN`: The payment status is unknown. |
| `old_payment_status` | [`OldPaymentStatus`](../../doc/models/old-payment-status.md) | Required | The previous status of the payment.<br><br>`PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.<br><br>`PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.<br><br>`PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.<br><br>`PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.<br><br>`PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.<br><br>`PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.<br><br>`PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.<br><br>`PAYMENT_STATUS_UNKNOWN`: The payment status is unknown. |
| `original_reference` | `str` | Required | The original value of the reference when creating the payment. |
| `adjusted_reference` | `str` | Optional | The value of the reference sent to the bank after adjustment to pass bank validation rules. |
| `original_start_date` | `date` | Required | The original value of the `start_date` provided during the creation of a standing order. If the payment is not a standing order, this field will be `null`. |
| `adjusted_start_date` | `date` | Required | The start date sent to the bank after adjusting for holidays or weekends.  Will be provided in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). If the start date did not require adjustment, or if the payment is not a standing order, this field will be `null`. |
| `timestamp` | `datetime` | Required | The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. `"2017-09-14T14:42:19.350Z"` |
| `error` | [`Error`](../../doc/models/error.md) | Optional | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook_type": "webhook_type2",
  "webhook_code": "webhook_code8",
  "payment_id": "payment_id8",
  "new_payment_status": "PAYMENT_STATUS_BLOCKED",
  "old_payment_status": "PAYMENT_STATUS_BLOCKED",
  "original_reference": "original_reference4",
  "adjusted_reference": "adjusted_reference8",
  "original_start_date": "2016-03-13",
  "adjusted_start_date": "2016-03-13",
  "timestamp": "2016-03-13T12:52:32.123Z",
  "error": {
    "error_type": "RECAPTCHA_ERROR",
    "error_code": "error_code6",
    "error_message": "error_message6",
    "display_message": "display_message8",
    "request_id": "request_id4",
    "causes": [
      {
        "key1": "val1",
        "key2": "val2"
      },
      {
        "key1": "val1",
        "key2": "val2"
      },
      {
        "key1": "val1",
        "key2": "val2"
      }
    ],
    "status": 217.06,
    "documentation_url": "documentation_url6",
    "suggested_action": "suggested_action0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

