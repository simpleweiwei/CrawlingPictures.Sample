import re

# 正则表达式最好编译一下可复用
# search方法比match通用
# findall查找所用匹配项目比较方便

html = r"<html><body><p>hello world</p><p>hello world2</p><p>hello world3</p></body></html>"
rule = r"<p>(.*?)</p>"  # .*?：任意字符＋零个或多个＋非贪婪模式
pattern = re.compile(rule)
group_result = pattern.search(html)  # 得到一个p标签,无论这个p标签在什么地方
print(group_result.group(1))  # 得到分组1的结果：hello world，如果分组值为0或者不传,则结果：<p>hello world</p>

group_result2 = pattern.match(html)  # 得到一个p标签,这个p标签必须在文本开头，不然结果为None
print(group_result2)  # 因为没有p标签开头的东东，所以为：None

list_result = pattern.findall(html)  # 得到所有p标签的内容,返回的是个字符串列表
print(list_result)  # ['hello world', 'hello world2', 'hello world3']
