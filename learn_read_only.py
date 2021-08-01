from openpyxl.worksheet._read_only import ReadOnlyWorksheet

from openpyxl import load_workbook

a = load_workbook("a.xlsx", read_only=False)
ws : ReadOnlyWorksheet = a.active
print(ws.max_column, ws.max_row)
for row in ws.values:
    pass

