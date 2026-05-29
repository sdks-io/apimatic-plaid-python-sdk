
# Processor Identity Get Response

ProcessorIdentityGetResponse defines the response schema for `/processor/identity/get`

*This model accepts additional fields of type Any.*

## Structure

`ProcessorIdentityGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | [`AccountIdentity`](../../doc/models/account-identity.md) | Required | - |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account": {
    "account_id": "account_id2",
    "balances": {
      "available": 142.32,
      "current": 79.74,
      "limit": 30.84,
      "iso_currency_code": "iso_currency_code6",
      "unofficial_currency_code": "unofficial_currency_code2",
      "last_updated_datetime": "2016-03-13T12:52:32.123Z",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "mask": "mask4",
    "name": "name0",
    "official_name": "official_name2",
    "type": "brokerage",
    "subtype": "tfsa",
    "owners": [
      {
        "names": [
          "names6",
          "names7"
        ],
        "phone_numbers": [
          {
            "data": "data0",
            "primary": false,
            "type": "office",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "emails": [
          {
            "data": "data6",
            "primary": false,
            "type": "other",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "addresses": [
          {
            "data": {
              "city": "city0",
              "region": "region6",
              "street": "street0",
              "postal_code": "postal_code2",
              "country": "country4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "primary": false,
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      }
    ],
    "verification_status": "pending_manual_verification",
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

