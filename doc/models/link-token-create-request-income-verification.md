
# Link Token Create Request Income Verification

Specifies options for initializing Link for use with the Income (beta) product. This field is required if `income_verification` is included in the `products` array.

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenCreateRequestIncomeVerification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `income_verification_id` | `str` | Required | The `income_verification_id` of the verification instance, as provided by `/income/verification/create`. |
| `asset_report_id` | `str` | Optional | The `asset_report_id` of an asset report associated with the user, as provided by `/asset_report/create`. Providing an `asset_report_id` is optional and can be used to verify the user through a streamlined flow. If provided, the bank linking flow will be skipped. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "income_verification_id": "income_verification_id2",
  "asset_report_id": "asset_report_id6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

