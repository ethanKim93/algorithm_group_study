import sys
sys.stdin = open('sample_input2.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [number for number in range(1, 13)]
    total_list = []
    subset_list = []
    cnt = 0

    for i in range(1 << len(arr)):
        total = 0
        subset = []
        for j in range(len(arr)):
            if i & (1 << j):
                subset.append(arr[j])
                total += arr[j]
        total_list.append(total)
        subset_list.append(subset)

    for i in range(len(subset_list)):
        if len(subset_list[i]) == N and total_list[i] == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))




