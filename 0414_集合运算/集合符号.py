# 定义三个社团的报名人员集合
dances = {"Alice", "Bob", "Charlie", "David"}
basketballs = {"Bob", "David", "Eve", "Frank"}
badmintons = {"Charlie", "David", "Eve", "Grace"}

# 1. 交集（Intersection）
# 交集运算会返回多个集合中共同拥有的元素
# 使用 & 运算符
both_dance_and_basketball = dances & basketballs
print("既报名舞蹈又报名篮球的人员:", both_dance_and_basketball)
# 也可以使用 intersection 方法
both_dance_and_badminton = dances.intersection(badmintons)
print("既报名舞蹈又报名羽毛球的人员:", both_dance_and_badminton)

# 2. 并集（Union）
# 并集运算会将多个集合中的所有元素合并成一个集合，重复元素只保留一个
# 使用 | 运算符
all_dance_or_basketball = dances | basketballs
print("报名舞蹈或篮球的人员:", all_dance_or_basketball)
# 也可以使用 union 方法
all_dance_or_badminton = dances.union(badmintons)
print("报名舞蹈或羽毛球的人员:", all_dance_or_badminton)

# 3. 差集（Difference）
# 差集运算会返回在一个集合中但不在另一个集合中的元素
# 使用 - 运算符
only_in_dance = dances - basketballs
print("只报名舞蹈未报名篮球的人员:", only_in_dance)
# 也可以使用 difference 方法
only_in_basketball = basketballs.difference(dances)
print("只报名篮球未报名舞蹈的人员:", only_in_basketball)

# 4. 对称差集（Symmetric Difference）
# 对称差集运算会返回只在其中一个集合中出现的元素，即去除两个集合的交集部分
# 使用 ^ 运算符
unique_to_dance_or_basketball = dances ^ basketballs
print("只报名舞蹈或只报名篮球的人员:", unique_to_dance_or_basketball)
# 也可以使用 symmetric_difference 方法
unique_to_dance_or_badminton = dances.symmetric_difference(badmintons)
print("只报名舞蹈或只报名羽毛球的人员:", unique_to_dance_or_badminton)

# 5. 子集判断（Subset）
# 判断一个集合是否是另一个集合的子集
# 使用 <= 运算符
is_subset = {"Alice", "Bob"} <= dances
print("{'Alice', 'Bob'} 是否是舞蹈社团报名人员集合的子集:", is_subset)
# 也可以使用 issubset 方法
is_subset_method = {"Eve", "Frank"}.issubset(basketballs)
print("{'Eve', 'Frank'} 是否是篮球社团报名人员集合的子集:", is_subset_method)

# 6. 超集判断（Superset）
# 判断一个集合是否是另一个集合的超集（即包含另一个集合的所有元素）
# 使用 >= 运算符
is_superset = dances >= {"Alice", "Bob"}
print("舞蹈社团报名人员集合是否是 {'Alice', 'Bob'} 的超集:", is_superset)
# 也可以使用 issuperset 方法
is_superset_method = basketballs.issuperset({"Eve", "Frank"})
print("篮球社团报名人员集合是否是 {'Eve', 'Frank'} 的超集:", is_superset_method)

# 7. 不相交判断（Disjoint）
# 判断两个集合是否没有共同元素
# 使用 isdisjoint 方法
are_disjoint = dances.isdisjoint({"Grace", "Ivy"})
print("舞蹈社团报名人员集合与 {'Grace', 'Ivy'} 是否没有共同元素:", are_disjoint)