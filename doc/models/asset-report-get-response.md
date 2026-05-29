
# Asset Report Get Response

AssetReportGetResponse defines the response schema for `/asset_report/get`

*This model accepts additional fields of type Any.*

## Structure

`AssetReportGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `report` | [`AssetReport`](../../doc/models/asset-report.md) | Required | An object representing an Asset Report |
| `warnings` | [`List[Warning]`](../../doc/models/warning.md) | Required | If the Asset Report generation was successful but identity information cannot be returned, this array will contain information about the errors causing identity information to be missing |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "report": {
    "asset_report_id": "asset_report_id6",
    "client_report_id": "client_report_id0",
    "date_generated": "2016-03-13T12:52:32.123Z",
    "days_requested": 102.14,
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
  },
  "warnings": [
    {
      "warning_type": "warning_type4",
      "warning_code": "OWNERS_UNAVAILABLE",
      "cause": {
        "item_id": "item_id4",
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
  "request_id": "request_id6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

