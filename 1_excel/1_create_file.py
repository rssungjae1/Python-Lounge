from openpyxl import Workbook
wb = Workbook() # 새 워크북 생성
ws = wb.active # 현재 활성화 된 sheet 가져옴
ws.title = "SongSheet" # 워크시트 이름변경
wb.save("sample.xlsx") # 워크북 저장
wb.close()