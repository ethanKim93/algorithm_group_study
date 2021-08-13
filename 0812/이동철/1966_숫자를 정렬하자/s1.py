import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, len(arr) - 1):
        min_num = i
        for j in range(i + 1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]

    print('#{}'.format(tc), end=' ')
    print(*arr)
