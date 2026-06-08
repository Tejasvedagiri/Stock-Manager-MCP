import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Parameters to launch the server
    # Using uv run to ensure dependencies are installed and the environment is correct
    import os
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "python", "src/stock_manager_mcp/server.py"],
        env=env
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {tools}")

            # Call the get_stock_holdings tool
            result = await session.call_tool("get_stock_holdings", arguments={})
            print(f"Tool result: {result}")

if __name__ == "__main__":
    asyncio.run(main())