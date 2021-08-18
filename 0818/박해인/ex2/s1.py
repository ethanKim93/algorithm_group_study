import sys
sys.stdin = open("input.txt")

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        # underflow <-> overflow
        return
    else:
        return stack.pop(-1)

for _ in range(2):
    parenthesis = input()
    stack = [0] * len(parenthesis)
    result = True

    for p in range(len(parenthesis)):
        try:
            if p == '(':
                push('(')
            else:
                pop()
        except:
            print(False)
    else:
        if len(stack):
            print(False)
        else:
            print(True)
