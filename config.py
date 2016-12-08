import configparser
"""
1.Python的configparser模块中定义了3个类对INI或CONF文件进行操作：RawConfigParser、ConfigParser、SafeConfigParser
2.RawCnfigParser是最基础的INI文件读取类，ConfigParser、SafeConfigParser支持对%(value)s变量的解析
"""
cp = configparser.ConfigParser()
cp.read("app.conf")
secs = cp.sections()  # ['db']
print("sections", secs)

opts = cp.options("db")  # ['host', 'port', 'user', 'pass']
print('options:', opts)

kvs = cp.items("db")  # [('host', '127.0.0.1'), ('port', '3306'), ('user', 'root'), ('pass', 'root')]
print('db:', kvs)

host = cp.get("db", "host")
port_int = cp.getint("db", "port")
url = cp.get("db", "url")
print("host:", host, type(host))  # host: 127.0.0.1 <class 'str'>
print("port_int:", port_int, type(port_int))  # port_int: 3306 <class 'int'>
print("url:", url, type(url))  # url: http://127.0.0.1:3306/Portal <class 'str'>
# 新增配置值
cp.set("db", "db_name", "Product")
db_name = cp.get("db", "db_name")
print("db_name:", db_name)
# 修改配置值
cp.set("db", "db_name", "Product_Modified")
db_name = cp.get("db", "db_name")
print("db_name:", db_name)
# 新增节点
cp.add_section('ApiUrl')
cp.set('ApiUrl', 'user', 'http://www.api.com')
user = cp.get("ApiUrl", "user")
print("user:", user)
# 此处才是真正写入，不可缺少
with open("app.conf", "w") as f:
    cp.write(f)


"""
最终配置文件app.conf内容为：
[db]
url = http://%(host)s:%(port)s/Portal
host = 127.0.0.1
port = 3306
user = root
pass = root
db_name = Product_Modified

[ApiUrl]
user = http://www.api.com

"""