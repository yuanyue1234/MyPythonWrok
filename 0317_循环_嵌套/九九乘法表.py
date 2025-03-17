i =1
while i<10:
    j=1
    while j<i:
        print(f"{j}*{i}={j*i}", end="\t")
        j+=1
    print()
    i+=1
print('------------------------------------------------')
for i in range(1,10):
    for j in range(1,10):
        print(f"{j}*{i}={j*i}", end="\t")
    print()