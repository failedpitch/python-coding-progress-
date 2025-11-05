#getter and setter

class Student:
  def __init__(self,name,age): #parameterized means, 'self' with 'name' and 'age', default
    self.name=name             #constructor means only 'self'
    self.age=age

  #getter
  def get_name(self):
    return self.name

  #setter
  def set_name(self,v):
    self.name=v

s=Student("Yann",18)
print(s.get_name())

s.set_name("Swarnava")
print(s.get_name())