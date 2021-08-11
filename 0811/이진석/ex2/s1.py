import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    flag = 0
    for i in range(1, 1 << len(numbers)):
        temp = 0
        for j in range(len(numbers)):
            if i & (1 << j):
                temp += numbers[j]
        if not temp:
            flag = 1
            break
    print('#{} {}'.format(tc, flag))