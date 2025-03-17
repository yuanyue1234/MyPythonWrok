# 整数（int）
# 整数是没有小数部分的数字，可以是正数、负数或零
i = 42
print(f"整数类型示例: {i}，类型: {type(i)}")

# 浮点数（float）
# 浮点数是带有小数部分的数字
f = 3.14
print(f"浮点数类型示例: {f}，类型: {type(f)}")

# 布尔值（bool）
# 布尔值只有两个可能的值：True 或 False
t = True
f_val = False
print(f"布尔值类型示例 - True: {t}，类型: {type(t)}")
print(f"布尔值类型示例 - False: {f_val}，类型: {type(f_val)}")

# 字符串（str）
# 字符串是由零个或多个字符组成的序列，可以使用单引号、双引号或三引号来表示
s1 = 'Hello, World!'
s2 = "Hello, Python!"
s3 = '''This is a multi - line
string example.'''
print(f"字符串类型示例 - 单引号: {s1}，类型: {type(s1)}")
print(f"字符串类型示例 - 双引号: {s2}，类型: {type(s2)}")
print(f"字符串类型示例 - 三引号: {s3}，类型: {type(s3)}")

# 列表（list）
# 列表是一种可变的、有序的序列，可以包含不同类型的元素
lst = [1, 2, 3, 'apple', 'banana']
print(f"列表类型示例: {lst}，类型: {type(lst)}")

# 元组（tuple）
# 元组是一种不可变的、有序的序列，可以包含不同类型的元素
tup = (1, 2, 3, 'apple', 'banana')
print(f"元组类型示例: {tup}，类型: {type(tup)}")

# 集合（set）
# 集合是一种无序的、唯一的元素集合
st = {1, 2, 3, 3, 4}  # 重复的元素会被自动去除
print(f"集合类型示例: {st}，类型: {type(st)}")

# 字典（dict）
# 字典是一种无序的键值对集合，每个键必须是唯一的
d = {'name': 'John', 'age': 30, 'city': 'New York'}
print(f"字典类型示例: {d}，类型: {type(d)}")