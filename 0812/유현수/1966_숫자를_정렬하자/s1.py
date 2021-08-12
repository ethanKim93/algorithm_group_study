import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_n = 0
    for n in arr:
        if max_n < n:
            max_n = n

    counts = [0] * (max_n + 1)

    for i in range(N):
        counts[arr[i]] += 1

    for i in range(max_n):
        counts[i+1] += counts[i]

    result = [0] * N
    for i in range(N):
        result[counts[arr[i]]-1] = arr[i]
        counts[arr[i]] -= 1

    print('#{} '.format(tc), end='')
    print(*result, sep=' ')