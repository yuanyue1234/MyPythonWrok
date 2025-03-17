# 算数运算符(加（+）、减（-）、乘（*）、除（/）、取整除法（//）、取模（%）、幂运算（**）)

# 关系运算符(等于（==）、不等于（!=）、大于（>）、小于（<）、大于等于（>=）、小于等于（<=）)

# 逻辑运算符(与（and）、或（or）、非（not）)

# 赋值运算符(简单赋值（=）、加法赋值（+=）、减法赋值（-=）、乘法赋值（*=）、除法赋值（/=）、取整除法赋值（//=）、取模赋值（%=）、幂赋值（**=）等)

# 测试运算符(is、is not、in、not in)

"""
一、选择结构
1. 条件表达式
"""
a = 5
if a:
    print('a为true')


# 单分支语句
# 单分支语句只会在条件为真时执行相应的代码块
x = 10
y = 5
if x > y:
    print(f"{x} 大于 {y}")

# 双分支语句
# 双分支语句会根据条件的真假执行不同的代码块
x = 3
y = 8
if x > y:
    print(f"{x} 大于 {y}")
else:
    print(f"{x} 小于等于 {y}")


# if elif 结构
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"成绩 {score} 对应的等级是：{grade}")

#  更具年份和月份计算当月天数
# 获取用户输入的年份和月份
year = int(input("请输入年份: "))
month = int(input("请输入月份: "))

# 判断月份对应的天数
if 1 <= month <= 12:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    else:  # 2 月需要判断是否为闰年
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days = 29
        else:
            days = 28
    print(f"{year} 年 {month} 月有 {days} 天。")
else:
    print("输入的月份无效，请输入 1 - 12 之间的数字。")


# 计算器

# 获取用户输入
a = int(input("输入第一个数字："))
c = input("请输入 + - * / 中的一个运算符：")
b = int(input("输入第二个数字："))

# 根据运算符进行计算
if c == "+":
    result = a + b
    print(result)
elif c == "-":
    result = a - b
    print(result)
elif c == "*":
    result = a * b
    print(result)
elif c == "/":
    if b == 0:
        print("错误：除数不能为 0，请重新运行程序输入有效数字。")
    else:
        result = a / b
        print(result)
else:
    print("错误：输入的运算符无效，请输入 + - * / 中的一个。")
