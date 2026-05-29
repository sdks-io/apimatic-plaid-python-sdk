
# Payment Initiation Payment Create Response

PaymentInitiationPaymentCreateResponse defines the response schema for `/payment_initiation/payment/create`

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationPaymentCreateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `str` | Required | A unique ID identifying the payment |
| `status` | `str` | Required | For a payment returned by this endpoint, there is only one possible value:<br><br>`PAYMENT_STATUS_INPUT_NEEDED`: The initial phase of the payment |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "payment_id": "payment_id8",
  "status": "PAYMENT_STATUS_INPUT_NEEDED",
  "request_id": "request_id0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

