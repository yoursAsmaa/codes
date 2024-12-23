# -*- coding: utf-8 -*-

class Person():
 	def __init__(self, name, age):
         self.name = name
         self.age = age
 	def display(self):
         print(self.name, self.age)
    
    # child class
class Student(Person):
 	def __init__(self, name, age, DOB):
         self.DOB = DOB
         super().__init__(name, age)
    
 	def displayInfo(self):
         print(self.name, self.age, self.DOB)

obj = Student("Asmaa", 19, "29/05/05")
obj.display()
obj.displayInfo()