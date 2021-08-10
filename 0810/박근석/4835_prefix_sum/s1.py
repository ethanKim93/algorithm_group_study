import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    total = 0
    min_total = 0

    for i in range(0, M):
        total += nums[i]

    for i in range(0, M):
        min_total += nums[i]
    # print(min_total)

    for i in range(0, N-M):
        if total < total - nums[i] + nums[i+M]:
            total = total - nums[i] + nums[i+M]
        if min_total > min_total - nums[i] + nums[i+M]:
            min_total = min_total - nums[i] + nums[i+M]

    print(total)
    print(min_total)