# 定义全局变量来存储银行卡余额
money = 0

def setmoney():
    global money
    amount = float(input("请输入存款金额: "))
    if amount > 0:
        money += amount
        print(f"存款成功！当前余额为: {money}")
    else:
        print("存款金额必须大于 0。")


def getmoney():
    global money
    amount = float(input("请输入取款金额: "))
    if amount > 0:
        if amount <= money:
            money -= amount
            print(f"取款成功！当前余额为: {money}")
        else:
            print("余额不足，取款失败。")
    else:
        print("取款金额必须大于 0。")


def querymoney():
    print(f"当前余额为: {money}")


def main():
    while True:
        print("\n欢迎使用常德职业技术学院农行ATM系统，请选择你的操作：")
        print("1. 存款")
        print("2. 取款")
        print("3. 查看余额")
        print("4. 退出")
        choice = input("请输入你的选择 (1-4): ")

        if choice == '1':
            setmoney()
        elif choice == '2':
            getmoney()
        elif choice == '3':
            querymoney()
        elif choice == '4':
            print("感谢使用，再见！")
            break
        else:
            print("无效的选择，请输入 1-4 之间的数字。")


if __name__ == "__main__":
    main()
