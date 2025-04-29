## 14.4 - 27.4

In the first few weeks, we've found a bunch of articles about threats related to data leakage that MCP tools are now facing, especially those based on LangChain, as well as the mechanism of corresponding defenses. Through these materials, we found that now the security tools are more focused on the interaction between LLM and MCP tools.

Thus, we were thinking about designing a label system for both data and entities (LLM, tools, the user, etc.) to restrict how MCP tools act on data. That is, even if LLM or untrusted tools have been poisoned, they can't leak or change sensitive data.

Our system aims to guarantee both confidentiality and integrity for the user's data. That is, first, the MCP tools cannot leak the user's data (whether it's intended or not), and also, malicious tools cannot have the chance to change the user's data.

We also discussed how to define the non-interference of information flow in LLM, and we came up with two ideas. The first one is the same as the classic non-interference definition, that is, whenever the secret data in LLM's data source has been changed, its answer to the same question of the user (with lower authority) should always be the same. But we think it's hard to define "the same answer" for LLMs, as the words they generate are always statistical but not deterministic. The other definition we came up with is simpler: that no matter what the user has asked, the LLM's answer doesn't contain any secret data. This definition is easier for implementation. For example, our monitor can reject LLM returning an answer with some secret data with a higher security label than the authority the user has, as the figure shows:
