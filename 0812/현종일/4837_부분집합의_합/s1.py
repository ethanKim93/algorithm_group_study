import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    total = 0
    for i in range(1 << 12):
        numsum = 0
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                numsum += arr[j]
                cnt += 1
        if numsum == K and N == cnt:
            total += 1
    print('#{} {}'.format(tc, total))
