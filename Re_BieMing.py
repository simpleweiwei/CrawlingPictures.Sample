import re

# 为分组起别名(?P<name>…)

line = '192.168.0.1 25/Oct/2012:14:46:34 "GET /api HTTP/1.1" 200 44 "http://abc.com/search" "Mozilla/5.0"'
reg = re.compile(
    '^(?P<remote_ip>[^ ]*) (?P<date>[^ ]*) "(?P<request>[^"]*)" (?P<status>[^ ]*) (?P<size>[^ ]*) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"')
regMatch = reg.match(line)
linebits = regMatch.groupdict()  # 得到别名字典
print(linebits)
for k, v in linebits.items():
    print(k + ": " + v)


"""
输出：

size: 44
request: GET /api HTTP/1.1
remote_ip: 192.168.0.1
user_agent: Mozilla/5.0
referrer: http://abc.com/search
status: 200
date: 25/Oct/2012:14:46:34
"""