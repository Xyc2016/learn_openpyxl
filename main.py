import io
from openpyxl import Workbook
from openpyxl.worksheet._write_only import WriteOnlyWorksheet
from zipfile import ZipFile

wb = Workbook(write_only=True)

ws = wb.create_sheet()

ws.append(["abcdefg"])

file = io.BytesIO()

wb.save(file)

file.seek(0)
with open("a.xlsx", "wb") as file1:
    file1.write(file.read())
