
# Signal Evaluate Scores

Risk scoring details broken down by risk category.

*This model accepts additional fields of type Any.*

## Structure

`SignalEvaluateScores`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_initiated_return_risk` | [`CustomerInitiatedReturnRisk`](../../doc/models/customer-initiated-return-risk.md) | Optional | The object contains a risk score and a risk tier that evaluate the transaction return risk of an unauthorized debit. Common return codes in this category include: “R05”, "R07", "R10", "R11", "R29". These returns typically have a return time frame of up to 60 calendar days. During this period, the customer of financial institutions can dispute a transaction as unauthorized. |
| `bank_initiated_return_risk` | [`BankInitiatedReturnRisk`](../../doc/models/bank-initiated-return-risk.md) | Optional | The object contains a risk score and a risk tier that evaluate the transaction return risk because an account is overdrawn or because an ineligible account is used. Common return codes in this category include: "R01", "R02", "R03", "R04", "R06", “R08”,  "R09", "R13", "R16", "R17", "R20", "R23". These returns have a turnaround time of 2 banking days. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "customer_initiated_return_risk": {
    "score": 100,
    "risk_tier": 5,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "bank_initiated_return_risk": {
    "score": 100,
    "risk_tier": 8,
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

