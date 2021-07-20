from openpyxl import load_workbook
import io
with open("0720.xlsx", "rb") as f:
    bio = io.BytesIO()
    bio.write(f.read())
wb = load_workbook(bio, read_only=True)
ws = wb.active
print(list(ws.values))