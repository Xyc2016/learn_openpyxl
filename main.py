import io
from openpyxl import Workbook
from openpyxl.styles.colors import Color
from openpyxl.styles.fills import PatternFill
from openpyxl.worksheet._write_only import WriteOnlyWorksheet, WriteOnlyCell
from openpyxl.styles import Font
from zipfile import ZipFile
import os
import psutil
from datetime import datetime
from faker import Faker
wb = Workbook(write_only=True)
from random import random, randint
faker = Faker()
import linecache
import os
import tracemalloc


# ... run your application ...
ws = wb.create_sheet()

process = psutil.Process(os.getpid())

def print_rss():
    print(process.memory_info().rss / 1024 /1024, "MB")
def random_chinese():
	 val = randint(0x4e00, 0x9fbf)
	 return chr(val)

ws.column_dimensions["B"].width = 60

print_rss()
for row_index in range(100):

    values = []
    values.extend(random() for _ in range(10))
    values.extend( "".join(random_chinese() for i in range(10)) for _ in range(1) )
    cell = WriteOnlyCell(ws, value="hello world")
    cell.fill = PatternFill(fgColor=Color("000000FF"), patternType='solid')
    ws.append(values+[cell])

file = io.BytesIO()
print_rss()
wb.save(file)
print_rss()
file.seek(0)
with open("a.xlsx", "wb") as file1:
    file1.write(file.read())
