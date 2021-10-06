import sys
sys.stdin = open("sample_input.txt")

dx = [0, 1]
dy = [1, 0]

def f_road(x, y, cnt):
    global result
    if x == N-1 and y == N-1:
        cnt += field[x][y]
        if cnt < result:
            result = cnt
            return

    if cnt > result:
        return

    for arrow in range(2):
        nx = x + dx[arrow]
        ny = y + dy[arrow]
        if (x <= N-1 and y <= N-1) and not visited[x][y]:
            visited[x][y] = 1
            f_road(nx, ny, cnt+field[x][y])
            visited[x][y] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    result = (N*2-1) * 10
    visited = [[0] * N for _ in range(N)]
    f_road(0, 0, 0)

    print("#{} {}".format(tc, result))

