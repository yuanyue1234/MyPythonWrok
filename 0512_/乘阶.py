# x = int(input("请输入一个数："))
# for a in range(1,x+1):
#     a *= a
#
#

def digui(x):
    if x == 1:
        return 1
    else:
        return x * digui(x-1)

print(digui(5))


def digui2(x):
    if x ==1 or x == 2:
        return 1
    else:
        return digui2(x-1) + digui2(x-2)

print(digui2(25))


lamada_text = lambda x,y: pow(x,y)
print(lamada_text(5,3))

