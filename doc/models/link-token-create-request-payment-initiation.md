
# Link Token Create Request Payment Initiation

Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if `payment_initiation` is included in the `products` array.

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenCreateRequestPaymentInitiation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `str` | Required | The `payment_id` provided by the `/payment_initiation/payment/create` endpoint.<br><br>**Constraints**: *Minimum Length*: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "payment_id": "payment_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

