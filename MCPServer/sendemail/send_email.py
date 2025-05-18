# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
app = FastMCP("send-email")


# Add an addition tool
@app.tool()
def send_email(content:str) -> int:
    """
    mock sending email function, print email content
    """
    return f"sending{content}"

if __name__ == "__main__":
    app.run(transport='stdio')