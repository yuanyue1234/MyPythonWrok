import os.path
import time
temp = os.path.getctime('test2.txt')
print(temp)
print(time.strftime('%y-%m-%d %H:%M:%S',  time.localtime(temp)))