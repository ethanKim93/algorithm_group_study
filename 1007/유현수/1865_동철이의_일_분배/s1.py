import sys
sys.stdin = open('input.txt')


def backtrack(s, total):
    global ans
    if ans >= total:
        return
    if s == N:
        ans = total
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtrack(s+1, total*P[i][s]/100)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    visited = [0] * N
    backtrack(0, 1)
    print('#{} {:.6f}'.format(tc, ans*100, 6))
