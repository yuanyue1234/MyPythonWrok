import csv
f =  open('text.csv','r',encoding='utf-8')
csv_reader = csv.reader(f) # 创建读取器对象
for line in csv_reader:
    print(line)
csvfile = open('test2.csv','w',encoding='utf-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['测试','测试','测试3'])