
# Connected Application

Describes the connected application for a particular end user.

*This model accepts additional fields of type Any.*

## Structure

`ConnectedApplication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `application_id` | `str` | Required | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. |
| `name` | `str` | Required | The name of the application |
| `logo` | `str` | Required | A URL that links to the application logo image (will be deprecated in the future, please use logo_url). |
| `logo_url` | `str` | Required | A URL that links to the application logo image. |
| `application_url` | `str` | Required | The URL for the application's website |
| `reason_for_access` | `str` | Required | A string provided by the connected app stating why they use their respective enabled products. |
| `created_at` | `date` | Required | The date this application was linked in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. |
| `product_data_types` | [`List[ProductDataType]`](../../doc/models/product-data-type.md) | Required | (Deprecated) A list of enums representing the data collected and products enabled for this connected application. |
| `scopes` | [`ScopesNullable`](../../doc/models/scopes-nullable.md) | Optional | - |
| `requested_scopes` | [`RequestedScopes`](../../doc/models/requested-scopes.md) | Optional | Scope of required and optional account features or content from a ConnectedApplication. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "application_id": "application_id8",
  "name": "name2",
  "logo": "logo8",
  "logo_url": "logo_url2",
  "application_url": "application_url2",
  "reason_for_access": "reason_for_access0",
  "created_at": "2020-01-01",
  "product_data_types": [
    "ACCOUNT_BALANCE"
  ],
  "scopes": {
    "product_access": {
      "statements": false,
      "identity": false,
      "auth": false,
      "transactions": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "accounts": [
      {
        "unique_id": "unique_id6",
        "authorized": false,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      {
        "unique_id": "unique_id6",
        "authorized": false,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "new_accounts": false,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "requested_scopes": {
    "required_product_access": {
      "statements": false,
      "identity": false,
      "auth": false,
      "transactions": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "optional_product_access": {
      "statements": false,
      "identity": false,
      "auth": false,
      "transactions": false,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
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
    "account_selection_cardinality": "MULTI_SELECT",
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

