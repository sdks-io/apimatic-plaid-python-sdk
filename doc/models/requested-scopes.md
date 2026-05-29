
# Requested Scopes

Scope of required and optional account features or content from a ConnectedApplication.

*This model accepts additional fields of type Any.*

## Structure

`RequestedScopes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_product_access` | [`ProductAccess`](../../doc/models/product-access.md) | Required | The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed. |
| `optional_product_access` | [`ProductAccess`](../../doc/models/product-access.md) | Required | The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed. |
| `account_filters` | [`AccountFilter`](../../doc/models/account-filter.md) | Optional | Enumerates the account subtypes that the application wishes for the user to be able to select from. For more details refer to Plaid documentation on account filters. |
| `account_selection_cardinality` | [`AccountSelectionCardinality`](../../doc/models/account-selection-cardinality.md) | Required | The application requires that accounts be limited to a specific cardinality.<br>`MULTI_SELECT`: indicates that the user should be allowed to pick multiple accounts.<br>`SINGLE_SELECT`: indicates that the user should be allowed to pick only a single account.<br>`ALL`: indicates that the user must share all of their accounts and should not be given the opportunity to de-select |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "required_product_access": {
    "statements": true,
    "identity": true,
    "auth": true,
    "transactions": true,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "optional_product_access": {
    "statements": true,
    "identity": true,
    "auth": true,
    "transactions": true,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "account_selection_cardinality": "ALL",
  "account_filters": {
    "depository": [
      "depository1",
      "depository2"
    ],
    "credit": [
      "credit2"
    ],
    "loan": [
      "loan9"
    ],
    "investment": [
      "investment1",
      "investment2",
      "investment3"
    ],
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

