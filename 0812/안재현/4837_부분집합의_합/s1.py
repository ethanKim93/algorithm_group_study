import sys
sys.stdin = open('sample_input.txt')

A = int(input())
for tc in range(0, A):
    N, K = map(int, input().split())
    M = [i for i in range(1, 13)]
    n = len(M)
    cnt = 0
    for i in range(1 << n):
        val = 0
        cnt2 = 0
        for j in range(n):
            if i & (1 << j):
                val += M[j]
                cnt2 += 1
        if val == K and N == cnt2:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))
