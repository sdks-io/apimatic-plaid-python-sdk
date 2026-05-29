
# Deposit Switch Create Request Options

Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`.

*This model accepts additional fields of type Any.*

## Structure

`DepositSwitchCreateRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook` | `str` | Optional | The URL registered to receive webhooks when the status of a deposit switch request has changed. |
| `transaction_item_access_tokens` | `List[str]` | Optional | An array of access tokens corresponding to transaction items to use when attempting to match the user to their Payroll Provider. These tokens must be created by the same client id as the one creating the switch, and have access to the transactions product.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `99` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "webhook": "webhook4",
  "transaction_item_access_tokens": [
    "transaction_item_access_tokens8",
    "transaction_item_access_tokens9",
    "transaction_item_access_tokens0"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

