import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    if N < M:
        N, M = M, N

    maxi = 0
    mini = 999999

    for i in range(N-M+1):
        total = 0
        for j in range(i, M+i):
            total = total + L[j]

        if total > maxi:
            maxi = total

        if total < mini:
            mini = total

    print('#{} {}'.format(tc, maxi - mini))