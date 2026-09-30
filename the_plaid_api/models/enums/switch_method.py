from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SwitchMethod(str, Enum):
    """The method used to make the deposit switch.

    - ``instant`` – User instantly switched their direct deposit to a new or existing bank account by connecting their
        payroll or employer account.

    - ``mail`` – User requested that Plaid contact their employer by mail to make the direct deposit switch.

    - ``pdf`` – User generated a PDF or email to be sent to their employer with the information necessary to make the
        deposit switch.'"""

    INSTANT = "instant"
    MAIL = "mail"
    PDF = "pdf"

    __str__ = str.__str__


SwitchMethodOrStr: TypeAlias = Annotated[SwitchMethod | str, open_enum_validator(SwitchMethod)]
