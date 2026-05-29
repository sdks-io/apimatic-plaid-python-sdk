
# Institutions Search Payment Initiation Options

Additional options that will be used to filter institutions by various Payment Initiation configurations.

*This model accepts additional fields of type Any.*

## Structure

`InstitutionsSearchPaymentInitiationOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_id` | `str` | Optional | A unique ID identifying the payment |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "payment_id": "payment_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

