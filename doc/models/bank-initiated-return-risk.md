
# Bank Initiated Return Risk

The object contains a risk score and a risk tier that evaluate the transaction return risk because an account is overdrawn or because an ineligible account is used. Common return codes in this category include: "R01", "R02", "R03", "R04", "R06", “R08”,  "R09", "R13", "R16", "R17", "R20", "R23". These returns have a turnaround time of 2 banking days.

*This model accepts additional fields of type Any.*

## Structure

`BankInitiatedReturnRisk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `score` | `int` | Required | A score from 0-99 that indicates the transaction return risk: a higher risk score suggests a higher return likelihood.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `risk_tier` | `int` | Required | In the `bank_initiated_return_risk` object, there are eight risk tiers corresponding to the scores:<br>1: Predicted bank-initiated return incidence rate between 0.0% - 0.5%<br>2: Predicted bank-initiated return incidence rate between 0.5% - 1.5%<br>3: Predicted bank-initiated return incidence rate between 1.5% - 3%<br>4: Predicted bank-initiated return incidence rate between 3% - 5%<br>5: Predicted bank-initiated return incidence rate between 5% - 10%<br>6: Predicted bank-initiated return incidence rate between 10% - 15%<br>7: Predicted bank-initiated return incidence rate between 15% and 50%<br>8: Predicted bank-initiated return incidence rate greater than 50%<br><br>**Constraints**: `>= 1`, `<= 8` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "score": 100,
  "risk_tier": 8,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

