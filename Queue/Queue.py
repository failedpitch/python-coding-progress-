class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueue:", q.display())

print("Dequeued:", q.dequeue())
print("Queue after dequeue:", q.display())

q.enqueue(50)
print("Queue after adding 50:", q.display())

  