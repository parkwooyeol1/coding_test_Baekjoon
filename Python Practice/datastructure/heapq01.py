class Queue :
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return len(self.queue) == 0
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        a = max(self.queue)
        self.queue.remove(a)
        return a
    def peek(self):
        return max(self.queue)
    def size(self):
        return len(self.queue)
    def clear(self):
        self.queue = []
prq = Queue()

prq.enqueue(1)
prq.enqueue(3)
prq.enqueue(2)



print(prq.dequeue())
print(prq.queue)
print(prq.dequeue())
print(prq.queue)

prq.clear()
print(prq.queue)