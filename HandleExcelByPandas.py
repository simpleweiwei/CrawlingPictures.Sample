import pandas as pd

# 读入excel文件中的第2个表
df = pd.read_excel('log.xls', sheetname=1)
# 查看表的数据类型
print(df.dtypes)
# 查看Member列的数据
print(df['Member'])

'''
# 新建一列，每一行的值是Member列和activity列相同行值的和
for i in df.index:
  df['activity_2'][i] = df['Member'][i] + df['activity'][i]
'''

# 根据Member字段去除掉多余的行，并且保留相同行的最后一行数据
new_df = df.drop_duplicates(subset='Member', keep='last')
# 导出结果
out = pd.ExcelWriter('output.xls')
new_df.to_excel(out)
out.save()
