
# Numbers

Account and bank identifier number data used to configure the test account. All values are optional.

*This model accepts additional fields of type Any.*

## Structure

`Numbers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `str` | Optional | Will be used for the account number. |
| `ach_routing` | `str` | Optional | Must be a valid ACH routing number. |
| `ach_wire_routing` | `str` | Optional | Must be a valid wire transfer routing number. |
| `eft_institution` | `str` | Optional | EFT institution number. Must be specified alongside `eft_branch`. |
| `eft_branch` | `str` | Optional | EFT branch number. Must be specified alongside `eft_institution`. |
| `international_bic` | `str` | Optional | Bank identifier code (BIC). Must be specified alongside `international_iban`. |
| `international_iban` | `str` | Optional | International bank account number (IBAN). If no account number is specified via `account`, will also be used as the account number by default. Must be specified alongside `international_bic`. |
| `bacs_sort_code` | `str` | Optional | BACS sort code |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "account": "account6",
  "ach_routing": "ach_routing6",
  "ach_wire_routing": "ach_wire_routing6",
  "eft_institution": "eft_institution8",
  "eft_branch": "eft_branch0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

