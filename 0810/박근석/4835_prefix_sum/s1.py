import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    total = 0

    for i in range(0, M):
        total += nums[i]

    list_a = []
    list_a.append(total)

    for i in range(0, N-M):
        list_a.append(total - nums[i] + nums[i+M])
        total = total - nums[i] + nums[i + M]

    max_num = list_a[0]
    for i in list_a:
        if max_num < i:
            max_num = i

    min_num = list_a[0]
    for j in list_a:
        if min_num > j:
            min_num = j

    print('#{} {}'.format(tc, max_num - min_num))

