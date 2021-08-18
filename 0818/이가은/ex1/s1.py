class Stack(self):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return self.stack
        else:
            pop_save = self.stack.pop(-1)
            return self.stack

    def top(self):
        if len(self.stack) == 0:
            return self.stack
        else:
            return self.stack[-1]
