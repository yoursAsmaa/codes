# -*- coding: utf-8 -*-


class Base(object):
      def __init__(self, name):
          self.name = name

      def getName(self):
          return self.name

class Child(Base):
 	def __init__(self, name, age):
          Base.__init__(self, name)
          self.age = age

 	def getAge(self):
          return self.age

class GrandChild(Child):

 	def __init__(self, name, age, address):
          Child.__init__(self, name, age)
          self.address = address

 	def getAddress(self):
          return self.address

a = GrandChild("asmaa", 19, "cairo")
print(a.getName(), a.getAge(), a.getAddress())