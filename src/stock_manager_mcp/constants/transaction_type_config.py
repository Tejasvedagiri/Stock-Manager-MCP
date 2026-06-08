from dataclasses import dataclass

@dataclass(frozen=True)
class TransactionTypeInfo:
    code: str
    increases_holdings: bool = False
    decreases_holdings: bool = False

@dataclass(frozen=True)
class TransactionTypeConfig:
    buy: TransactionTypeInfo = TransactionTypeInfo(code="Buy", increases_holdings=True)
    ach: TransactionTypeInfo = TransactionTypeInfo(code="ACH", increases_holdings=False)
    nrat: TransactionTypeInfo = TransactionTypeInfo(code="NRAT", increases_holdings=False)
    cdiv: TransactionTypeInfo = TransactionTypeInfo(code="CDIV", increases_holdings=True)
    int_: TransactionTypeInfo = TransactionTypeInfo(code="INT", increases_holdings=False)
    sell: TransactionTypeInfo = TransactionTypeInfo(code="Sell", decreases_holdings=True)
    xent_cc: TransactionTypeInfo = TransactionTypeInfo(code="XENT_CC", increases_holdings=False)
    itrf: TransactionTypeInfo = TransactionTypeInfo(code="ITRF", increases_holdings=False)
    gdbp: TransactionTypeInfo = TransactionTypeInfo(code="GDBP", increases_holdings=False)
    spl: TransactionTypeInfo = TransactionTypeInfo(code="SPL", increases_holdings=True)
    noa: TransactionTypeInfo = TransactionTypeInfo(code="NOA", increases_holdings=False)
    rtp: TransactionTypeInfo = TransactionTypeInfo(code="RTP", increases_holdings=False)
    slip: TransactionTypeInfo = TransactionTypeInfo(code="SLIP", increases_holdings=False)
    rec: TransactionTypeInfo = TransactionTypeInfo(code="REC", increases_holdings=True)

TRANSACTION_TYPES = TransactionTypeConfig()
