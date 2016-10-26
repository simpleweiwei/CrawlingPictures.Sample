import xlrd

"""
跨平台读取Excel文件，同时支持.xls和.xlsx后缀的Excel。

1、导入模块
      import xlrd
2、打开Excel文件读取数据
       data = xlrd.open_workbook('xx.xlsx')
3、使用技巧
        获取一个工作表
        table = data.sheets()[0]  # 通过索引顺序获取
        table = data.sheet_by_index(0)  # 通过索引顺序获取
        table = data.sheet_by_name(r'Sheet1')  # 通过名称获取

        获取整行和整列的值（数组）
         table.row_values(i)
         table.col_values(i)

        获取行数和列数
        nrows = table.nrows
        ncols = table.ncols

        循环行列表数据
        for i in range(nrows ):
           print table.row_values(i)

        单元格
        cell_A1 = table.cell(0,0).value
        cell_C4 = table.cell(2,3).value

        使用行列索引
        cell_A1 = table.row(0)[0].value
        cell_A2 = table.col(1)[0].value

        简单的写入
        row = 0
        col = 0
        # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        ctype = 1 value = '单元格的值'
        xf = 0 # 扩展的格式化

        table.put_cell(row, col, ctype, value, xf)
        table.cell(0,0)  #单元格的值'
        table.cell(0,0).value #单元格的值'
"""


def open_excel(file='file.xls'):
    """
    打开文件
    """

    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)


def get_sheet_by_index(file='file.xls', colnameindex=0, _index=0):
    """
    根据索引获取Excel表格中的sheet数据
    """

    data = open_excel(file)
    table = data.sheets()[_index]
    rows_count = table.nrows  # 行数
    cols_count = table.ncols  # 列数
    col_names = table.row_values(colnameindex)  # 标题行数据
    list = []
    for rownum in range(1, rows_count):

        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(col_names)):
                app[col_names[i]] = row[i]
            list.append(app)
    return list


def get_sheet_by_name(file='file.xls', colnameindex=0, _name=r'20161020094049'):
    """
    根据名称获取Excel表格中的sheet数据
    :param file:Excel文件路径
    :param colnameindex:表头索引
    :param _name:Sheet名称
    :return:列表
    """

    data = open_excel(file)
    table = data.sheet_by_name(_name)
    rows_count = table.nrows  # 行数
    col_names = table.row_values(colnameindex)  # 标题行数据
    list = []
    for rownum in range(1, rows_count):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(col_names)):
                app[col_names[i]] = row[i]
            list.append(app)
    return list


def main():
    tables = get_sheet_by_index(r'C:\Users\Administrator\Desktop\购买关注用户\关注20161020.xlsx')
    for row in tables:
        print(row)

    tables = get_sheet_by_name(r'C:\Users\Administrator\Desktop\购买关注用户\关注20161020.xlsx')
    for row in tables:
        print(row)


if __name__ == "__main__":
    main()
