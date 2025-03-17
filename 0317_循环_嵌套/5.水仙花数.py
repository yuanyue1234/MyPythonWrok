'''
Author: asunny e@asunny.top
Date: 2025-03-17 09:52:48
LastEditors: asunny e@asunny.top
LastEditTime: 2025-03-17 09:54:35
FilePath: \课程作业\0317_循环_嵌套\5.水仙花数.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 水仙花数 
# 水仙花数是一个 三位数，其各位数字的立方和等于该数本身。

for i in range(100,1000):
    one = i % 10
    ten = i // 10 % 10
    hundred = i // 100
    if i == one ** 3 + ten ** 3 + hundred ** 3:
        print(i)