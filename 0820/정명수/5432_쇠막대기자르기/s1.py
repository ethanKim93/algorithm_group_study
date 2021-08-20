import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T+1):
    iron = input()
    now = 0
    answer = 0
    i = 0
    while i < len(iron):
        if iron[i] == '(' and iron[i+1] == ')':
            answer += now
            i += 2
            continue
        elif iron[i] == '(':
            now += 1
        else:
            now -= 1
            answer += 1
        i += 1
    print('#{} {}'.format(test_case,answer))