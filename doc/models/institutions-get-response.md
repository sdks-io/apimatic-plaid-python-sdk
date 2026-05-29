
# Institutions Get Response

InstitutionsGetResponse defines the response schema for `/institutions/get`

*This model accepts additional fields of type Any.*

## Structure

`InstitutionsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `institutions` | [`List[Institution]`](../../doc/models/institution.md) | Required | A list of Plaid Institution |
| `total` | `int` | Required | The total number of institutions available via this endpoint |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "institutions": [
    {
      "institution_id": "institution_id0",
      "name": "name2",
      "products": [
        "investments",
        "liabilities",
        "payment_initiation"
      ],
      "country_codes": [
        "GB",
        "ES",
        "NL"
      ],
      "url": "url6",
      "primary_color": "primary_color0",
      "logo": "logo8",
      "routing_numbers": [
        "routing_numbers6",
        "routing_numbers7",
        "routing_numbers8"
      ],
      "oauth": false,
      "status": {
        "item_logins": {
          "status": "HEALTHY",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "transactions_updates": {
          "status": "DOWN",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "auth": {
          "status": "DEGRADED",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "balance": {
          "status": "DOWN",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "identity": {
          "status": "DEGRADED",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "investments_updates": {
          "status": "DEGRADED",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "liabilities_updates": {
          "status": "HEALTHY",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "liabilities": {
          "status": "DEGRADED",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "investments": {
          "status": "DOWN",
          "last_status_change": "2016-03-13T12:52:32.123Z",
          "breakdown": {
            "success": 164.84,
            "error_plaid": 201.78,
            "error_institution": 35.5,
            "refresh_interval": "NORMAL",
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
        "health_incidents": [
          {
            "start_date": "2016-03-13T12:52:32.123Z",
            "end_date": "2016-03-13T12:52:32.123Z",
            "title": "title8",
            "incident_updates": [
              {
                "description": "description2",
                "status": "UNKNOWN",
                "updated_date": "2016-03-13T12:52:32.123Z",
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              },
              {
                "description": "description2",
                "status": "UNKNOWN",
                "updated_date": "2016-03-13T12:52:32.123Z",
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              },
              {
                "description": "description2",
                "status": "UNKNOWN",
                "updated_date": "2016-03-13T12:52:32.123Z",
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
          {
            "start_date": "2016-03-13T12:52:32.123Z",
            "end_date": "2016-03-13T12:52:32.123Z",
            "title": "title8",
            "incident_updates": [
              {
                "description": "description2",
                "status": "UNKNOWN",
                "updated_date": "2016-03-13T12:52:32.123Z",
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              },
              {
                "description": "description2",
                "status": "UNKNOWN",
                "updated_date": "2016-03-13T12:52:32.123Z",
                "exampleAdditionalProperty": {
                  "key1": "val1",
                  "key2": "val2"
                }
              },
              {
                "description": "description2",
                "status": "UNKNOWN",
                "updated_date": "2016-03-13T12:52:32.123Z",
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
      "payment_initiation_metadata": {
        "supports_international_payments": false,
        "maximum_payment_amount": {
          "key0": "maximum_payment_amount9",
          "key1": "maximum_payment_amount0",
          "key2": "maximum_payment_amount1"
        },
        "supports_refund_details": false,
        "standing_order_metadata": {
          "supports_standing_order_end_date": false,
          "supports_standing_order_negative_execution_days": false,
          "valid_standing_order_intervals": [
            "WEEKLY",
            "MONTHLY"
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
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "total": 2,
  "request_id": "request_id8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

