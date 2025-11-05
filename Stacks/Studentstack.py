# A school wants to keep track of students entering and leaving a classroom using a stack.

# Tasks:

# (a) [2 marks] Define a class StudentStack with a constructor to initialize an empty stack.

# (b) [3 marks] Implement the following methods in StudentStack:

# push(student_name) → Adds a student to the top of the stack.

# pop() → Removes and returns the student who leaves the classroom (top of the stack).

# peek() → Returns the student currently at the top of the stack without removing them.

# (c) [2 marks] Implement a method display() that prints all students currently in the stack from 
# top to bottom.

# (d) [3 marks] Write a program that:

# Pushes the students "Alice", "Bob", "Charlie", "David" onto the stack in that order.

# Displays all students in the stack.

# Simulates two students leaving by popping from the stack and displaying their names.

# Displays the remaining students in the stack.

class StudentStack:
    def __init__(self):
        self.StudentStack=[]
        
    def push(self, student_name):
        self.StudentStack.append(student_name)
        
    def pop(self):
        if not self.is_empty():
            return self.StudentStack.pop()
        else:
            return "Student is still in."
        
    def is_empty(self):
        return len(self.StudentStack)==0
    
    def size(self):
        return len(self.StudentStack)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            for i in reversed(self.StudentStack):
                print(i)
                
s=StudentStack()
s.push("Alice")
s.push("Bob")
s.push("Charlie")
s.push("David")
s.display()
print("\n")
s.pop()
s.display()