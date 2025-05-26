file1 = "我是第一行\n"
file2 = "我是第二行\n"
file3 = "我是第三行\n"

with open("test.txt", "w", encoding="utf-8") as f:
    f.write(file1)
    f.write(file2)
    f.write(file3)

#  自动关闭文件
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())
