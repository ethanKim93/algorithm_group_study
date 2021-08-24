import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    formula = input()
    trans = ''
    stack = []
    result = 0
    for i in formula:
        if i == '*':
            while len(stack) and stack[-1] != '+':
                trans += stack.pop()
            stack.append(i)
        elif i == '+':
            while len(stack):
                trans += stack.pop()
            stack.append(i)
        else:
            trans += i
    for s in range(len(stack)):
        trans += stack.pop()

    for t in trans:
        if t == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(b + a)
        elif t == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        else:
            stack.append(int(t))
    print('#{} {}'.format(tc, stack[0]))