import re

# .虽然表示任意字符，其实是不包含换行符的
# 启用re.S模式将使.表示任意字符当然也包含换行符
key = "a23b\na34b"
print(re.findall(r"a(\d+)b.+a(\d+)b", key))  # 输出[]-因为不能处理str中间有\n换行的情况
print(re.findall(r"a(\d+)b.+a(\d+)b", key, re.S))  # 输出[('23', '34')]


# 启用re.M模式将匹配多行
print(re.findall(r"^a(\d+)b", key))  # 输出['23']
print(re.findall(r"^a(\d+)b", key, re.M))  # 输出['23', '34']
