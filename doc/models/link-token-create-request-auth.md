
# Link Token Create Request Auth

Specifies options for initializing Link for use with the Auth product. This field is currently only required if using the Flexible Auth product (currently in closed beta).

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenCreateRequestAuth`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `flow_type` | `str` | Required | The optional Auth flow to use. Currently only used to enable Flexible Auth. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "flow_type": "FLEXIBLE_AUTH",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

