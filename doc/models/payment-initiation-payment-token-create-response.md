
# Payment Initiation Payment Token Create Response

PaymentInitiationPaymentTokenCreateResponse defines the response schema for `/payment_initiation/payment/token/create`

*This model accepts additional fields of type Any.*

## Structure

`PaymentInitiationPaymentTokenCreateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_token` | `str` | Required | A `payment_token` that can be provided to Link initialization to enter the payment initiation flow |
| `payment_token_expiration_time` | `datetime` | Required | The date and time at which the token will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. A `payment_token` expires after 15 minutes. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "payment_token": "payment_token4",
  "payment_token_expiration_time": "2016-03-13T12:52:32.123Z",
  "request_id": "request_id6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

