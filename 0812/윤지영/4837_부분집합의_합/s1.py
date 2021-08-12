import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    sub_set = []
    for i in range(1, 1 << len(A)):
        sub = []
        for j in range(len(A)):
            if i & (1 << j):
                sub.append(A[j])
        sub_set.append(sub)
    cnt = 0
    for n in range(1, len(sub_set)):
        result = 0
        if len(sub_set[n]) == N:
            for k in range(N):
                result += sub_set[n][k]
            if result == K:
                cnt += 1
    print('#{} {}'.format(tc, cnt))
