import json
import xlwt


with open('data/coords.json', 'r', encoding='utf-8') as input:
    data = json.load(input)

wb = xlwt.Workbook()
ws = wb.add_sheet('Coords')

i = 0
for coords in data.values():
    if i in [407, 370, 214, 356, 357, 259, 390, 244, 293, 388, 324, 412, 261]:
        continue
    ws.write(i, 0, coords[0])
    ws.write(i, 1, coords[1])
    ws.write(i, 2, 'Пятёрочка #' + str(i + 1))
    ws.write(i, 3, '')
    ws.write(i, 4, i + 1)
    i += 1

wb.save('data/toMap.xls')
