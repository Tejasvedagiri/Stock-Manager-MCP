import pandas as pd
import logging
from stock_manager_mcp.models.holding import Holding
from stock_manager_mcp.models.holdings_response import HoldingsResponse
from stock_manager_mcp.constants.column_config import COLUMNS
from stock_manager_mcp.constants.transaction_type_config import TRANSACTION_TYPES
from stock_manager_mcp.utils.data_utils import load_fixed_csv, clean_numeric_column
from fastmcp.tools import tool

logger = logging.getLogger(__name__)

class Stock:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.df = load_fixed_csv(self.data_path)

    def _calculate_signed_qty(self, row, tt_map):
        """
        Helper method to calculate signed quantity based on transaction type.
        """
        qty = row[COLUMNS.quantity.name]
        if pd.isna(qty):
            return 0
        
        type_code = str(row[COLUMNS.trans_code.name]).strip().lower()
        info = tt_map.get(type_code)
        if info and info.increases_holdings:
            return qty
        elif info and info.decreases_holdings:
            return -qty
        return 0

    @tool("calculate_holding", description="Calculate total holdings for each stock")
    def calculate_holding(self):
        """
        Calculates total holdings for each stock from the CSV data.
        Returns a HoldingsResponse.
        """
        if self.df is None or self.df.empty:
            return HoldingsResponse(holdings=[])

        try:
            # Create a mapping of lowercase code to TransactionTypeInfo for efficient lookup
            tt_map = {
                val.code.lower(): val 
                for val in vars(TRANSACTION_TYPES).values() 
                if hasattr(val, 'code')
            }

            # Create a signed quantity: positive for Buy, and recovery, negative for Sell
            self.df['SignedQty'] = self.df.apply(
                lambda row: self._calculate_signed_qty(row, tt_map), 
                axis=1
            )

            # Group by symbol and sum
            holdings_df = self.df.groupby(COLUMNS.instrument.name)['SignedQty'].sum().reset_index()
            holdings_df.columns = ['Symbol', 'Total Holdings']

            # Round to 3 decimals
            holdings_df['Total Holdings'] = holdings_df['Total Holdings'].round(3)

            # Filter out rows where Total Holdings is 0 (using a small epsilon for float precision)
            # Use 0.0005 to ensure that anything rounding to 0.000 at 3 decimal places is removed
            holdings_df = holdings_df[holdings_df['Total Holdings'].abs() > 0.0005]

            # Convert to a list of Pydantic models
            holdings_list = [
                Holding(symbol=row['Symbol'], total_holdings=row['Total Holdings'])
                for _, row in holdings_df.iterrows()
            ]

            return HoldingsResponse(holdings=holdings_list)

        except Exception as e:
            # For simplicity in a tool, returning an empty response or error
            # In a real app, we'd handle this more formally
            logger.info(f"Error calculating holdings: {e}")
            return HoldingsResponse(holdings=[])