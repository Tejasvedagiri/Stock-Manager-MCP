from stock_manager_mcp.server import stock_manager
from stock_manager_mcp.models.holdings_response import HoldingsResponse

def test():
    print("Testing calculate_holding tool...")
    try:
        result = stock_manager.calculate_holding()
        print(f"Result: {result}")
        print(f"Result Type: {type(result)}")
        # Verify it's a HoldingsResponse object
        if isinstance(result, HoldingsResponse):
            print("Verification Successful: Result is a HoldingsResponse instance.")
        else:
            print(f"Verification Failed: Result is {type(result)} instead of HoldingsResponse.")
    except Exception as e:
        print(f"Error during test: {e}")

if __name__ == "__main__":
    test()