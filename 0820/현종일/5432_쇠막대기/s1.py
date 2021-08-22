import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    case = input()
    cnt = 0
    result = 0
    for i in range(len(case)):
        if case[i] == '(':
            cnt += 1
        elif case[i] == ')' and case[i-1] == '(':
            cnt -= 1
            result += cnt
        elif case[i] == ')':
            cnt -= 1
            result += 1
    print('#{} {}'.format(tc, result))

