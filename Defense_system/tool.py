from typing import Callable, Tuple



def parse_label(label_str: str) -> tuple[str, str]:
    """从字符串格式 <Trusted|Private> 解析为 ('Trusted', 'Private')"""
    label_str = label_str.strip("<>").strip()
    integrity, confidentiality = label_str.split("|")
    return integrity.strip(), confidentiality.strip()


SECURITY_ORDER = {"Trusted": 0, "Untrusted": 1}
CONFIDENTIALITY_ORDER = {"Public": 0, "Private": 1}

def flows_to(source: Tuple[str, str], target: Tuple[str, str]) -> bool:
    """判断 source 标签是否可以安全流向 target 标签。"""
    int_s, conf_s = source
    int_t, conf_t = target
    return (
        SECURITY_ORDER[int_s] <= SECURITY_ORDER[int_t] and
        CONFIDENTIALITY_ORDER[conf_s] <= CONFIDENTIALITY_ORDER[conf_t]
    )

def calculate(data_label: Tuple[str, str], tool_label: Tuple[str, str]) -> bool:
    """
    判断是否允许将数据传递给该工具。

    :param data_label: 数据的安全标签 (integrity, confidentiality)
    :param tool_label: 工具的接收限制标签 (integrity, confidentiality)
    :return: True 表示允许传播，False 表示不允许
    """
    allowed = flows_to(data_label, tool_label)
    if allowed:
        print(f"✅ ALLOW: {data_label} ⊑ {tool_label}")
    else:
        print(f"❌ BLOCK: {data_label} ⊄ {tool_label}")
    return allowed

if __name__ == '__main__':
    data_1 = ("Trusted", "Public")
    data_2 = ("Trusted", "Private")

    tool = ("Trusted", "Public")

    calculate(data_1, tool)  # ✅ 允许
    calculate(data_2, tool)  # ❌ 拒绝
