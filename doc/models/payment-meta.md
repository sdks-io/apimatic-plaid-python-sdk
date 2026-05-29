
# Payment Meta

Transaction information specific to inter-bank transfers. If the transaction was not an inter-bank transfer, all fields will be `null`.

If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, the `payment_meta` key will always appear, but no data elements are guaranteed. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.

*This model accepts additional fields of type Any.*

## Structure

`PaymentMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reference_number` | `str` | Required | The transaction reference number supplied by the financial institution. |
| `ppd_id` | `str` | Required | The ACH PPD ID for the payer. |
| `payee` | `str` | Required | For transfers, the party that is receiving the transaction. |
| `by_order_of` | `str` | Required | The party initiating a wire transfer. Will be `null` if the transaction is not a wire transfer. |
| `payer` | `str` | Required | For transfers, the party that is paying the transaction. |
| `payment_method` | `str` | Required | The type of transfer, e.g. 'ACH' |
| `payment_processor` | `str` | Required | The name of the payment processor |
| `reason` | `str` | Required | The payer-supplied description of the transfer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "reference_number": "reference_number8",
  "ppd_id": "ppd_id2",
  "payee": "payee8",
  "by_order_of": "by_order_of4",
  "payer": "payer6",
  "payment_method": "payment_method2",
  "payment_processor": "payment_processor2",
  "reason": "reason8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

