import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    A = list(range(1, 13)) # A = 1~12

    total_NK = 0
    for i in range(1<<12):

        total = 0
        cnt = []

        for j in range(12):
            if i & (1<<j):
                cnt.append(A[j])
                total += A[j]

        if total == K and len(cnt) == N:
            total_NK += 1

    print('#{} {}'.format(tc, total_NK))