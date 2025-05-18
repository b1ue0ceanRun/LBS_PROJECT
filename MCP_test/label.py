import csv
from enum import Enum
from typing import Tuple, List

# === 标签定义 ===
class Integrity(Enum):
    TRUSTED = "Trusted"
    UNTRUSTED = "Untrusted"

class Confidentiality(Enum):
    PUBLIC = "Public"
    PRIVATE = "Private"

Label = Tuple[Integrity, Confidentiality]

class Region:
    def __init__(self, content: str, label: Label, id: int):
        self.content = content
        self.label = label
        self.id = id

    def __repr__(self):
        return f"Region(id={self.id}, label={self.label}, content={self.content!r})"

# === 数据写入（你的已有部分） ===
csv_file_name = 'data1.csv'
table = [
    {"id": 1, "data": "So close, such beautiful"},
    {"id": 2, "data": "flag{hackedbyb1ue0cean}"},
]

with open(csv_file_name, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['id', 'data'])
    writer.writeheader()
    for record in table:
        writer.writerow(record)

# === 读取并打标签 ===
def load_and_label_csv(path: str) -> List[Region]:
    regions = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            content = row["data"]
            row_id = int(row["id"])
            if "flag" in content:
                label = (Integrity.TRUSTED, Confidentiality.PRIVATE)
            else:
                label = (Integrity.TRUSTED, Confidentiality.PUBLIC)
            regions.append(Region(content=content, label=label, id=row_id))
    return regions

# === 打印已打标签的数据 ===
if __name__ == "__main__":
    labeled_regions = load_and_label_csv(csv_file_name)
    for r in labeled_regions:
        print(r)
