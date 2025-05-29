from mcp.server.fastmcp import FastMCP
import subprocess
import logging
from utils import split_args
from mcp_context import McpContext

logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为 INFO（只记录 INFO 及以上级别的日志）
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 日志输出格式
    datefmt='%Y-%m-%d %H:%M:%S'  # 时间格式
)

log = logging.getLogger("MCP_PROXY")



'''
我这是一个proxy 应该能够去管理很多的工具
能注册到原来的进程外吗
'''

'''
确实是不是可以开子进程来进行监控

先拿到args 再说


今天先做拦截，如果说权限不够，就直接给down掉
那也就是说要拿得到输入才行
1. 先把tools的问题解决了
'''
def hook_tool_call(ctx: McpContext, request: dict) -> tuple[dict, bool]:
    '''
    要把tool call拦截下来？？？再进行转发？？？
    '''
    pass


def stream_and_forward_stdout(mcp_process: subprocess.Popen, ctx: McpContext)->None:
    """Read from the mcp_process stdout, apply guardrails and forward to sys.stdout"""
    pass


def stream_and_forward_stderr():
    pass

def execute(args: list[str] = None):
    """Main function to execute the MCP gateway."""

    mcp_gateway_args, mcp_server_command_args = split_args(args)
    ctx = McpContext(mcp_gateway_args)

    # 我需要一个class 它应该包含label？内容的label tool的label
    # 先去执行一下 看一下执行出来的是个什么东西
    mcp_process = subprocess.Popen(
        mcp_server_command_args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=0,
    )

    # 接下来要去执行subprocess
    # tool 怎么获得， tool的label怎么获得都要考虑一下
    # Start async tasks for stdout and stderr
    stdout_task = stream_and_forward_stdout(mcp_process, ctx)
    stderr_task = stream_and_forward_stderr(mcp_process)

if __name__ == '__main__':
    pass
