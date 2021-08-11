import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    sum_bin_list = []
    for i in range(0, N-M+1):
        temp_total =0
        for k in range(i,i+M):
            temp_total += nums[k]
        sum_bin_list.append(temp_total)

    big = sum_bin_list[0]
    mini = sum_bin_list[0]
    for k in sum_bin_list:
        if k > big:
            big = k
    for j in sum_bin_list:
        if j < mini:
            mini = j

    print('#{} {}'.format(tc, big-mini))

