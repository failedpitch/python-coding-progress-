class Demo:
  def show(self,a=None,b=None):
    if a is not None and b is not None:
      print("Hey again ",a,b)
    elif a is not None:
      print("Hey ",a)
    else:
      print("No arguements")
obj=Demo()
obj.show()
obj.show(20)
obj.show(30,40)