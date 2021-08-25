import sys
sys.stdin = open('input.txt', 'r')

def cal(a, b, c):
    if c == '+':
        return a + b
    return a * b

for tc in range(1, 11):
    N = int(input())
    string = input()

    stack_cal = []
    stack_result = []
    for i in range(N):
        if string[i] in '1234567890':
            stack_result += [string[i]]
        else:
            if stack_cal:
                if string[i] == '+':
                    while stack_cal:
                        stack_result += [stack_cal.pop()]
                    stack_cal += [string[i]]
                else:
                    while stack_cal[-1] == '*':
                        stack_result += [stack_cal.pop()]
                        if not stack_cal:
                            break
                    stack_cal += [string[i]]
            else:
                stack_cal += [string[i]]
    for i in range(len(stack_cal)):
        stack_result += [stack_cal.pop()]

    for i in range(len(stack_result)):
        if stack_result[i] in '1234567890':
            stack_cal += [stack_result[i]]
        else:
            b = int(stack_cal.pop())
            a = int(stack_cal.pop())
            stack_cal += [str(cal(a, b, stack_result[i]))]

    print("#{} {}".format(tc, stack_cal[-1]))