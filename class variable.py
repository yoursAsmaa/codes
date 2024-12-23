# -*- coding: utf-8 -*-

class mnustudent:
	stream = 'iot'
	def __init__(self,name,roll):
		self.name = name		 
		self.roll = roll		

# Class variables can be accessed using class
print(mnustudent.stream)

a = mnustudent('asmaa', 1)
b = mnustudent('jana', 2)

print(a.stream) 
print(b.stream) 
print(a.name) 
print(b.name)
print(a.roll)
print(b.roll) 

#we can change the stream directly from the class
mnustudent.stream = 'mi'

print(a.stream)
print(b.stream)
print(mnustudent.stream)