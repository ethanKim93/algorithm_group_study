import sys
sys.stdin = open('input.txt')

def isp(x):
    if x == '(':
        return 0
    elif x == '+':
        return 1
    elif x == '*':
        return 2

def icp(y):
    if y == '(':
        return 3
    elif y == '+':
        return 1
    elif y == '*':
        return 2

def check(f):
    stack = []
    new_formula = []
    for i in f:
        if '0' <= i <= '9':
            new_formula.append(i)

        else:
            if not stack:
                stack.append(i)
            else:
                if i == ')':
                    while stack[-1] != '(':
                        new_formula.append(stack.pop())
                    stack.pop()
                elif icp(i) > isp(stack[-1]):
                    stack.append(i)

                else:
                    while icp(i) <= isp(stack[-1]):
                        new_formula.append(stack.pop())
                    stack.append(i)
    return new_formula

def cal(k):
    temp = []

    for i in k:
        if '0' <= i <= '9':
            temp.append(i)
        elif i == '*':
            a = temp.pop()
            b = temp.pop()
            temp.append(int(a) * int(b))
        else:
            a = temp.pop()
            b = temp.pop()
            temp.append(int(a) + int(b))
    return temp[0]



for tc in range(1, 11):
    N = int(input())
    formula = input()
    print('#{} {}'.format(tc, cal(check(formula))))
