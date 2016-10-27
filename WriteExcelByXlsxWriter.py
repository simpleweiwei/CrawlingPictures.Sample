import xlsxwriter
"""
XlsxWriter不支持创建老版本的xls文件（如需要可使用xlwt），且只能通过“新建Excel文件进行任意写入”（如需读取可使用
xlrd），功能比较全，支持图表和公式等
"""


workbook = xlsxwriter.Workbook(r"D:\test.xlsx")
worksheet = workbook.add_worksheet("mySheetName")
worksheet.write(0, 0, 1)
worksheet.write(0, 1, 2)
worksheet.write(0, 2, 3)
worksheet.write(0, 3, 4)
worksheet.write(0, 4, 5)
worksheet.write(0, 5, '=SUM(A%d:E%d)' % (1, 1))  # 利用求和公式写单元格
workbook.close()
