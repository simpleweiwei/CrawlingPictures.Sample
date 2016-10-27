import xlrd
from xlutils import copy

# xlutils依赖于xlrd和xlwt，相当于它们之间的管道，仅支持xls文件修改（实质是每次copy原来的文件并重新生成一个文件）

rb = xlrd.open_workbook(r"D:\demo.xls")
wb = copy.copy(rb)
sheet = wb.get_sheet(0)
sheet.write(2, 0, 'PUSH')
sheet.write(2, 1, 'PULL')
wb.save(r'D:\demo.xls')
