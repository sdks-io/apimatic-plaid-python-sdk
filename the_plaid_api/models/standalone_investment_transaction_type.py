from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .buy_type import BuyType, BuyTypeDict
from .cash_type import CashType, CashTypeDict
from .fee_type import FeeType, FeeTypeDict
from .sell_type import SellType, SellTypeDict
from .transfer_type import TransferType, TransferTypeDict


class StandaloneInvestmentTransactionType(SdkBaseModel):
    """Valid values for investment transaction types and subtypes. Note that transactions representing inflow of cash
    will appear as negative amounts, outflow of cash will appear as positive amounts."""

    buy: BuyType
    """Buying an investment"""

    sell: SellType
    """Selling an investment"""

    cancel: str
    """A cancellation of a pending transaction"""

    cash: CashType
    """Activity that modifies a cash position"""

    fee: FeeType
    """Fees on the account, e.g. commission, bookkeeping, options-related."""

    transfer: TransferType
    """Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer"""


class StandaloneInvestmentTransactionTypeDict(TypedDict):
    buy: BuyTypeDict
    sell: SellTypeDict
    cancel: str
    cash: CashTypeDict
    fee: FeeTypeDict
    transfer: TransferTypeDict
