import sys
sys.stdin = open('input.txt')


def push(n):
    global top
    top += 1
    stack[top] = n


def pop():
    global top
    stack[top] = 0
    top -= 1


for tc in range(1, 3):
    gwalho = input()
    stack = [0] * len(gwalho)
    top = -1

    for i in gwalho:
        if i == '(':
            push('(')
        else:
            if '(' not in stack:
                print('스택에 ( 가 없습니다.')
            else:
                pop()

    if '(' in stack:
        print('스택에 ( 가 남아있습니다.')
    else:
        print('스택에 아무것도 없습니다.')
