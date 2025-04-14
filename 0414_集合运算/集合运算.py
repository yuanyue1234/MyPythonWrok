# 输入舞蹈社团报名人员
dances_input = input("请输入舞蹈社团报名人员，以逗号分隔: ")
dances = set(dances_input.split(','))


# 输入篮球社团报名人员
basketballs_input = input("请输入篮球社团报名人员，以逗号分隔: ")
basketballs = set(basketballs_input.split(','))

# 输入羽毛球社团报名人员
badmintons_input = input("请输入羽毛球社团报名人员，以逗号分隔: ")
badmintons = set(badmintons_input.split(','))

# 输出每个社团的人数和人员
print("舞蹈社团人数:", len(dances), "人员:", dances)
print("篮球社团人数:", len(basketballs), "人员:", basketballs)
print("羽毛球社团人数:", len(badmintons), "人员:", badmintons)

# 使用并集获取所有报名人员
all_people = badmintons|basketballs|dances
print("所有报名人员数量:", len(all_people), "人员:", all_people)

# 计算报了 3 个社团的人数
three_clubs = dances & basketballs & badmintons
print("报了 3 个社团的人数:", len(three_clubs), "人员:", three_clubs)

# 计算报了 2 个社团的人数
two_clubs =(dances & basketballs | dances & badmintons | basketballs & badmintons) - three_clubs
print("报了 2 个社团的人数:", len(two_clubs), "人员:", two_clubs)
