import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # nm_list = list(map(int, input().split()))
    # N = nm_list[0]
    # M = nm_list[1]
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    sum_list = []
    for i in range(0, N-M+1):
        sum = 0
        for j in range(0, M):
            sum += nums[i+j]
        sum_list.append(sum)

    max_sum = sum_list[0]
    min_sum = sum_list[0]
    for i in sum_list:
        if i > max_sum:
            max_sum = i
    for i in sum_list:
        if i < min_sum:
            min_sum = i
    result = max_sum - min_sum

    print('#{} {}'.format(tc, result))