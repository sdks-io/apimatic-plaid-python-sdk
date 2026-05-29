
# Processor Stripe Bank Account Token Create Response

ProcessorStripeBankAccountTokenCreateResponse defines the response schema for `/processor/stripe/bank_account/create`

*This model accepts additional fields of type Any.*

## Structure

`ProcessorStripeBankAccountTokenCreateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stripe_bank_account_token` | `str` | Required | A token that can be sent to Stripe for use in making API calls to Plaid |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "stripe_bank_account_token": "stripe_bank_account_token0",
  "request_id": "request_id6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

