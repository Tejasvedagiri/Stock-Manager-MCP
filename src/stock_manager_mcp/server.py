from fastmcp import FastMCP
from stock_manager_mcp.tools.stock import Stock
from stock_manager_mcp.models.holdings_response import HoldingsResponse

# Initialize FastMCP server
mcp = FastMCP("Stock Manager MCP")

# Instantiate the Stock manager
stock_manager = Stock(data_path='data/data.csv')

# Register the calculate_holding method as a tool
mcp.add_tool(stock_manager.calculate_holding)

if __name__ == "__main__":
    mcp.run()
