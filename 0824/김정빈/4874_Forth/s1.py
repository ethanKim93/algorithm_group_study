import sys
sys.stdin = open("input.txt")
#4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    stack = []

    try:
        for i in arr:
            if i == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(b // a)
            elif i == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif i == '.':
                if len(stack) > 1:
                    print('#{} {}'.format(tc, "error"))
                else:
                    print('#{} {}'.format(tc, *stack))
            else:
                stack.append(int(i))
        # print('#{} {}'.format(tc, *stack))
    except:
        print('#{} {}'.format(tc, "error"))