import json

# 示例1：将Python字典转换为json字符串
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data, sort_keys=False, indent=3)  # 这样就可以显示地漂亮一些
"""
Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key
ensure_ascii：默认值True，如果dict内含有non-ASCII的字符，则会类似"uXXXX"的显示数据，设置成False后，就能正常显示
indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty-printed json
separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(',',':')；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。
encoding：默认是UTF-8，设置json数据的编码方式。
sort_keys：将数据根据keys的值进行排序。
"""
print(json_str)

# 示例2：将json字符串装载为Python字典
data = json.loads(json_str)
print(data["shares"])

# 示例3：将通过接口访问到的数据装载为Python字典
from urllib.request import urlopen

u = urlopen(r'http://appnewstest.1234567.com.cn:9305/apibuy.html')
resp = json.loads(u.read().decode('utf-8'))
print(resp)

# 示例4：将json字符串装载为Python其他对象(OrderedDict)
from collections import OrderedDict

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
orderedDictObj = json.loads(s, object_pairs_hook=OrderedDict)
print(orderedDictObj)


# 示例5：将json字符串装载为Python其他对象(JSONObject)
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


str = '{"name": "ACME", "shares": 50, "price": 490.1}'
jsonObj = json.loads(str, object_hook=JSONObject)
print(jsonObj.name)


# 示例6：将普通Python对象序列化为JSON字符串
# 对象实例通常并不是JSON可序列化的，如果你想序列化对象实例，你可以提供一个函数，它的输入是一个实例，返回一个可序列化的字典。
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
objStr = json.dumps(p, default=serialize_instance)
print(objStr)

# 示例7：将JSON字符串装载为普通Python对象
# Dictionary mapping names to known classes
classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


a = json.loads(objStr, object_hook=unserialize_object)
print(a.x)
