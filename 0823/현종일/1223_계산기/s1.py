import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    S = input()
    oper = []
    stack = []
    prior = ['*','/']
    for i in S:
        if i.isdecimal():
           stack.append(i)
        elif i not in prior:
            while oper and oper[-1] in prior:
                stack.append(oper.pop())
            oper.append(i)
        else:
            oper.append(i)
    while oper:
        stack.append(oper.pop())

    temp = []
    op_list = prior + ['+','-']
    for j in stack:
        if j.isdecimal():
            temp.append(j)
        else:
            b = int(temp.pop())
            a = int(temp.pop())
            c = 0
            if j == '+':
                c = a+b
            elif j == '-':
                c = a-b
            elif j == '*':
                c = a*b
            else:
                c = a/b
            temp.append(c)
    print('#{} {}'.format(tc,*temp))