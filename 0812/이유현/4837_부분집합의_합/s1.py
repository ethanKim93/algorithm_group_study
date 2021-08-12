import sys
sys.stdin = open('sample_input.txt')

A = list(range(1, 13))
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    result = 0
    for i in range(1<<12):
        part = 0
        cnt = 0

        for j in range(12):
            if i & (1<<j):
                part += A[j]
                cnt += 1
        if K == part and N == cnt:
            result += 1

    print('#{} {}'.format(tc, result))


