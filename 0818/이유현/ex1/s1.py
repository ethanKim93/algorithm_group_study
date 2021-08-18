class Stack:
    def __init__(self):
        self.top = []

    # Push
    def push(self, item):
        self.top.append(item)

    # Pop
    def pop(self):
        return self.top.pop()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())