import sys
sys.stdin = open('input.txt')



def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop(-1)

for tc in range(2):
    N = input()
    stack = []

    for char in N:
        if char == '(':
            push(char)
        else:
            pop()
    if len(stack):
        print(False)
    else:
        print(True)
