class Stack:
  def __init__(self):
    self.stack=[]

  def push(self,item):
    self.stack.append(item)

  def pop(self):
    if not self.is_empty():
      return self.stack.pop()
    else:
      return "Stack is empty"

  
  def is_empty(self):
    return len(self.stack)==0
  
  def size(self):
    return len(self.stack)

  def display(self):
    if self.is_empty():
      print("Stack is empty")
    else:
      for i  in reversed(self.stack):
        print(i)


s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("\n")
s.pop()
s.display()