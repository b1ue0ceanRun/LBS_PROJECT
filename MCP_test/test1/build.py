from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo", debug=True, log_level="DEBUG")

# Add an addition tool
@mcp.tool()
def add(a: int,b: int)-> int:
    """Add two numbers"""
    return a+b

@mcp.tool()
def echo_tool(message: str)-> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"

if __name__ =="__main__":
    mcp.run(transport="sse")