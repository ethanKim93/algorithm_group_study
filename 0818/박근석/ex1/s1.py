class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)


    def pop(self):
        if len(self.stack) == 0:
            return
        else:
            return self.stack.pop(-1);

s = stack()

s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())