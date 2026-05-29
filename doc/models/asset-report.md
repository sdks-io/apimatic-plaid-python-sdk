
# Asset Report

An object representing an Asset Report

*This model accepts additional fields of type Any.*

## Structure

`AssetReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_report_id` | `str` | Required | A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive. |
| `client_report_id` | `str` | Required | An identifier you determine and submit for the Asset Report. |
| `date_generated` | `datetime` | Required | The date and time when the Asset Report was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. "2018-04-12T03:32:11Z"). |
| `days_requested` | `float` | Required | The duration of transaction history you requested |
| `user` | [`AssetReportUser`](../../doc/models/asset-report-user.md) | Required | The user object allows you to provide additional information about the user to be appended to the Asset Report. All fields are optional. The `first_name`, `last_name`, and `ssn` fields are required if you would like the Report to be eligible for Fannie Mae’s Day 1 Certainty™ program. |
| `items` | [`List[AssetReportItem]`](../../doc/models/asset-report-item.md) | Required | Data returned by Plaid about each of the Items included in the Asset Report. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "asset_report_id": "asset_report_id8",
  "client_report_id": "client_report_id2",
  "date_generated": "2016-03-13T12:52:32.123Z",
  "days_requested": 66.56,
  "user": {
    "client_user_id": "client_user_id4",
    "first_name": "first_name0",
    "middle_name": "middle_name0",
    "last_name": "last_name8",
    "ssn": "ssn6",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "items": [
    {
      "item_id": "item_id2",
      "institution_name": "institution_name4",
      "institution_id": "institution_id6",
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
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

