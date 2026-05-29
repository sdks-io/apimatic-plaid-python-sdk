
# Payment Initiation Metadata

Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests.

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `supports_international_payments` | `bool` | Required | Indicates whether the institution supports payments from a different country. |
| `maximum_payment_amount` | `Dict[str, str]` | Required | A mapping of currency to maximum payment amount (denominated in the smallest unit of currency) supported by the insitution.<br><br>Example: `{"GBP": "10000"}` |
| `supports_refund_details` | `bool` | Required | Indicates whether the institution supports returning refund details when initiating a payment. |
| `standing_order_metadata` | [`PaymentInitiationStandingOrderMetadata`](../../doc/models/payment-initiation-standing-order-metadata.md) | Required | Metadata specifically related to valid Payment Initiation standing order configurations for the institution. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "supports_international_payments": false,
  "maximum_payment_amount": {
    "key0": "maximum_payment_amount7",
    "key1": "maximum_payment_amount8",
    "key2": "maximum_payment_amount9"
  },
  "supports_refund_details": false,
  "standing_order_metadata": {
    "supports_standing_order_end_date": false,
    "supports_standing_order_negative_execution_days": false,
    "valid_standing_order_intervals": [
      "WEEKLY",
      "MONTHLY"
    ],
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

