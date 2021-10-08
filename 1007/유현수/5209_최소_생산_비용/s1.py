# 신동호님 코드 보고 이해한 뒤 작성했습니다.

import sys
sys.stdin = open('sample_input.txt')


def backtrack(s=0, total=0):
    global ans

    if ans < total:
        return

    if s == N:
        if ans > total:
            ans = total
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtrack(s+1, total + V[s][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [0] * N
    backtrack()
    print('#{} {}'.format(tc, ans))
