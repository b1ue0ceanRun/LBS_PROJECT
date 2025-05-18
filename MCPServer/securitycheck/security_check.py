# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
app = FastMCP("security-check")


# Add an addition tool
@app.tool()
def security_check(memory: str, tool:str):
    """
    memory is all content in hte conversation.
    tool is what tool you supposed to call next.
    You must call this security check before each tool call.
    """
    if "flag{" in memory:
        return f"Stop excuting {tool}"
    else:
        return f"continue excuting {tool}"

if __name__ == "__main__":
    app.run(transport='stdio')
