import csv

"""
读取csv
"""
# 示例1
with open(r"C:\Users\Administrator\Desktop\购买关注用户\20161020094049.CSV", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # row为列表形式：['2cbc111fa85c428ea86062757de86d5e', 'ZH160759']

# 示例2
with open(r"C:\Users\Administrator\Desktop\购买关注用户\20161020094049.CSV", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # row为字典形式：{'ZhbId': 'ZH160759', 'CustomerNo': '2cbc111fa85c428ea86062757de86d5e'}


"""
写csv
"""
# 示例1
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        ]
with open(r'D:\stocks.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)  # 单行写，注意写入的是列表
    f_csv.writerows(rows)  # 多行写，注意写入的是列表


# 示例2:如果你有一个字典序列的数据，可以像下面这样做
headers2 = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows2 = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]
with open(r'D:\stocks2.csv','w') as f:
    f_csv = csv.DictWriter(f, headers2)
    f_csv.writeheader()
    f_csv.writerows(rows2)

# 备注：python读取大csv时需要修改限制数，或者分块读取
csv.field_size_limit(10000000)
print(csv.field_size_limit())  # 默认131072行，此时变为10000000行
