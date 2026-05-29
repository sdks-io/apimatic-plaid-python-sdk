
# Sandbox Processor Token Create Request

*This model accepts additional fields of type Any.*

## Structure

`SandboxProcessorTokenCreateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body. |
| `secret` | `str` | Optional | Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body. |
| `institution_id` | `str` | Required | The ID of the institution the Item will be associated with |
| `options` | [`SandboxProcessorTokenCreateRequestOptions`](../../doc/models/sandbox-processor-token-create-request-options.md) | Optional | An optional set of options to be used when configuring the Item. If specified, must not be `null`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "client_id": "client_id8",
  "secret": "secret2",
  "institution_id": "institution_id4",
  "options": {
    "override_username": "override_username0",
    "override_password": "override_password8",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

