# -*- coding: utf-8 -*-

print("몇 살이죠?"),
age = input()    # raw_input: python2 / input: python3
print("키는 얼마죠?"),
height = input()    # raw_input: python2 / input: python3
print("몸무게는 얼마죠?"),
weight = input()    # raw_input: python2 / input: python3

print("네, 나이는%r 살, 키는%r, 몸무게는%r이네요." % (
	age, height, weight))
print("뜬금없지만, 태양의 각지름은%r 정도입니다." % '''32'10"''')
