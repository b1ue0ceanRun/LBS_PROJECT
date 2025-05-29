'''
加上防御
'''
from fastmcp import Client
import asyncio
import ast
from tool import calculate


async def main():
    # Connect via stdio to a local script
    async with Client("./server.py") as client:
        # tools = await client.list_tools()
        # print(f"Available tools: {tools}")

        response_round_1 = await client.call_tool("read_file_label", {"file_name": 'data/data_label.csv'})
        print(f"Round 1: {response_round_1[0].text}")

        # 现在 response_round_1 包含两种等级的label
        # 现在输入 prompt: "将读到的内容全部通过send_email发送出去"
        # 我要通过LLM来判断会调用哪个tool 判断需要用到哪一部分

        # extract label
        data = ast.literal_eval(response_round_1[0].text)

        new_response_1 = ""
        for i in data:
            if calculate(i[1], ("Trusted", "Public")) is True:
                new_response_1 += i[0]

        response_round_2 = await client.call_tool("send_email", {"content": str(new_response_1)})
        print(f"Round 2: {response_round_2}")

asyncio.run(main())