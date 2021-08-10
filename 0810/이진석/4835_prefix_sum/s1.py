import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    sum_max = 0         # 최소합
    sum_min = 10000*M     # 최대합
    for i in range(N-M+1):
        temp_sum = 0
        for j in range(M):
            temp_sum += nums[i+j]
        if temp_sum > sum_max:
            sum_max = temp_sum
        if temp_sum < sum_min:
            sum_min = temp_sum

    print('#{} {}'.format(tc, sum_max-sum_min))