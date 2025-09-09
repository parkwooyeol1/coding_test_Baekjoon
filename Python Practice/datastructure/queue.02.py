class Deque:
    def __init__(self):
        self.dq = [1]
    def isEmpty(self):
        return len(self.dq) == 0
    def addFront(self, x):
        self.dq.insert(0, x)
    def deleteFront(self):
        a = self.dq.pop(0)
        return a
    def getFront(self):
        return self.dq[0]
    def addRear(self, x):
        self.dq.append(x)
    def deleteRear(self):
        a = self.dq.pop()
        return  a
    def getRear(self):
        k = len(self.dq)
        return self.dq[k-1] 
    def size(self):
        return len(self.dq)
    def clear(self):
        self.dq = []

dq = Deque()

print(dq.isEmpty())
print(dq.addFront(2))
print(dq.deleteFront())
print(dq.getFront())
print(dq.addRear(3))
print(dq.deleteRear())
print(dq.getRear())
print(dq.size())
print(dq.clear())
