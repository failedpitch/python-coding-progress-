# 1<-2<-3<-4<-5<-None
class Node:
  def  __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None
  
  def insert(self,data):
    new=Node(data)
    if not self.head:
      self.head=new
      return
    temp=self.head
    while temp.next:
      temp=temp.next
    temp.next=new
  def delete(self,key):
    temp=self.head
    if temp and temp.data==key:
      self.head=temp.next
      temp=None
      return
    prev=None
    while temp and temp.data!=key:
      prev=temp
      temp=temp.next
    if temp is None:
      return
    prev.next=temp.next
    temp=None

  def display(self):
      nodes=[]
      temp=self.head
      while temp:
        nodes.append(temp.data)
        temp=temp.next
      return nodes


l1=LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
print("Linkedlist is: ",l1.display())

l1.delete(2)
print("Linkedlist is: ",l1.display())

l1.insert(6)
print("Linkedlist is: ",l1.display())