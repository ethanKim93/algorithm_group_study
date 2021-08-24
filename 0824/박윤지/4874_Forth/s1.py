import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    eq = input().split()
    stack = []
    ans = ''

    for i in eq:
        if i.isdecimal():
            stack.append(int(i))
        else:
            if i in ['+', '-', '*', '/'] and len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(a/b)
            elif i in ['+', '-', '*', '/'] and len(stack) <= 1:
                ans = 'error'
                break
            else:  # '.'일 때
                if len(stack) == 1:
                    ans = int(stack.pop())  # '/' 연산 하면 나누어 떨어져도 2.0 처럼 소숫점이 생긴다. 그래서 int()로 감싸야함
                else:
                    ans = 'error'
                    break

    print('#{} {}'.format(tc, ans))

