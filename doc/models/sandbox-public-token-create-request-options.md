
# Sandbox Public Token Create Request Options

An optional set of options to be used when configuring the Item. If specified, must not be `null`.

*This model accepts additional fields of type Any.*

## Structure

`SandboxPublicTokenCreateRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook` | `str` | Optional | Specify a webhook to associate with the new Item. |
| `override_username` | `str` | Optional | Test username to use for the creation of the Sandbox Item. Default value is `user_good`.<br><br>**Default**: `"user_good"` |
| `override_password` | `str` | Optional | Test password to use for the creation of the Sandbox Item. Default value is `pass_good`.<br><br>**Default**: `"pass_good"` |
| `transactions` | [`SandboxPublicTokenCreateRequestOptionsTransactions`](../../doc/models/sandbox-public-token-create-request-options-transactions.md) | Optional | SandboxPublicTokenCreateRequestOptionsTransactions is an optional set of parameters corresponding to transactions options. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "override_username": "user_good",
  "override_password": "pass_good",
  "webhook": "webhook8",
  "transactions": {
    "start_date": "2016-03-13",
    "end_date": "2016-03-13",
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

