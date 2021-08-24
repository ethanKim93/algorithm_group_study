import sys
sys.stdin = open('input.txt')

def cal(text):
    stack = []
    sub = []
    calc = []
    ls = ['(', ')', '+', '*']
    for i in range(N):
        if text[i] in ls:
            if text[i] == '(':
                stack.append(text[i])
            elif text[i] == '*':
                stack.append(text[i])
            elif text[i] == '+':
                while stack[-1] != '(':
                    sub.append(stack.pop())
                stack.append(text[i])
            else:
                while stack[-1] != '(':
                    sub.append(stack.pop())
                stack.pop()
        else:
            sub.append(text[i])
    for j in sub:
        if j == '+':
            calc.append(calc.pop() + calc.pop())
        elif j == '*':
            calc.append(calc.pop() * calc.pop())
        else:
            calc.append(int(j))
    return calc.pop()

for tc in range(1, 11):
    N = int(input())
    text = input()

    print('#{} {}'.format(tc, cal(text)))