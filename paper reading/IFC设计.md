
问题回来了 IFC究竟要如何设计

需要具体对数据执行哪些操作

为什么能拦截xx，xx攻击


信息一直是递减的？
工具如何影响信息？



训练时：可以通过其推理时的输出泄露其训练数据中的敏感信息

考虑一个公司使用其专有代码库为其内部代码补全模型进行训练的场景，而每个员工根据其团队或项目不同，只能访问代码库的不同子集。


在LLM中找到一个替代信息传递的过程



MCP
划分成多个安全域

IFC在ML中的目标是开发一种训练过程、推理过程和模型架构，能够在推理时遵循访问策略，通过保证不受访问控制数据对模型输出的泄露来实现这一目标。我们通过非干扰（NI）的视角来定义这一问题，并将IFC呈现为ML系统需要解决的一个新挑战。

可不可以通过修改PROMPT来实现？？？
PROMPT Engineering
来做一个double check？
但要是输入较多怎么办？？？
能不能自己aware？
System Prompt？






https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents





要看的：https://arxiv.org/pdf/2406.04031
https://arxiv.org/pdf/2411.11496v3
https://arxiv.org/pdf/2412.00473

![[Pasted image 20250413052422.png]]