import sys
def split_args(args: list[str] = None) -> tuple[list[str], list[str]]:
    """
    Splits CLI arguments into two parts:
    1. Arguments intended for the MCP gateway (everything before `--exec`)
    2. Arguments for the underlying MCP server (everything after `--exec`)

    Parameters:
        args (list[str]): The list of CLI arguments.

    Returns:
        Tuple[list[str], list[str]]: A tuple containing (mcp_gateway_args, mcp_server_command_args)
    """
    if not args:
        print("[ERROR] No arguments provided.")
        sys.exit(1)

    try:
        exec_index = args.index("--exec")
    except ValueError:
        print("[ERROR] '--exec' flag not found in arguments.")
        sys.exit(1)

    mcp_gateway_args = args[:exec_index]
    mcp_server_command_args = args[exec_index + 1 :]

    if not mcp_server_command_args:
        print("[ERROR] No arguments provided after '--exec'.")
        sys.exit(1)

    return mcp_gateway_args, mcp_server_command_args