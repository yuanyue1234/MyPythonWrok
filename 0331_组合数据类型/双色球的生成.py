# 红色 1-33 蓝色 1-16
# 红色有6个 蓝色有1个
# 1. 用循环生成得红色球6个，号码事1-33中得随机数。
import random

list1 = []
while len(list1) <= 6:
    num = random.randint(1, 33)
    if num not in list1:
        list1.append(num)
print(list1)

# 蓝色 直接生成1-16范围得蓝色
list1.append(random.randint(1,16))
print("红色球是:")
for i in list1:
    print(i,end=" ")
print("蓝色球是:",list1[-1])
print("蓝色球是:",list1[-1])