class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def push(self, e):
        self.stack.append(e)
        return True
    def pop(self):
        return self.stack.pop()
    def peek(self):
        k = len(self.stack)
        return self.stack[k-1]
    def size(self):
        return len(self.stack)
    def clear(self):
        self.stack = []
        return True
stack = Stack()
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.clear())
print(stack.size())


