# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
	print("꼭대기에서 i는 %d" % i)
	numbers.append(i)

	i = i + 1
	print("숫자는 이제: ", numbers)
	print("바닥에서 i는 %d" % i)


print("숫자: ")

for num in numbers:
	print(num)
