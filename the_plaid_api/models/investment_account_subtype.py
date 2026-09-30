from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvestmentAccountSubtype(SdkBaseModel):
    """An investment account. Supported products for ``investment`` accounts are: Balance and Investments."""

    a529: str = Field(alias="529a")
    """Tax-advantaged college savings and prepaid tuition 529 plans (US)"""

    a401: str = Field(alias="401a")
    """Employer-sponsored money-purchase 401(a) retirement plan (US)"""

    k401: str = Field(alias="401k")
    """Standard 401(k) retirement account (US)"""

    b403: str = Field(alias="403b")
    """403(b) retirement savings account for non-profits and schools (US)"""

    b457: str = Field(alias="457b")
    """Tax-advantaged deferred-compensation 457(b) retirement plan for governments and non-profits (US)"""

    brokerage: str
    """Standard brokerage account"""

    cash_isa: str = Field(alias="cash isa")
    """Individual Savings Account (ISA) that pays interest tax-free (UK)"""

    education_savings_account: str = Field(alias="education savings account")
    """Tax-advantaged Coverdell Education Savings Account (ESA) (US)"""

    fixed_annuity: str = Field(alias="fixed annuity")
    """Fixed annuity"""

    gic: str
    """Guaranteed Investment Certificate (Canada)"""

    health_reimbursement_arrangement: str = Field(alias="health reimbursement arrangement")
    """Tax-advantaged Health Reimbursement Arrangement (HRA) benefit plan (US)"""

    hsa: str
    """Non-cash tax-advantaged medical Health Savings Account (HSA) (US)"""

    ira: str
    """Traditional Invididual Retirement Account (IRA) (US)"""

    isa: str
    """Non-cash Individual Savings Account (ISA) (UK)"""

    keogh: str
    """Keogh self-employed retirement plan (US)"""

    lif: str
    """Life Income Fund (LIF) retirement account (Canada)"""

    life_insurance: str = Field(alias="life insurance")
    """Life insurance account"""

    lira: str
    """Locked-in Retirement Account (LIRA) (Canada)"""

    lrif: str
    """Locked-in Retirement Income Fund (LRIF) (Canada)"""

    lrsp: str
    """Locked-in Retirement Savings Plan (Canada)"""

    mutual_fund: str = Field(alias="mutual fund")
    """Mutual fund account"""

    non_taxable_brokerage_account: str = Field(alias="non-taxable brokerage account")
    """A non-taxable brokerage account that is not covered by a more specific subtype"""

    other: str
    """An account whose type could not be determined"""

    other_annuity: str = Field(alias="other annuity")
    """An annuity account not covered by other subtypes"""

    other_insurance: str = Field(alias="other insurance")
    """An insurance account not covered by other subtypes"""

    pension: str
    """Standard pension account"""

    prif: str
    """Prescribed Registered Retirement Income Fund (Canada)"""

    profit_sharing_plan: str = Field(alias="profit sharing plan")
    """Plan that gives employees share of company profits"""

    qshr: str
    """Qualifying share account"""

    rdsp: str
    """Registered Disability Savings Plan (RSDP) (Canada)"""

    resp: str
    """Registered Education Savings Plan (Canada)"""

    retirement: str
    """Retirement account not covered by other subtypes"""

    rlif: str
    """Restricted Life Income Fund (RLIF) (Canada)"""

    roth: str
    """Roth IRA (US)"""

    roth_401k: str = Field(alias="roth 401k")
    """Employer-sponsored Roth 401(k) plan (US)"""

    rrif: str
    """Registered Retirement Income Fund (RRIF) (Canada)"""

    rrsp: str
    """Registered Retirement Savings Plan (Canadian, similar to US 401(k))"""

    sarsep: str
    """Salary Reduction Simplified Employee Pension Plan (SARSEP), discontinued retirement plan (US)"""

    sep_ira: str = Field(alias="sep ira")
    """Simplified Employee Pension IRA (SEP IRA), retirement plan for small businesses and self-employed (US)"""

    simple_ira: str = Field(alias="simple ira")
    """Savings Incentive Match Plan for Employees IRA, retirement plan for small businesses (US)"""

    sipp: str
    """Self-Invested Personal Pension (SIPP) (UK)"""

    stock_plan: str = Field(alias="stock plan")
    """Standard stock plan account"""

    tfsa: str
    """Tax-Free Savings Account (TFSA), a retirement plan similar to a Roth IRA (Canada)"""

    trust: str
    """Account representing funds or assets held by a trustee for the benefit of a beneficiary. Includes both revocable
    and irrevocable trusts."""

    ugma: str
    """'Uniform Gift to Minors Act' (brokerage account for minors, US)"""

    utma: str
    """'Uniform Transfers to Minors Act' (brokerage account for minors, US)"""

    variable_annuity: Optional[str] = Field(default=UNSET, alias="variable annuity")
    """Tax-deferred capital accumulation annuity contract"""


class InvestmentAccountSubtypeDict(TypedDict):
    a529: str
    a401: str
    k401: str
    b403: str
    b457: str
    brokerage: str
    cash_isa: str
    education_savings_account: str
    fixed_annuity: str
    gic: str
    health_reimbursement_arrangement: str
    hsa: str
    ira: str
    isa: str
    keogh: str
    lif: str
    life_insurance: str
    lira: str
    lrif: str
    lrsp: str
    mutual_fund: str
    non_taxable_brokerage_account: str
    other: str
    other_annuity: str
    other_insurance: str
    pension: str
    prif: str
    profit_sharing_plan: str
    qshr: str
    rdsp: str
    resp: str
    retirement: str
    rlif: str
    roth: str
    roth_401k: str
    rrif: str
    rrsp: str
    sarsep: str
    sep_ira: str
    simple_ira: str
    sipp: str
    stock_plan: str
    tfsa: str
    trust: str
    ugma: str
    utma: str
    variable_annuity: NotRequired[str]
