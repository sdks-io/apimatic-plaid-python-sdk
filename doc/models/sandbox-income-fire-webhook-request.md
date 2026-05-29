
# Sandbox Income Fire Webhook Request

SandboxIncomeFireWebhookRequest defines the request schema for `/sandbox/income/fire_webhook`

*This model accepts additional fields of type Any.*

## Structure

`SandboxIncomeFireWebhookRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `income_verification_id` | `str` | Required | The ID of the verification. |
| `webhook` | `str` | Required | The URL to which the webhook should be sent. |
| `verification_status` | [`VerificationStatus3`](../../doc/models/verification-status-3.md) | Required | `VERIFICATION_STATUS_PROCESSING_COMPLETE`: The income verification status processing has completed.<br><br>`VERIFICATION_STATUS_DOCUMENT_REJECTED`: The documentation uploaded by the end user was recognized as a supported file format, but not recognized as a valid paystub.<br><br>`VERIFICATION_STATUS_PROCESSING_FAILED`: A failure occurred when attempting to process the verification documentation. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id4",
  "secret": "secret8",
  "income_verification_id": "income_verification_id0",
  "webhook": "webhook0",
  "verification_status": "VERIFICATION_STATUS_DOCUMENT_REJECTED",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

