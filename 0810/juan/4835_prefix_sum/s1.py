import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    numbers = list(map(int, input().split()))

    temp = 0
    for i in range(M):
        temp += numbers[i]

    max_value = min_value = temp

    for i in range(M, N):
        temp = temp + numbers[i] - numbers[i-M]

        if max_value < temp:
            max_value = temp
        if min_value > temp:
            min_value = temp

    print('#{} {}'.format(tc, max_value-min_value))