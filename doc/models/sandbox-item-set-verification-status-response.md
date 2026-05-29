
# Sandbox Item Set Verification Status Response

SandboxItemSetVerificationStatusResponse defines the response schema for `/sandbox/item/set_verification_status`

*This model accepts additional fields of type Any.*

## Structure

`SandboxItemSetVerificationStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "request_id": "request_id4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

