
# Depository

A filter to apply to `depository`-type accounts

*This model accepts additional fields of type Any.*

## Structure

`Depository`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_subtypes` | [`List[AccountSubtype]`](../../doc/models/account-subtype.md) | Optional | An array of account subtypes to display in Link. If not specified, all account subtypes will be shown. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#accounts-schema). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account_subtypes": [
    "cash isa",
    "education savings account",
    "ebt"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

