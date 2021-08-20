import sys
sys.stdin = open('input.txt')

def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        return

    else:
        return s.pop(-1)




for tc in range(2):
    stack = list(input())
    s = []
    for item in stack:
        if item == '(':
            push(item)

        elif item == ')' and len(s) != 0:
            pop()

        elif len(s) == 0:
            break

    if s:
        print(False)
    else:
        print(True)

