list0 = []
print(type(list0))
list1 = list()
print(type(list1))
list2 = [1,2,"3",4.0,True]
for i in range(1,4):
    print(i)
for i in "python":
    print(i)
# 可迭代对象可以用在for循环

from collections.abc import Iterable
print(isinstance(list1, Iterable))

# 访问列表元素
# 1. 通过索引
print(list2[2])
print(list2[-2])

# 2. 切片方式 (获取新的列表)
list3 = list(range(1,10))

print(list3[2:5])
print(list3[2:])
print(list3[:5])
print(list3[::2])

# 3.循环方式
for i in list3:
    print(i,end=" ")
# in 与 not  in
print()
print(2 in list3)
print(10 not in list3)

# 添加列表元素
list3.append("hello")
print(list3)
# insert()在指定位置添加
list3.insert(2,"yy")
print(list3)
# extend()在末尾添加一个新的列表
list4 = ["yy",18]
list3.extend(list4)
list3.extend(["yy",18])
print(list3)

# 删除语句
# del语句：删除指定位置的元素
del list3[-1]
# remove()删除列表中得某一个元素，匹配第一个元素
list3.remove("yy")
print(list3)
# pop([index]):默认删除列表中的最后一个元素
list3.pop()
list3.pop(1) # 1指的是索引
print(list3)
# clear() 清空
list3.clear()
print(list3)

# 排序
# 1.sort() 直接对原列表进行排序，排序后原列表的顺序会被改变。
list5 = [29,31,12,38,99]
list5.sort()
print(list5)

# 2.reverse() 逆转列表
list5=[29,31,12,38,99]
list5.reverse()
print(list5)

# 3.sorted(): 生成一个新的排序后的列表
list6 =[29,31,12,38,99]
list7 = sorted(list6)
print(list6)
print(list7)