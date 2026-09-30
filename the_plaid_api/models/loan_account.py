from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoanAccount(SdkBaseModel):
    """A loan type account. Supported products for ``loan`` accounts are: Balance, Liabilities, and Transactions."""

    auto: str
    """Auto loan"""

    business: str
    """Business loan"""

    commercial: str
    """Commercial loan"""

    construction: str
    """Construction loan"""

    consumer: str
    """Consumer loan"""

    home_equity: str = Field(alias="home equity")
    """Home Equity Line of Credit (HELOC)"""

    loan: str
    """General loan"""

    mortgage: str
    """Mortgage loan"""

    overdraft: str
    """Pre-approved overdraft account, usually tied to a checking account"""

    line_of_credit: str = Field(alias="line of credit")
    """Pre-approved line of credit"""

    student: str
    """Student loan"""

    other: str
    """Other loan type or unknown loan type"""


class LoanAccountDict(TypedDict):
    auto: str
    business: str
    commercial: str
    construction: str
    consumer: str
    home_equity: str
    loan: str
    mortgage: str
    overdraft: str
    line_of_credit: str
    student: str
    other: str
