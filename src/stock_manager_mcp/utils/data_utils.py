import os
import pandas as pd
import logging

from stock_manager_mcp.constants.column_config import COLUMNS

logger = logging.getLogger(__name__)

def fix_csv(input_file: str, output_file: str):
    """
    Fixes a CSV file where lines might have been split incorrectly.
    """
    if not os.path.exists(input_file):
        logger.info(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        
        header = f_in.readline()
        if not header:
            logger.info("File is empty.")
            return
        
        f_out.write(header)
        
        buffer = ""
        for line in f_in:
            stripped_line = line.rstrip('\n\r')
            
            if not stripped_line.endswith('"'):
                buffer += " " + stripped_line
            else:
                if buffer:
                    full_line = buffer.lstrip() + " " + stripped_line
                    f_out.write(full_line + '\n')
                    buffer = ""
                else:
                    f_out.write(line)
    
    logger.info(f"Fixed CSV written to {output_file}")
    
def clean_numeric_column(df, column_name):
    """
    Cleans a numeric column by removing commas, dollar signs, and handling parentheses for negative numbers.
    """
    # Remove dollar signs and commas
    df[column_name] = df[column_name].astype(str).str.replace(',', '', regex=False).str.replace('$', '', regex=False)
    
    # Handle parentheses for negative numbers
    df[column_name] = df[column_name].str.replace(r'\((.*?)\)', r'-\1', regex=True)
    
    # Convert to numeric
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    return df

def load_fixed_csv(data_path: str, ):

    output_path = data_path.replace('.csv', '_fixed.csv')
    fix_csv(data_path, output_path)
    df = pd.read_csv(output_path, on_bad_lines='warn')
    
    qty_col = COLUMNS.quantity.name
    df = clean_numeric_column(df, qty_col)
    
    return df
