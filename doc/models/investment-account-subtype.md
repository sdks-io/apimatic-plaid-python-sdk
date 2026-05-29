
# Investment Account Subtype

An investment account. Supported products for `investment` accounts are: Balance and Investments.

*This model accepts additional fields of type Any.*

## Structure

`InvestmentAccountSubtype`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `m_529_a` | `str` | Required | Tax-advantaged college savings and prepaid tuition 529 plans (US) |
| `m_401_a` | `str` | Required | Employer-sponsored money-purchase 401(a) retirement plan (US) |
| `m_401_k` | `str` | Required | Standard 401(k) retirement account (US) |
| `m_403_b` | `str` | Required | 403(b) retirement savings account for non-profits and schools (US) |
| `m_457_b` | `str` | Required | Tax-advantaged deferred-compensation 457(b) retirement plan for governments and non-profits (US) |
| `brokerage` | `str` | Required | Standard brokerage account |
| `cash_isa` | `str` | Required | Individual Savings Account (ISA) that pays interest tax-free (UK) |
| `education_savings_account` | `str` | Required | Tax-advantaged Coverdell Education Savings Account (ESA) (US) |
| `fixed_annuity` | `str` | Required | Fixed annuity |
| `gic` | `str` | Required | Guaranteed Investment Certificate (Canada) |
| `health_reimbursement_arrangement` | `str` | Required | Tax-advantaged Health Reimbursement Arrangement (HRA) benefit plan (US) |
| `hsa` | `str` | Required | Non-cash tax-advantaged medical Health Savings Account (HSA) (US) |
| `ira` | `str` | Required | Traditional Invididual Retirement Account (IRA) (US) |
| `isa` | `str` | Required | Non-cash Individual Savings Account (ISA) (UK) |
| `keogh` | `str` | Required | Keogh self-employed retirement plan (US) |
| `lif` | `str` | Required | Life Income Fund (LIF) retirement account (Canada) |
| `life_insurance` | `str` | Required | Life insurance account |
| `lira` | `str` | Required | Locked-in Retirement Account (LIRA) (Canada) |
| `lrif` | `str` | Required | Locked-in Retirement Income Fund (LRIF) (Canada) |
| `lrsp` | `str` | Required | Locked-in Retirement Savings Plan (Canada) |
| `mutual_fund` | `str` | Required | Mutual fund account |
| `non_taxable_brokerage_account` | `str` | Required | A non-taxable brokerage account that is not covered by a more specific subtype |
| `other` | `str` | Required | An account whose type could not be determined |
| `other_annuity` | `str` | Required | An annuity account not covered by other subtypes |
| `other_insurance` | `str` | Required | An insurance account not covered by other subtypes |
| `pension` | `str` | Required | Standard pension account |
| `prif` | `str` | Required | Prescribed Registered Retirement Income Fund (Canada) |
| `profit_sharing_plan` | `str` | Required | Plan that gives employees share of company profits |
| `qshr` | `str` | Required | Qualifying share account |
| `rdsp` | `str` | Required | Registered Disability Savings Plan (RSDP) (Canada) |
| `resp` | `str` | Required | Registered Education Savings Plan (Canada) |
| `retirement` | `str` | Required | Retirement account not covered by other subtypes |
| `rlif` | `str` | Required | Restricted Life Income Fund (RLIF) (Canada) |
| `roth` | `str` | Required | Roth IRA (US) |
| `roth_401_k` | `str` | Required | Employer-sponsored Roth 401(k) plan (US) |
| `rrif` | `str` | Required | Registered Retirement Income Fund (RRIF) (Canada) |
| `rrsp` | `str` | Required | Registered Retirement Savings Plan (Canadian, similar to US 401(k)) |
| `sarsep` | `str` | Required | Salary Reduction Simplified Employee Pension Plan (SARSEP), discontinued retirement plan (US) |
| `sep_ira` | `str` | Required | Simplified Employee Pension IRA (SEP IRA), retirement plan for small businesses and self-employed (US) |
| `simple_ira` | `str` | Required | Savings Incentive Match Plan for Employees IRA, retirement plan for small businesses (US) |
| `sipp` | `str` | Required | Self-Invested Personal Pension (SIPP) (UK) |
| `stock_plan` | `str` | Required | Standard stock plan account |
| `tfsa` | `str` | Required | Tax-Free Savings Account (TFSA), a retirement plan similar to a Roth IRA (Canada) |
| `trust` | `str` | Required | Account representing funds or assets held by a trustee for the benefit of a beneficiary. Includes both revocable and irrevocable trusts. |
| `ugma` | `str` | Required | 'Uniform Gift to Minors Act' (brokerage account for minors, US) |
| `utma` | `str` | Required | 'Uniform Transfers to Minors Act' (brokerage account for minors, US) |
| `variable_annuity` | `str` | Optional | Tax-deferred capital accumulation annuity contract |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "529a": "529a8",
  "401a": "401a8",
  "401k": "401k4",
  "403b": "403b6",
  "457b": "457b0",
  "brokerage": "brokerage6",
  "cash isa": "cash isa2",
  "education savings account": "education savings account6",
  "fixed annuity": "fixed annuity2",
  "gic": "gic4",
  "health reimbursement arrangement": "health reimbursement arrangement2",
  "hsa": "hsa6",
  "ira": "ira0",
  "isa": "isa8",
  "keogh": "keogh4",
  "lif": "lif4",
  "life insurance": "life insurance2",
  "lira": "lira8",
  "lrif": "lrif4",
  "lrsp": "lrsp8",
  "mutual fund": "mutual fund0",
  "non-taxable brokerage account": "non-taxable brokerage account2",
  "other": "other6",
  "other annuity": "other annuity6",
  "other insurance": "other insurance8",
  "pension": "pension8",
  "prif": "prif8",
  "profit sharing plan": "profit sharing plan8",
  "qshr": "qshr6",
  "rdsp": "rdsp0",
  "resp": "resp2",
  "retirement": "retirement0",
  "rlif": "rlif4",
  "roth": "roth8",
  "roth 401k": "roth 401k2",
  "rrif": "rrif4",
  "rrsp": "rrsp2",
  "sarsep": "sarsep0",
  "sep ira": "sep ira6",
  "simple ira": "simple ira8",
  "sipp": "sipp2",
  "stock plan": "stock plan8",
  "tfsa": "tfsa8",
  "trust": "trust8",
  "ugma": "ugma4",
  "utma": "utma2",
  "variable annuity": "variable annuity2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

