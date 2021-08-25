import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    sen = input()
    opers = []
    stack = []
    for i in sen:
        if i.isdecimal():
            stack.append(i)
        elif i == ')':
            while opers and opers[-1] != '(':
                stack.append(opers.pop())
            opers.pop()
        elif i == '+':
            while opers and opers[-1] not in '+(':
                stack.append(opers.pop())
            opers.append(i)
        else:
            opers.append(i)

    while opers:
        stack.append(opers.pop())

    result = []
    for j in stack:
        if j.isdecimal():
            result.append(j)
        else:
            b = int(result.pop())
            a = int(result.pop())
            c = a + b if j == '+' else a * b
            result.append(c)
    print('#{} {}'.format(tc, result[-1]))

