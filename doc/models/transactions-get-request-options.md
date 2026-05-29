
# Transactions Get Request Options

An optional object to be used with the request. If specified, `options` must not be `null`.

*This model accepts additional fields of type Any.*

## Structure

`TransactionsGetRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_ids` | `List[str]` | Optional | A list of `account_ids` to retrieve for the Item<br><br>Note: An error will be returned if a provided `account_id` is not associated with the Item. |
| `count` | `int` | Optional | The number of transactions to fetch.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 500` |
| `offset` | `int` | Optional | The number of transactions to skip. The default value is 0.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |
| `include_original_description` | `bool` | Optional | Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager.<br><br>**Default**: `False` |
| `include_personal_finance_category_beta` | `bool` | Optional | Include the `personal_finance_category` object in the response. This feature is currently in beta – to request access, contact transactions-feedback@plaid.com.<br><br>**Default**: `False` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "count": 100,
  "offset": 0,
  "include_original_description": false,
  "include_personal_finance_category_beta": false,
  "account_ids": [
    "account_ids9"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

