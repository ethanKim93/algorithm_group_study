import sys
sys.stdin = open('sample_input.txt')

def backtrack(s=0, tot=0):
    global visited, ans, V, N
    if tot > ans:
        return
    if s == N:
        if tot < ans:
            ans = tot
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtrack(s+1, tot+V[s][i])
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [0] * N
    backtrack()
    print('#{} {}'.format(tc, ans))