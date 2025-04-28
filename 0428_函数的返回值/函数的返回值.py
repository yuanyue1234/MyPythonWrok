# 没有返回值
a = (1,2,3,4,5)
b1,b2,*rest=a
def text1(a):
    print(a)
# 返回一个值
def  text2(b1,rest):
    return b1,rest
# 返回多个值
def text3(b1,b2,*rest):
    return b1,b2,rest

print(text1(a))
print(text2(b1,rest))
print(text3(b1,b2,*rest))
#python、 vue、 ssm 输入三个分数，作为函数的参数、定义一个函数，返回最大值最小值和

def get_max_min(score1, score2, score3):
    max_score = max(score1, score2, score3)
    min_score = min(score1, score2, score3)
    return max_score, min_score
max_score, min_score = get_max_min(10, 20, 30)
print(f"最大值: {max_score}, 最小值: {min_score}")
