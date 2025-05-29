'''
mcp_context should include the label of content and the tool

tool???
How to get the tool?


'''



'''
MCP label
Content label
'''
class McpContext:
    def __init__(self, label):
        self.label = label
        self.tools = [] # 这个每个tool都得给它弄个role