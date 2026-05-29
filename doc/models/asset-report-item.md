
# Asset Report Item

A representation of an Item within an Asset Report.

*This model accepts additional fields of type Any.*

## Structure

`AssetReportItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_id` | `str` | Required | The `item_id` of the Item associated with this webhook, warning, or error |
| `institution_name` | `str` | Required | The full financial institution name associated with the Item. |
| `institution_id` | `str` | Required | The id of the financial institution associated with the Item. |
| `date_last_updated` | `datetime` | Required | The date and time when this Item’s data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. |
| `accounts` | [`List[AccountAssets]`](../../doc/models/account-assets.md) | Required | Data about each of the accounts open on the Item. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "item_id": "item_id4",
  "institution_name": "institution_name2",
  "institution_id": "institution_id4",
  "date_last_updated": "2016-03-13T12:52:32.123Z",
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
      "days_available": 57.96,
      "transactions": [
        {
          "transaction_type": "digital",
          "pending_transaction_id": "pending_transaction_id2",
          "category_id": "category_id0",
          "category": [
            "category0",
            "category1",
            "category2"
          ],
          "location": {
            "address": "address0",
            "city": "city6",
            "region": "region0",
            "postal_code": "postal_code6",
            "country": "country8",
            "lat": 205.22,
            "lon": 217.68,
            "store_number": "store_number0",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          "original_description": "original_description6",
          "account_id": "account_id0",
          "amount": 157.0,
          "iso_currency_code": "iso_currency_code8",
          "unofficial_currency_code": "unofficial_currency_code0",
          "date": "2016-03-13",
          "pending": false,
          "transaction_id": "transaction_id6",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
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
      "historical_balances": [
        {
          "date": "2016-03-13",
          "current": 192.42,
          "iso_currency_code": "iso_currency_code2",
          "unofficial_currency_code": "unofficial_currency_code6",
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
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

