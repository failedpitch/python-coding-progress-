# Write a Python function find_middle() that returns the middle element of a singly linked list.
# Task:
# Create a linked list with elements 5, 10, 15, 20, 25.
# Find and display the middle element.

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
l1.insert(5)
l1.insert(10)
l1.insert(15)
l1.insert(20)
l1.insert(25)
print("Linkedlist is: ",l1.display())

class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node2(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

l1 = LinkedList()
l1.insert(5)
l1.insert(10)
l1.insert(15)
l1.insert(20)
l1.insert(25)

print("Middle element:", l1.find_middle())
            