import sys
sys.stdin = open('input.txt')


class Stack:
    def __init__(self):
        self.top = []

    # Push
    def push(self, item):
        self.top.append(item)

    # Pop
    def pop(self):
        return self.top.pop()

    def isEmpty(self):
        return not self.top


for tc in range(2):
    par = input()
    stack = Stack()
    ans = False
    for p in par:
        if p == '(':
            stack.push(p)
        else:
            check_p = stack.pop()
            if check_p == '(':
                continue
            else:
                break
    if stack.isEmpty():
        ans = True

    print(ans)
