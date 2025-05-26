with open('text', 'r+', encoding="utf-8") as f:
    # readline()先定位 f.seek()
    f.seek(0)
    # 读取全部
    while True:
        line = f.readline()
        if line:
            print(line, end="")
        else:
            break

# or

    f.seek(0)
    content = f.readlines()
    print(content)
    for line in content:
        print(line, end=" ")

f1 = open('test.txt', 'r', encoding="utf-8")
f2 = open('test2.txt', 'w+', encoding="utf-8")

content = f1.readlines()
f2.writelines(content)
f2.seek(0)
for line in f2:
    print(line, end="")
f1.close()
f2.close()
