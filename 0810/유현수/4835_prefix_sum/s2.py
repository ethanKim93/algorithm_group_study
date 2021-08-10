# 교수님 풀이

import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    temp = 0
    for i in range(M):
        temp += nums[i]

    max_value = min_value = temp

    for i in range(M, N):
        temp = temp + nums[i] - nums[i-M]

        if max_value < temp:
            max_value = temp

        if min_value > temp:
            min_value = temp

    print('#{} {}'.format(tc, max_value - min_value))