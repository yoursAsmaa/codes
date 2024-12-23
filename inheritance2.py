# -*- coding: utf-8 -*-


class Base1(object):
 	def __init__(self):
          self.str1 = "asmaa"
          print("Base1")


class Base2(object):
 	def __init__(self):
          self.str2 = "jana"
          print("Base2")


class Derived(Base1, Base2):
 	def __init__(self):
          Base1.__init__(self)
          Base2.__init__(self)
          print("Derived")

 	def printStrs(self):
          print(self.str1)
          print(self.str2)


ob = Derived()
ob.printStrs()