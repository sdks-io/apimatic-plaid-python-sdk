
# Income Verification Taxforms Get Request

IncomeVerificationTaxformsGetRequest defines the request schema for `/income/verification/taxforms/get`

*This model accepts additional fields of type Any.*

## Structure

`IncomeVerificationTaxformsGetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `income_verification_id` | `str` | Optional | The ID of the verification. |
| `access_token` | `str` | Optional | The access token associated with the Item data is being requested for. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id8",
  "secret": "secret2",
  "income_verification_id": "income_verification_id4",
  "access_token": "access_token4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

