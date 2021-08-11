import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    subset_list = []
    result = 0

    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(arr[j])
        subset_list.append(subset)

    for subset in subset_list:
        sum_num = 0
        if len(subset) != 0:
            for num in subset:
                sum_num += num
            if sum_num == 0:
                result = 1
    print('#{} {}'.format(tc, result))
