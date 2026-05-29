
# Link Token Eu Config

Configuration parameters for EU flows

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenEuConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `headless` | `bool` | Optional | If `true`, open Link without an initial UI. Defaults to `false`. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "headless": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

