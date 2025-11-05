class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        item = self.items[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def display(self):
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


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print("Queue after enqueue:", cq.display())
print("Dequeued:", cq.dequeue())
print("Queue after dequeue:", cq.display())
cq.enqueue(50)
cq.enqueue(60)
cq.enqueue(70)
cq.enqueue(80)
print("Queue after adding 50, 60, 70:", cq.display())