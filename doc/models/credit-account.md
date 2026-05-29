
# Credit Account

A credit card type account. Supported products for `credit` accounts are: Balance, Transactions, Identity, and Liabilities.

*This model accepts additional fields of type Any.*

## Structure

`CreditAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit_card` | `str` | Required | Bank-issued credit card |
| `paypal` | `str` | Required | PayPal-issued credit card |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "credit card": "credit card2",
  "paypal": "paypal4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

