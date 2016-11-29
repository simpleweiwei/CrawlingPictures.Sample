import re

# 正则替换

text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', '-', text))  # JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...
print(re.sub(r'\s+', '-', text, 2))  # 只替换两处

# 调用subn函数时除了替换，还返回替换次数
print(re.subn('[1-2]', 'A', '123456abcdef'))  # ('AA3456abcdef', 2)
print(re.subn("g.t", "have", 'I get A,  I got B ,I gut C'))  # ('I have A,  I have B ,I have C', 3)
