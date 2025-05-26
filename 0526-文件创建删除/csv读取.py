import csv
f =  open('test2.csv','r',encoding='utf-8')
csv_reader = csv.reader(f) # 创建读取器对象
for line in csv_reader:
    print(line)