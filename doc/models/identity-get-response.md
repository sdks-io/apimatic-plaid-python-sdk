
# Identity Get Response

IdentityGetResponse defines the response schema for `/identity/get`

*This model accepts additional fields of type Any.*

## Structure

`IdentityGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | [`List[AccountIdentity]`](../../doc/models/account-identity.md) | Required | The accounts for which Identity data has been requested |
| `item` | [`Item`](../../doc/models/item.md) | Required | Metadata about the Item. |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accounts": [
    {
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
      "type": "depository",
      "subtype": "consumer",
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
      "verification_status": "automatically_verified",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "item": {
    "item_id": "item_id2",
    "institution_id": "institution_id0",
    "webhook": "webhook0",
    "error": {
      "error_type": "RECAPTCHA_ERROR",
      "error_code": "error_code6",
      "error_message": "error_message6",
      "display_message": "display_message8",
      "request_id": "request_id4",
      "causes": [
        {
          "key1": "val1",
          "key2": "val2"
        },
        {
          "key1": "val1",
          "key2": "val2"
        },
        {
          "key1": "val1",
          "key2": "val2"
        }
      ],
      "status": 217.06,
      "documentation_url": "documentation_url6",
      "suggested_action": "suggested_action0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "available_products": [
      "transfer",
      "assets"
    ],
    "billed_products": [
      "deposit_switch",
      "standing_orders"
    ],
    "consent_expiration_time": "2016-03-13T12:52:32.123Z",
    "update_type": "background",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "request_id": "request_id2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

