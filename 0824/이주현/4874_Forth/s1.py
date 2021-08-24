import sys
sys.stdin = open('sample_input.txt', 'r')

def cal(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a // b

T = int(input())
for tc in range(1, T + 1):
    string = list(map(str, input().split()))
    stack = []
    i = 0

    while string[i] != '.':
        if string[i] not in '/*-+':
            stack.append(string[i])
        else:
            if len(stack) > 1:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(cal(a, b, string[i]))
            else:
                break
        i += 1

    if len(stack) == 1 and i == len(string) - 1:
        print("#{} {}".format(tc, stack[0]))
    else:
        print("#{} {}".format(tc, 'error'))