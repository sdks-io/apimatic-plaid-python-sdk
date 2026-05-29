
# Item Application List Response

Describes the connected application for a particular end user.

*This model accepts additional fields of type Any.*

## Structure

`ItemApplicationListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `applications` | [`List[ConnectedApplication]`](../../doc/models/connected-application.md) | Required | A list of connected applications. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "applications": [
    {
      "application_id": "application_id6",
      "name": "name8",
      "logo": "logo6",
      "logo_url": "logo_url2",
      "application_url": "application_url2",
      "reason_for_access": "reason_for_access6",
      "created_at": "2020-01-01",
      "product_data_types": [
        "ACCOUNT_TRANSACTIONS",
        "ACCOUNT_BALANCE",
        "ACCOUNT_USER_INFO"
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
  ],
  "request_id": "request_id4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

