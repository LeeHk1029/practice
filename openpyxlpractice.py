from openpyxl import load_workbook

load_wb = load_workbook("C:/Users/rdrha/OneDrive/바탕 화면/helloworld (1)/안녕.xlsx")
load_ws = load_wb['Sheet2']
for row in load_ws.rows:
            print(row)