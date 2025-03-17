# 求和 偶数 奇数

s = 0

odd = 0

even = 0

for i in range(0,100):
    if i % 2 == 0:
        even +=1
    else:
        odd +=1
    s+=i
print(odd)
print(even)
print(s)