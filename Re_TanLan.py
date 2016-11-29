import re


# 非贪婪模式的几种形式：*? +? ?? {m,n}?,除此之外其他地方出现的？多半表示"可选项"，别搞混了
key = "a123b456b"
rule = r"a(.+?)b"
pattern = re.compile(rule)
print(pattern.findall(key))  # 非贪婪：输出['123']

print(re.findall(r"a(.+)b", key))  # 贪婪： 输出['123b456']

print(re.findall(r"a(.*)b", key))  # 贪婪：输出['123b456']
