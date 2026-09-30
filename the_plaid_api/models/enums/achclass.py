from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Achclass(str, Enum):
    """Specifies the use case of the transfer. Required for transfers on an ACH network.

    ``"arc"`` - Accounts Receivable Entry

    ``"cbr``" - Cross Border Entry

    ``"ccd"`` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    ``"cie"`` - Customer Initiated Entry

    ``"cor"`` - Automated Notification of Change

    ``"ctx"`` - Corporate Trade Exchange

    ``"iat"`` - International

    ``"mte"`` - Machine Transfer Entry

    ``"pbr"`` - Cross Border Entry

    ``"pop"`` - Point-of-Purchase Entry

    ``"pos"`` - Point-of-Sale Entry

    ``"ppd"`` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer,
    eg. bill payment

    ``"rck"`` - Re-presented Check Entry

    ``"tel"`` - Telephone-Initiated Entry

    ``"web"`` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over
    the Internet"""

    ARC = "arc"
    CBR = "cbr"
    CCD = "ccd"
    CIE = "cie"
    COR = "cor"
    CTX = "ctx"
    IAT = "iat"
    MTE = "mte"
    PBR = "pbr"
    POP = "pop"
    POS = "pos"
    PPD = "ppd"
    RCK = "rck"
    TEL = "tel"
    WEB = "web"

    __str__ = str.__str__


AchclassOrStr: TypeAlias = Annotated[Achclass | str, open_enum_validator(Achclass)]
