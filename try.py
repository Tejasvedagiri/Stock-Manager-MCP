import pandas as pd
from stock_manager_mcp.constants.column_config import COLUMNS
from stock_manager_mcp.utils.data_utils import load_fixed_csv, clean_numeric_column

def calculate_investments(data_path):
    """
    Calculates total invested, total withdrawn, and current invested amounts
    by analyzing all transaction codes.
    """
    df = load_fixed_csv(data_path)
    
    if df is None or df.empty:
        return 0, 0, 0
    
    # Clean numeric columns
    df = clean_numeric_column(df, COLUMNS.amount.name)
    
    # Print sum of amounts for each transaction code for analysis
    code_sums = df.groupby(COLUMNS.trans_code.name)[COLUMNS.amount.name].sum()
    print("--- Transaction Code Sums ---")
    print(code_sums)
    print("----------------------------")
    
    # Filter for ACH transactions
    ach_df = df[df[COLUMNS.trans_code.name] == 'ACH']
    
    # Let's print all ACH transactions to see them
    print("--- ACH Transactions ---")
    print(ach_df[[COLUMNS.trans_code.name, COLUMNS.amount.name]])
    print("------------------------")
    
    # Filter for Buy transactions
    buy_df = df[df[COLUMNS.trans_code.name] == 'Buy']
    print("--- Buy Transactions ---")
    print(buy_df[[COLUMNS.trans_code.name, COLUMNS.amount.name]])
    print("------------------------")
    
    # Filter for Sell transactions
    sell_df = df[df[COLUMNS.trans_code.name] == 'Sell']
    print("--- Sell Transactions ---")
    print(sell_df[[COLUMNS.trans_code.name, COLUMNS.amount.name]])
    print("------------------------")

    # Find all transactions with parentheses in amount (before cleaning)
    # Since load_fixed_csv cleans the column, we need to do it differently
    # Let's just use the raw file to search for '('
    
    # Total Invested: Sum of positive ACH amounts
    total_invested = ach_df[ach_df[COLUMNS.amount.name] > 0][COLUMNS.amount.name].sum()
    
    # Total Withdrawn: Sum of negative ACH amounts
    total_withdrawn = abs(ach_df[ach_df[COLUMNS.amount.name] < 0][COLUMNS.amount.name].sum())
    
    # Current Invested: The difference
    current_invested = total_invested - total_withdrawn
    
    return total_invested, total_withdrawn, current_invested

if __name__ == "__main__":
    # Using the data_fixed.csv as the source
    DATA_PATH = "data/data_fixed.csv"
    invested, withdrawn, current = calculate_investments(DATA_PATH)
    print(f"Total Invested Amt: ${invested:,.2f}")
    print(f"Total Withdrawed Amt: ${withdrawn:,.2f}")
    print(f"Current Invested Amt: ${current:,.2f}")