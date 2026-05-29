
# Deductions

An object with the deduction information found on a paystub.

*This model accepts additional fields of type Any.*

## Structure

`Deductions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subtotals` | [`List[Total]`](../../doc/models/total.md) | Optional | - |
| `totals` | [`List[Total]`](../../doc/models/total.md) | Optional | - |
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
}
```

