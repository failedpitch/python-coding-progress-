# company wants to manage customer service requests using a Circular Queue.
# The system should work as follows:

# Create a circular queue of size 4.
# Implement the following methods:

# add_request(request_id) → Add a new service request. If the queue is full, print "Service queue 
# is full".

# process_request() → Remove the oldest service request and print "Processing request <id>". 
# If the queue is empty, print "No requests to process".

# show_requests() → Display the current requests in the queue in order.
# Perform the following operations in order:
# Copy code

# add_request("R101")
# add_request("R102")
# add_request("R103")
# process_request()
# add_request("R104")
# add_request("R105")
# show_requests()

class Servicequeue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1
        
class add_request:
    def __init__(self, request_id):
        def enqueue(self, request_id):
            if self.is_full():
                print ("Service queue is full.")
                return
            if self.is_empty():
                self.front = 0
                self.rear = (self.rear + 1) % self.capacity
                self.items[self.rear] = request_id
                
class ServiceQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def add_request(self, request_id):
        if self.is_full():
            print("Service queue is full.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = request_id

    def process_request(self):
        if self.is_empty():
            return "No requests to process"
        item = self.items[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Processing request {item}.")
        return item

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def show_requests(self):
        if self.is_empty():
            return []
        elements = []
        i = self.front
        while True:
            elements.append(self.items[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return elements


sq = ServiceQueue(4)
print("Current Service Requests:", sq.show_requests())
sq.add_request("R101")
sq.add_request("R102")
sq.add_request("R103")
print("Requests after adding:", sq.show_requests())
sq.process_request()
print("After processing one request:", sq.show_requests())
sq.add_request("R104")
sq.add_request("R105")
print("Final Requests in Queue:", sq.show_requests())