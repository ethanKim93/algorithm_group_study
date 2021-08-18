import sys
sys.stdin = open("input.txt")

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return print("Error")
        else:
            pop_save = self.stack.pop(-1)
            return self.stack

    def top(self):
        if len(self.stack) == 0:
            return self.stack
        else:
            return self.stack[-1]



for _ in range(2):
    check = str(input())
    pair = Stack()

    for i in check:
        if i == '(':
            pair.push('(')
        elif i == ')':
            pair.pop()

    if pair.stack == []:
        print('Success')
    else:
        print('Fail')