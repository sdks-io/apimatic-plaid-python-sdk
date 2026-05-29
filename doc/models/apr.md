
# Apr

Information about the APR on the account.

*This model accepts additional fields of type Any.*

## Structure

`Apr`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apr_percentage` | `float` | Required | Annual Percentage Rate applied. |
| `apr_type` | [`AprType`](../../doc/models/apr-type.md) | Required | The type of balance to which the APR applies. |
| `balance_subject_to_apr` | `float` | Required | Amount of money that is subjected to the APR if a balance was carried beyond payment due date. How it is calculated can vary by card issuer. It is often calculated as an average daily balance. |
| `interest_charge_amount` | `float` | Required | Amount of money charged due to interest from last statement. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "apr_percentage": 181.06,
  "apr_type": "purchase_apr",
  "balance_subject_to_apr": 19.5,
  "interest_charge_amount": 108.38,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

