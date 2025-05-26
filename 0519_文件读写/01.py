file1 = " 我是第一行"
file2  = "我是第二行"
file3  = "我是第三行"

try:
    f = open("test.txt", "w")
    f.write(file1)
    f.write(file2)
    f.write(file3)
finally:
    f.close()
