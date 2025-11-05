# A library uses a stack to manage the books returned by students. The last book returned is 
# placed on the top of the stack.

# Tasks:

# (a) [2 marks] Define a class BookStack with a constructor to initialize an empty stack.

# (b) [3 marks] Implement the following methods in BookStack:

# push(book_name) → Adds a book to the top of the stack.

# pop() → Removes and returns the top book from the stack.

# peek() → Returns the top book without removing it.

# is_empty() → Returns True if the stack is empty, otherwise False.

# (c) [2 marks] Implement a method display() that prints all books in the stack from top to bottom.

# (d) [3 marks] Write a program that:

# Pushes the books "Maths", "Physics", "Chemistry", "Biology" onto the stack in that order.

# Displays all books in the stack.

class BookStack:
    def __init__(self):
        self.BookStack=[]
        
    def push(self, book_name):
        self.BookStack.append(book_name)
        
    def pop(self):
        if not self.is_empty():
            return self.BookStack.pop()
        else:
            print("Stack is empty.")
            
    def is_empty(self):
        return len(self.BookStack)==0
    
    def size(self):
        return len(self.BookStack)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            for i in reversed(self.BookStack):
                print(i)
                
b=BookStack()
b.push("Maths")
b.push("Physics")
b.push("Chemistry")
b.push("Biology")
b.push("Computer Science")
b.display()
print("\n")
b.pop()
b.display()
