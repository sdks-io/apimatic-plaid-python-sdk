
# Payment Amount

The amount and currency of a payment

*This model accepts additional fields of type Any.*

## Structure

`PaymentAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | [`Currency`](../../doc/models/currency.md) | Required | The ISO-4217 currency code of the payment. For standing orders, `"GBP"` must be used. |
| `value` | `float` | Required | The amount of the payment. Must contain at most two digits of precision e.g. `1.23`. Minimum accepted value is `1`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "currency": "GBP",
  "value": 106.08,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

