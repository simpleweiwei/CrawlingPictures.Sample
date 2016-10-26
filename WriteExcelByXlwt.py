import xlwt

# xlwt写xlsx文件比较扯淡，好像不支持

file = xlwt.Workbook()  # 注意这里的Workbook首字母是大写
# table = file.add_sheet('sheet1')  新建一个sheet
# table.write(0, 0, 'test')  写入数据table.write(行,列,value)

# 如果对一个单元格重复操作，会引发
# returns error:
# Exception: Attempt to overwrite cell:
# sheetname=u'sheet 1' rowx=0 colx=0
# 所以在打开时加cell_overwrite_ok=True解决
table = file.add_sheet('sheet1', cell_overwrite_ok=True)

# 另外，写入时可使用style
style = xlwt.XFStyle()  # 初始化样式
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True
style.font = font  # 为样式设置字体
table.write(0, 0, 'FirstWrite', style)  # 使用样式
table.write(0, 0, 'SecondWrite', style)  # 使用样式
file.save(r'D:\demo.xls')  # 保存文件

