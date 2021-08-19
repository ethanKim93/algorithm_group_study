import sys
sys.stdin = open("input.txt")

stack = []
top = -1


def pop():
    global top
    top -= 1
    return stack.pop(top+1)


def push(n):
    global top
    top += 1
    stack.append(n)


for tc in range(2):
    target = input()
    result = True
    for i in range(len(target)):
        if target[i] == '(':
            push('(')
        elif target[i] == ')':
            if pop() == '(':
                pass
            else:
                result = False
                break
    for j in range(len(stack)):
        if stack[j] == 0:
            pass
        else:
            result = False
            break
    print(result)


