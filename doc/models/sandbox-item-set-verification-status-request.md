
# Sandbox Item Set Verification Status Request

SandboxItemSetVerificationStatusRequest defines the request schema for `/sandbox/item/set_verification_status`

*This model accepts additional fields of type Any.*

## Structure

`SandboxItemSetVerificationStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `access_token` | `str` | Required | The access token associated with the Item data is being requested for. |
| `account_id` | `str` | Required | The `account_id` of the account whose verification status is to be modified |
| `verification_status` | [`VerificationStatus1`](../../doc/models/verification-status-1.md) | Required | The verification status to set the account to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id2",
  "secret": "secret4",
  "access_token": "access_token8",
  "account_id": "account_id2",
  "verification_status": "automatically_verified",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

