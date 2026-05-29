
# Auth Supported Methods

Metadata specifically related to which auth methods an institution supports.

*This model accepts additional fields of type Any.*

## Structure

`AuthSupportedMethods`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `instant_auth` | `bool` | Required | Indicates if instant auth is supported. |
| `instant_match` | `bool` | Required | Indicates if instant match is supported. |
| `automated_micro_deposits` | `bool` | Required | Indicates if automated microdeposits are supported. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "instant_auth": false,
  "instant_match": false,
  "automated_micro_deposits": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

