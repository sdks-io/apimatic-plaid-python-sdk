
# Institution

Details relating to a specific financial institution

*This model accepts additional fields of type Any.*

## Structure

`Institution`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `institution_id` | `str` | Required | Unique identifier for the institution |
| `name` | `str` | Required | The official name of the institution |
| `products` | [`List[Products]`](../../doc/models/products.md) | Required | A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return `auth` in the product array; institutions that do not list `auth` may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/). |
| `country_codes` | [`List[CountryCode]`](../../doc/models/country-code.md) | Required | A list of the country codes supported by the institution. |
| `url` | `str` | Optional | The URL for the institution's website |
| `primary_color` | `str` | Optional | Hexadecimal representation of the primary color used by the institution |
| `logo` | `str` | Optional | Base64 encoded representation of the institution's logo |
| `routing_numbers` | `List[str]` | Required | A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution. |
| `oauth` | `bool` | Required | Indicates that the institution has an OAuth login flow. This is primarily relevant to institutions with European country codes. |
| `status` | [`InstitutionStatus`](../../doc/models/institution-status.md) | Optional | The status of an institution is determined by the health of its Item logins, Transactions updates, Investments updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate data.<br><br>Institution status is accessible in the Dashboard and via the API using the `/institutions/get_by_id` endpoint with the `include_status` option set to true. Note that institution status is not available in the Sandbox environment. |
| `payment_initiation_metadata` | [`PaymentInitiationMetadata`](../../doc/models/payment-initiation-metadata.md) | Optional | Metadata that captures what specific payment configurations an institution supports when making Payment Initiation requests. |
| `auth_metadata` | [`AuthMetadata`](../../doc/models/auth-metadata.md) | Optional | Metadata that captures information about the Auth features of an institution. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "institution_id": "institution_id0",
  "name": "name2",
  "products": [
    "credit_details",
    "income",
    "income_verification"
  ],
  "country_codes": [
    "IE",
    "CA",
    "US"
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
```

