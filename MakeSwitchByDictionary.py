def key_1_pressed():
    print('Key 1 Pressed')


def key_2_pressed():
    print('Key 2 Pressed')


def key_3_pressed():
    print('Key 3 Pressed')


def unknown_key_pressed():
    print('Unknown Key Pressed')

code = 2

# 1.正常模式
if code == 1:
    key_1_pressed()
elif code == 2:
    key_2_pressed()
elif code == 3:
    key_3_pressed()
else:
    unknown_key_pressed()

# 2.Dictionary模拟Switch模式
functions = {1: key_1_pressed, 2: key_2_pressed, 3: key_3_pressed}
functions.get(code, unknown_key_pressed)()
