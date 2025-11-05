# (a) [2 marks] Define a class Queue that uses a list to store items.

# (b) [4 marks] Implement the following methods:

# enqueue(item) → adds a customer ID to the rear of the queue

# dequeue() → removes and returns the customer ID at the front of the queue

# is_empty() → checks if the queue is empty

# peek() → returns the customer ID at the front without removing it

# (c) [2 marks] Create a queue and insert the customer IDs: 101, 102, 103. Display the queue.

# (d) [2 marks] Remove one customer from the queue, display the removed customer ID, and then 
# display the updated queue.

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
q.enqueue(101)
q.enqueue(102)
q.enqueue(103) 

print("All current customer IDs", q.display())     
q.dequeue()
print("Returned customer IDs", q.display())
