from openpyxl import Workbook
from faker import Faker 
import random
from datetime import datetime

now = datetime.now()
now_string = now.strftime("%Y%m%d_%H%M%S")
faker_client = Faker("zh_CN")

wb = Workbook()
ws = wb.active
ws.append(["商品ID", "报名结果", "失败原因或风险提示"])

for i in range(2000):
    ws.append(
        [str(random.randint(10**11, 10**12-1)), random.choice(["报名成功", "报名失败"]), 
        # faker_client.text(300),
        ] + ["文字"] * 160
    )
import io 
with io.BytesIO() as file:
    wb.save(file)
    size = file.tell()
    print(size)

wb.save(f"out/test_file_size.xlsx")