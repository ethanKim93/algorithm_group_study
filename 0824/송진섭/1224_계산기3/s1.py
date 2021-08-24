import sys
sys.stdin = open('input.txt')

for tc in range(1, 12):
    N = int(input())
    expression = input()

    isp = ['(', '+', '*']
    icp = ['', '+', '*', '(']
    result = []
    stack = []

    for i in expression:
        if i.isdecimal():
            result.append(i)
        else:
            if not stack:
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    result.append(stack.pop())
                del stack[-1]
            elif isp.index(stack[-1]) < icp.index(i):
                stack.append(i)
            else:
                while isp.index(stack[-1]) >= icp.index(i):
                    result.append(stack.pop())
                    if len(stack) == 0:
                        break
                stack.append(i)
    while stack:
        result.append(stack.pop())

    for i in result:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '+':
            b = stack.pop()
            a = stack.pop()
            c = a + b
            stack.append(c)
        else:
            b = stack.pop()
            a = stack.pop()
            c = a * b
            stack.append(c)
        if len(stack) == 1:
            answer = stack[0]

    print('#{} {}'.format(tc, answer))