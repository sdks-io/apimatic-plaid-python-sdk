
# Payment Initiation Refund

PaymentInitiationRefund defines a payment initiation refund

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationRefund`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refund_id` | `str` | Required | The ID of the refund. Like all Plaid identifiers, the `refund_id` is case sensitive. |
| `amount` | [`PaymentAmount`](../../doc/models/payment-amount.md) | Required | The amount and currency of a payment |
| `status` | [`Status2`](../../doc/models/status-2.md) | Required | The status of the refund.<br><br>`PROCESSING`: The refund is currently being processed. The refund will automatically exit this state when processing is complete.<br><br>`INITIATED`: The refund has been successfully initiated.<br><br>`EXECUTED`: Indicates that the refund has been successfully executed.<br><br>`FAILED`: The refund has failed to be executed. This error is retryable once the root cause is resolved. |
| `last_status_update` | `datetime` | Required | The date and time of the last time the `status` was updated, in IS0 8601 format |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "refund_id": "refund_id8",
  "amount": {
    "currency": "GBP",
    "value": 52.3,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "status": "PROCESSING",
  "last_status_update": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

