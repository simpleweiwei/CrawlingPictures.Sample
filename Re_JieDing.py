import re

content = '''
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a href="https://www.baidu.com//articles/gz.html" title="贵州省">贵州省主题介绍</a>
</td>
'''
# 使用普通方式
href_list = re.findall(r'<.+?"(.+?)" title=', content, re.I | re.M | re.S)
for link in href_list:
    print(link)

# 使用前向界定和后向界定
# ‘(?<=…)’ 前向界定－括号中 ’…’ 代表你希望匹配的字符串的前面应该出现的字符串。
# ‘(?=…)’  后向界定-括号中的 ’…’ 代表你希望匹配的字符串后面应该出现的字符串。

rule = r"(?<=href=\").+?(?=\")|(?<=href=').+?(?=')"  # 要求链接前面出现href="，后面出现"
reg = re.compile(rule, re.I | re.M | re.S)
link_list = reg.findall(content)
for l in link_list:
    print(l)
