
# Sandbox Processor Token Create Request Options

An optional set of options to be used when configuring the Item. If specified, must not be `null`.

*This model accepts additional fields of type Any.*

## Structure

`SandboxProcessorTokenCreateRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `override_username` | `str` | Optional | Test username to use for the creation of the Sandbox Item. Default value is `user_good`.<br><br>**Default**: `"user_good"` |
| `override_password` | `str` | Optional | Test password to use for the creation of the Sandbox Item. Default value is `pass_good`.<br><br>**Default**: `"pass_good"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "override_username": "user_good",
  "override_password": "pass_good",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

