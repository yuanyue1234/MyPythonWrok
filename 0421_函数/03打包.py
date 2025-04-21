def text1(*args):
    print(args)
text1(1,2,3,4,5)
def text2(**kwargs):
    print(kwargs)

text2(a=1,b=2,c=3)

# 6. 解包
def text3(a,b,c,d):
    print(a,b,c,d)
t1 = tuple(range(4))
text3(*t1)

list1 = set('pyth')
text3(*list1)
d1 = {'a':1,'b':2,'c':3}

text3(**d1)