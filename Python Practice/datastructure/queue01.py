class Queue :
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return len(self.queue) == 0
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        a = self.queue.pop(0)
        return a
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
    def clear(self):
        self.queue == []
    
