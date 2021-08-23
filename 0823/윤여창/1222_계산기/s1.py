import sys
sys.stdin = open('input.txt')    # 계산기2 문제가 안풀려서 계산기1 문제 풀거라도 제출합니다.


T = 10

for tc in range(1, T+1):
    N = int(input())
    S = input()

    stack = []
    postfix = ''
    cal = []

    for i in S:

        if not stack and i == '+':
            stack.append(i)
        elif stack and i == '+':
            postfix += stack.pop()
            stack.append(i)
        else:
            postfix += i
    else:
        postfix += stack.pop()

    for i in postfix:
        if i != '+':
            cal.append(int(i))
        elif i == '+':
            num2 = cal.pop()
            num1 = cal.pop()
            cal.append(num1+num2)

    print("#{} {}".format(tc, *cal))