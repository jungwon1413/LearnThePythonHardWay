# -*- coding: utf-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 188 # cm
my_weight = 82 # kg
my_eyes = '파랑'
my_teeth = '하양'
my_hair = '갈색'

print("%s에 대해 이야기해 보죠." % my_name)
print("키는 %d 센티미터고요." % my_height)
print("몸무게는 %d 킬로그램이에요." % my_weight)
print("사실 아주 많이 나가는 건 아니죠.")
print("눈은 %s이고 머리는 %s이에요." % (my_eyes, my_hair))
print("이는 보통 %s이고 커피를 먹으면 달라져요." % my_teeth)

# This line is complicated, but copy exactly
# print("%d, %d, %d를 모두 더하면 %d 랍니다." % my_age, my_height, my_weight, my_age + my_height + my_weight)

print("{} {} {}를 모두 더하면 {} 랍니다.".format(
     my_age, my_height, my_weight, my_age + my_height + my_weight))    # python3 style