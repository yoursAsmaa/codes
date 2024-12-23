# -*- coding: utf-8 -*-


class Employee:

 	def __init__(self , b = 15):
          self.balance = b
          print('Employee created.')

 	def __add__(self , other):
          return Employee(self.balance - other)

 	def __del__(self):
	  	print('Destructor called, Employee deleted.')

obj1 = Employee()
obj2 = obj1 + 10
print(obj2.balance)
del obj2