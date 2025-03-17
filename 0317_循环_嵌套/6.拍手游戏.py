'''
Author: asunny e@asunny.top
Date: 2025-03-17 09:56:15
LastEditors: asunny e@asunny.top
LastEditTime: 2025-03-17 09:58:35
FilePath: \课程作业\0317_循环_嵌套\6.拍手游戏.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 遇到7 拍手

for i in range(1, 101):
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        print("*", end="\t")
    else: 
        print(i, end="\t")
    if i % 10==0:
        print()