import sys
sys.stdin = open('input.txt')

T = 10
# +, * 만 하면 되지만 그냥 사칙연산 전부 해봤습니다
for tc in range(1, T+1):
    N = int(input())
    formula = list(input())
    stack = []
    ops = []
    result = []
    isp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}
    icp = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 3}
    for f in formula:
        if f.isdecimal():
            stack.append(f)
        else:
            if not len(ops):
                ops.append(f)
            else:
                if f == ')':
                    while not ops[-1] == '(':
                        stack.append(ops.pop())
                    ops.pop()
                else:
                    while not icp[f] > isp[ops[-1]]:
                        stack.append(ops.pop())
                    ops.append(f)

    for s in stack:
        if s.isdecimal():
            result.append(s)
        else:
            num1 = int(result.pop())
            num2 = int(result.pop())
            if s == '+':
                result.append(num2 + num1)
            if s == '*':
                result.append(num2 * num1)
            if s == '-':
                result.append(num2 - num1)
            if s == '/':
                result.append(num2 / num1)
    print('#{} {}'.format(tc,result[0]))
