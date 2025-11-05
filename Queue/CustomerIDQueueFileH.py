# (a) [2 marks] Define a class Queue that uses a list to store customer IDs.

# (b) [4 marks] Implement the following methods:

# enqueue(customerID) → adds a customer ID to the rear of the queue

# dequeue() → removes and returns the customer ID at the front of the queue

# is_empty() → checks if the queue is empty

# display() → returns the list of customer IDs in the queue

# (c) [2 marks] Create a queue, add the customer IDs 201, 202, 203, display the queue, then 
# remove one ID and display the updated queue.

# (d) [2 marks] Extend the program with file handling:

# After each enqueue or dequeue, write the current queue to a file named queue.txt.

# After all operations, read back the contents of queue.txt and display it

class Queue:
    def __init__(self):
        self.customerID = []
        
    def enqueue(self, customer):
        self.customerID.append(customer)
        
    def dequeue(self):
        if not self.is_empty():
            return self.customerID.pop(0)
        return "No customer ID."
        
    def is_empty(self):
        return len(self.customerID) == 0
    
    def display(self):
        return self.customerID
    
q=Queue()
q.enqueue(201)
q.enqueue(202)
q.enqueue(203) 

print("All current customer IDs", q.display())     
q.dequeue()
print("Returned customer IDs", q.display())

with open("queue.txt","w") as  x:
    x.write(str(q.display()))

with open("queue.txt","r") as x:
    y=x.read()
    
    print(y)