
# Earnings

An object representing both a breakdown of earnings on a paystub and the total earnings.

*This model accepts additional fields of type Any.*

## Structure

`Earnings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subtotals` | [`List[EarningsTotal]`](../../doc/models/earnings-total.md) | Optional | - |
| `totals` | [`List[EarningsTotal]`](../../doc/models/earnings-total.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
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
    },
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
    },
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
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

