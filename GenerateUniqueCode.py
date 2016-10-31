import random
import string
"""
主键+随机码的方式:

优点：使用也比较简单，不用直接去查询数据库，而最大的优点是查询的时候，可以根据邀请码直接得到主键id, 然后根据id去数据库查询(速度很快)，再比较查询出来的邀请码和用户提交的邀请码是否一致。
"""


def create_code(id, length=12):
    """
    组成：id(数据库primary key )->16进制 + "L(标识符)" +随机码

    :param id: DB主键
    :param length: 随机码的长度
    """
    prefix = hex(int(id))[2:] + 'L'  # 因为16进制数前两位均为0x，只是标识，所以从2切片，其中'L'是业务标识符
    length -= len(prefix)
    chars = string.ascii_letters + string.digits  # 所有的大小写字母和数字
    return prefix + ''.join([random.choice(chars) for i in range(length)])  # 将前缀与随机字符串进行拼接


def get_id(code):
    """ 将16进制的id再转回10进制 """
    return str(int(code.upper(), 16))


if __name__ == "__main__":
    for i in range(10, 500, 35):
        code = create_code(i)
        id_hex = code.split('L')[0]
        id = get_id(id_hex)
        print(code, id)  # 输出唯一随机码和DB的主键Id
