
# Customer Initiated Return Risk

The object contains a risk score and a risk tier that evaluate the transaction return risk of an unauthorized debit. Common return codes in this category include: “R05”, "R07", "R10", "R11", "R29". These returns typically have a return time frame of up to 60 calendar days. During this period, the customer of financial institutions can dispute a transaction as unauthorized.

*This model accepts additional fields of type Any.*

## Structure

`CustomerInitiatedReturnRisk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `score` | `int` | Required | A score from 0-99 that indicates the transaction return risk: a higher risk score suggests a higher return likelihood.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `risk_tier` | `int` | Required | A tier corresponding to the projected likelihood that the transaction, if initiated, will be subject to a return.<br><br>In the `customer_initiated_return_risk` object, there are five risk tiers corresponding to the scores:<br>1: Predicted customer-initiated return incidence rate between 0.00% - 0.02%<br>2: Predicted customer-initiated return incidence rate between 0.02% - 0.05%<br>3: Predicted customer-initiated return incidence rate between 0.05% - 0.1%<br>4: Predicted customer-initiated return incidence rate between 0.1% - 0.5%<br>5: Predicted customer-initiated return incidence rate greater than 0.5%<br><br>**Constraints**: `>= 1`, `<= 5` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "score": 94,
  "risk_tier": 1,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

