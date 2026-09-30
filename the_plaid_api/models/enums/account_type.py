from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType(str, Enum):
    """``investment:`` Investment account

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``brokerage``: An investment account. Used for ``/assets/`` endpoints only; other endpoints use ``investment``.

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    INVESTMENT = "investment"
    CREDIT = "credit"
    DEPOSITORY = "depository"
    LOAN = "loan"
    BROKERAGE = "brokerage"
    OTHER = "other"

    __str__ = str.__str__


AccountTypeOrStr: TypeAlias = Annotated[AccountType | str, open_enum_validator(AccountType)]
