
# Link Token Get Response

LinkTokenGetResponse defines the response schema for `/link/token/get`

*This model accepts additional fields of type Any.*

## Structure

`LinkTokenGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link_token` | `str` | Required | A `link_token`, which can be supplied to Link in order to initialize it and receive a `public_token`, which can be exchanged for an `access_token`. |
| `created_at` | `datetime` | Required | The creation timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. |
| `expiration` | `datetime` | Required | The expiration timestamp for the `link_token`, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. |
| `metadata` | [`LinkTokenGetMetadataResponse`](../../doc/models/link-token-get-metadata-response.md) | Required | An object specifying the arguments originally provided to the `/link/token/create` call. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "link_token": "link_token0",
  "created_at": "2016-03-13T12:52:32.123Z",
  "expiration": "2016-03-13T12:52:32.123Z",
  "metadata": {
    "initial_products": [
      "transfer",
      "assets"
    ],
    "webhook": "webhook4",
    "country_codes": [
      "GB",
      "ES"
    ],
    "language": "language8",
    "account_filters": {
      "depository": {
        "account_subtypes": [
          "non-taxable brokerage account",
          "other"
        ],
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "credit": {
        "account_subtypes": [
          "ugma",
          "utma",
          "variable annuity"
        ],
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "loan": {
        "account_subtypes": [
          "checking",
          "savings",
          "money market"
        ],
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "investment": {
        "account_subtypes": [
          "consumer",
          "home"
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
    },
    "redirect_uri": "redirect_uri4",
    "client_name": "client_name0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "request_id": "request_id6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

