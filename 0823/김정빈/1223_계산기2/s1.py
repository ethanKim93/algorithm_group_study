import sys
sys.stdin = open("input.txt")
for tc in range(1, 11):
    N = int(input())
    exp = input()

    stack = []
    res = []
    for i in exp:
        if '0' <= i <= '9':
            res.append(i)
        elif i == '*':
            stack.append(i)
        else: # i == '+'
            if len(stack) > 0:
                while stack:
                    res.append(stack.pop())
                stack.append(i)
            else: #스택 빌때
                stack.append(i)
    if stack: #for 끝났는데도 스택에 남아있으면
        while len(stack):
            res.append(stack.pop())

    total = []
    for j in res:
        if j == '+':
            a = int(total.pop())
            b = int(total.pop())
            total.append(a+b)
        elif j == '*':
            c = int(total.pop())
            d = int(total.pop())
            total.append(c*d)
        else:
            total.append(j)

    print('#{} {}'.format(tc, *total))
