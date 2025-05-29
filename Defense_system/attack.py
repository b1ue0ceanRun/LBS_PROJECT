'''
先来写一个攻击的流程
'''
from fastmcp import Client
import asyncio
async def main():
    # Connect via stdio to a local script
    async with Client("./server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        response_round_1 = await client.call_tool("read_file", {"file_name": 'data/data.csv'})
        print(f"Round 1: {response_round_1}")

        response_round_2 = await client.call_tool("send_email", {"content": str(response_round_1)})
        print(f"Round 2: {response_round_2}")

asyncio.run(main())