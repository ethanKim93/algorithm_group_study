import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    S = input()
    oper = []
    stack = []
    for i in S:
        if i.isdecimal():
           stack.append(i)
        elif i == '+':
            while oper and oper[-1] == '*':
                stack.append(oper.pop())
            oper.append(i)
        else:
            oper.append(i)
    while oper:
        stack.append(oper.pop())

    temp = []
    for j in stack:
        if j.isdecimal():
            temp.append(j)
        else:
            b = int(temp.pop())
            a = int(temp.pop())
            c = 0
            if j == '+':
                c = a+b
            else:
                c = a*b
            temp.append(c)
    print('#{} {}'.format(tc, *temp))