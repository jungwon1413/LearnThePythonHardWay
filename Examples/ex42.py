# -*- coding: utf-8 -*-

## Animal은 object의 일종이다 (is-a) (네, 조금 헷갈리죠) 추가 점수 부분을 살펴보세요
class Animal(object):
	pass

## Dog는 Animal의 일종이다. (어 상속인가?)
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## Cat은 Animal의 일종이다. (이것도 상속인가?)
class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## Person은 object의 일종이다.
class Person(object):

	def __init__(self, name):
		## ??
		self.name = name

		## Person은 어떤 종류의 pet을 갖고 있다 (has-a)
		self.pet = None

## Employee는 Person의 일종이다. (Person으로부터의 상속?)
class Employee(Person):

	def __init__(self, name, salary):
		## ?? 음 이 마법은 뭐죠?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## Fish는 object의 일종이다.
class Fish(object):
	pass

## Salmon은 Fish의 일종이다. (Fish로 부터의 상속?)
class Salmon(Fish):
	pass

## Halibut은 Fish의 일종이다. (Fish로 부터의 상속?)
class Halibut(Fish):
	pass


## rover는 Dog의 일종이다. (is-a)
rover = Dog("Rover")

## satan은 Cat의 일종이다
satan = Cat("Satan")

## mary는 Person의 일종이다
mary = Person("Mary")

## mary 변수에서 pet속성을 받아 satan값으로 정한다.
mary.pet = satan

## frank 변수를 Employee 클래스의 인스턴스 하나로 정한다. (첫번째 인자: name 속성 (Person, Employee 둘다 해당), 두번쨰 인자: salary 속성 (Employee 해당))
frank = Employee("Frank", 120000)

## frank 변수에서 pet속성을 받아 rover값으로 정한다.
frank.pet = rover

## flipper 변수를 Fish 클래스의 인스턴스 하나로 정한다.
flipper = Fish()

## crouse 변수를 Salmon 클래스의 인스턴스 하나로 정한다.
crouse = Salmon()

## harry 변수를 Halibut 클래스의 인스턴스 하나로 정한다.
harry = Halibut()
