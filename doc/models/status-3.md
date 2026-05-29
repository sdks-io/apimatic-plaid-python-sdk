
# Status 3

The status of the payment.

`PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.

`PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.

`PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.

`PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.

`PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.

`PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.

`PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.

`PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.

*This model accepts additional fields of type Any.*

## Enumeration

`Status3`

## Fields

| Name |
|  --- |
| `PAYMENT_STATUS_INPUT_NEEDED` |
| `PAYMENT_STATUS_PROCESSING` |
| `PAYMENT_STATUS_INITIATED` |
| `PAYMENT_STATUS_COMPLETED` |
| `PAYMENT_STATUS_INSUFFICIENT_FUNDS` |
| `PAYMENT_STATUS_FAILED` |
| `PAYMENT_STATUS_BLOCKED` |
| `PAYMENT_STATUS_UNKNOWN` |

