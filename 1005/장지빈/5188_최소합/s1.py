import sys
sys.stdin = open('input.txt')

dx = [1, 0]
dy = [0, 1]

def check(x, y, s):
    global ans
    visited[x][y] = 1
    if s >= ans:
        return
    if x == y == N - 1:
        if s < ans:
            ans = s
            return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            s += matrix[nx][ny]
            check(nx, ny, s)
            visited[nx][ny] = 0
            s -= matrix[nx][ny]

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += sum(matrix[i])
    visited = [[0]*N for _ in range(N)]
    check(0, 0, matrix[0][0])

    print('#{} {}'.format(tc, ans))