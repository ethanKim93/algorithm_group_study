import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    formula = input().split()
    stack = []
    try:
        for i in formula:
            if i == '.':
                result = stack.pop()
                if len(stack) != 0:
                    result = 'error'
                break
            elif i == '+':
                stack.append(stack.pop(-2) + stack.pop())
            elif i == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif i == '*':
                stack.append(stack.pop(-2) * stack.pop())
            elif i == '/':
                stack.append(stack.pop(-2) // stack.pop())
            else:
                stack.append(int(i))

    except:
        result = 'error'

    print('#{} {}'.format(tc, result))


