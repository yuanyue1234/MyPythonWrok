dict1 = {"name": "Tom", "age": 18, "gender": "male"}
dict2 = {"score": 100}
dict3 = dict(dict1)
dict4 = zip(dict1, dict2)
# print(dict4)
# 访问字典
# 字典名[key]
print(dict1["name"])
# 字典名.get(key)
print(dict1.get("name"))
print(dict1.keys())
for item in dict1:
    print(item,dict1[item])

dict1.update({"name": "Jerry"})
dict1.pop('age')
print(dict1)
# popitem 随机删除
print(dict3.popitem())
# clear 清空
print(dict3.clear())
# 取反
dict5 = { v:key for key,v in dict1.items()}
print(dict5)
