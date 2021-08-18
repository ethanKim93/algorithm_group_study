class Stack:
    def __init__(self):
        self.li = [0] * 3
        self.i = -1

    def push(self, num):
        self.i += 1
        self.li[self.i] = num

    def pop(self):
        num = self.li[self.i]
        self.li[self.i] = 0
        self.i -= 1
        return num


s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())



