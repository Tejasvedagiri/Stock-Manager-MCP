from dataclasses import dataclass, field

@dataclass(frozen=True)
class ColumnInfo:
    name: str
    description: str
    alternatives: list[str] = field(default_factory=list)

@dataclass(frozen=True)
class ColumnConfig:
    activity_date: ColumnInfo = ColumnInfo(
        name="Activity Date",
        description="The date the activity occurred",
        alternatives=["Event Date", "Transaction Date"]
    )
    process_date: ColumnInfo = ColumnInfo(
        name="Process Date",
        description="The date the transaction was processed",
        alternatives=["Posting Date", "Process Date"]
    )
    settle_date: ColumnInfo = ColumnInfo(
        name="Settle Date",
        description="The date the transaction settled",
        alternatives=["Settlement Date"]
    )
    instrument: ColumnInfo = ColumnInfo(
        name="Instrument",
        description="The stock symbol or identifier",
        alternatives=["Stock Name", "Ticker", "Symbol"]
    )
    description: ColumnInfo = ColumnInfo(
        name="Description",
        description="Detailed description of the transaction",
        alternatives=["Memo", "Notes"]
    )
    trans_code: ColumnInfo = ColumnInfo(
        name="Trans Code",
        description="The transaction type code",
        alternatives=["Transaction Type", "TransType"]
    )
    quantity: ColumnInfo = ColumnInfo(
        name="Quantity",
        description="The number of shares involved in the transaction",
        alternatives=["Qty", "Units", "Shares"]
    )
    price: ColumnInfo = ColumnInfo(
        name="Price",
        description="The price per share of the instrument",
        alternatives=["Unit Price", "Cost per Share"]
    )
    amount: ColumnInfo = ColumnInfo(
        name="Amount",
        description="The total value of the transaction",
        alternatives=["Total Amount", "Net Amount"]
    )

COLUMNS = ColumnConfig()
