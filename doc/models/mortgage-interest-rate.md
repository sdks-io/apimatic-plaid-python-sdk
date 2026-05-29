
# Mortgage Interest Rate

Object containing metadata about the interest rate for the mortgage.

*This model accepts additional fields of type Any.*

## Structure

`MortgageInterestRate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `percentage` | `float` | Required | Percentage value (interest rate of current mortgage, not APR) of interest payable on a loan. |
| `mtype` | `str` | Required | The type of interest charged (fixed or variable). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "percentage": 151.72,
  "type": "type6",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

