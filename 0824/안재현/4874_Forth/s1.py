import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for i in range(0, T):
    tc = list(input().split())
    stack = []
    result = 0
    num1 = 0
    num2 = 0
    for x in tc:
        if x.isdigit():
            stack.append(int(x))
        else:
            if x == '+' and len(stack) >= 2:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif x == '-' and len(stack) >= 2:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif x == '*' and len(stack) >= 2:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif x == '/' and len(stack) >= 2:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 // num1)
            elif x == '*' or x == '/' or x == '+' or x == '-' and len(stack) < 2:
                result = 'error'
                break
            elif x == '.' and len(stack) == 1:
                result = stack.pop()
                break
        result = 'error'

    print('#{} {}'.format(i + 1, result))
