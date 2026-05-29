
# Income Verification Paystubs Get Response

IncomeVerificationPaystubsGetResponse defines the response schema for `/income/verification/paystubs/get`.

*This model accepts additional fields of type Any.*

## Structure

`IncomeVerificationPaystubsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paystubs` | [`List[Paystub]`](../../doc/models/paystub.md) | Required | - |
| `error` | [`Error`](../../doc/models/error.md) | Optional | We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues.  Error fields will be `null` if no error has occurred. |
| `document_metadata` | [`List[DocumentMetadata]`](../../doc/models/document-metadata.md) | Optional | - |
| `request_id` | `str` | Required | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "paystubs": [
    {
      "employer": {
        "name": "name2",
        "address": {
          "city": "city6",
          "street": "street6",
          "line1": "line18",
          "line2": "line20",
          "postal_code": "postal_code8",
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
      "employee": {
        "name": "name8",
        "address": {
          "city": "city6",
          "street": "street6",
          "line1": "line18",
          "line2": "line20",
          "postal_code": "postal_code8",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "marital_status": "marital_status6",
        "taxpayer_id": {
          "id_type": "id_type8",
          "last_4_digits": "last_4_digits6",
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
      "pay_period_details": {
        "start_date": "2016-03-13",
        "end_date": "2016-03-13",
        "pay_day": "2016-03-13",
        "gross_earnings": 59.04,
        "check_amount": 134.86,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "income_breakdown": [
        {
          "type": "bonus",
          "rate": 29.56,
          "hours": 6.52,
          "total": 118.76,
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "ytd_earnings": {
        "gross_earnings": 4.84,
        "net_earnings": 206.94,
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "deductions": {
        "subtotals": [
          {
            "canonical_description": "OVERTIME",
            "description": "description8",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "ytd_pay": {
              "amount": 28.98,
              "currency": "currency0",
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
        "totals": [
          {
            "canonical_description": "BONUS",
            "description": "description8",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "ytd_pay": {
              "amount": 28.98,
              "currency": "currency0",
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
          {
            "canonical_description": "BONUS",
            "description": "description8",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "ytd_pay": {
              "amount": 28.98,
              "currency": "currency0",
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
          {
            "canonical_description": "BONUS",
            "description": "description8",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "ytd_pay": {
              "amount": 28.98,
              "currency": "currency0",
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
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "doc_id": "doc_id2",
      "earnings": {
        "subtotals": [
          {
            "canonical_description": "OVERTIME",
            "description": "description8",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "ytd_pay": {
              "amount": 28.98,
              "currency": "currency0",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "current_hours": "current_hours0",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "totals": [
          {
            "canonical_description": "BONUS",
            "description": "description8",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "ytd_pay": {
              "amount": 28.98,
              "currency": "currency0",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "current_hours": "current_hours4",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          {
            "canonical_description": "BONUS",
            "description": "description8",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "ytd_pay": {
              "amount": 28.98,
              "currency": "currency0",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "current_hours": "current_hours4",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          {
            "canonical_description": "BONUS",
            "description": "description8",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "ytd_pay": {
              "amount": 28.98,
              "currency": "currency0",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "current_hours": "current_hours4",
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
      "employment_details": {
        "annual_salary": {
          "amount": 106.22,
          "currency": "currency0",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "hire_date": "2016-03-13",
        "exampleAdditionalProperty": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "net_pay": {
        "distribution_details": [
          {
            "account_number": "account_number0",
            "bank_account_type": "bank_account_type8",
            "bank_name": "bank_name4",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "description": "description0",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          {
            "account_number": "account_number0",
            "bank_account_type": "bank_account_type8",
            "bank_name": "bank_name4",
            "current_pay": {
              "amount": 45.16,
              "currency": "currency4",
              "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2"
              }
            },
            "description": "description0",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          }
        ],
        "total": {
          "canonical_description": "NOT_FOUND",
          "description": "description0",
          "current_pay": {
            "amount": 45.16,
            "currency": "currency4",
            "exampleAdditionalProperty": {
              "key1": "val1",
              "key2": "val2"
            }
          },
          "ytd_pay": {
            "amount": 28.98,
            "currency": "currency0",
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
      },
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "request_id": "request_id6",
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
  "document_metadata": [
    {
      "name": "name2",
      "status": "status6",
      "doc_id": "doc_id6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "name": "name2",
      "status": "status6",
      "doc_id": "doc_id6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "name": "name2",
      "status": "status6",
      "doc_id": "doc_id6",
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

