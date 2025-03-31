# 猜数字

# 导入random 随机数
import random
random_num = random.randint(1, 100)  # 猜1-100的数字

# print(random_num)

stop = True

while stop:
    try:
        my_num = int(input("请输入1-100内的数字："))
    except ValueError:
        print("输入无效，请输入一个有效的整数。")
        continue
    if random_num == my_num:
        print("猜对了")
        # stop = False
        break
    elif my_num > 100:
        print("超出范围")
    elif random_num > my_num:
        print("猜小了")
    elif random_num < my_num:
        print("猜大了")
    else:
        print("出错")
