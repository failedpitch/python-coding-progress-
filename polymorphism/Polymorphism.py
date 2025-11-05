class Shape:
  def area(self):
    return 0

class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius

  def area(self):
    return 3.14*self.radius*self.radius

class Rectangle(Shape):
  def __init__(self,length,width):
    self.length=length
    self.width=width

  def area(self):
    return self.length*self.width

shapes=[Circle(5),Rectangle(4,6)]
for i in shapes:
  print(i.area())