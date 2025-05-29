from typing import List, Tuple, Any

from mcp.server.fastmcp import FastMCP
import pandas as pd
from tool import parse_label
# Create an MCP server
app = FastMCP("send-email")


# Add an addition tool
@app.tool()
def send_email(content: str) -> str:
    """mock sending email function, print email content."""

    return f"sending {content}!"

@app.tool()
def read_file(file_name: str) -> list[tuple[Any, ...]]:
    """local file reading."""

    df = pd.read_csv(file_name)
    tuples = [tuple(row) for row in df.itertuples(index=False)]

    return tuples

@app.tool()
def read_file_label(file_name: str) -> str:
    """local file reading."""

    df = pd.read_csv(file_name)
    df["label"] = df["label"].apply(parse_label)

    return str(list(zip(df["data"], df["label"])))

if __name__ == "__main__":
    # print(read_file('data/data.csv'))

    print(read_file_label("data/data_label.csv"))
    app.run(transport='stdio')