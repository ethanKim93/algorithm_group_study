import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10**9)

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def route(now_x, now_y):
    global max_cnt, min_start, cnt, start

    if cnt > max_cnt:
        max_cnt = cnt
        min_start = start

    if max_cnt == cnt:
        if min_start > start:
            min_start = start

    for arrow in range(4):
        nx = now_x + dx[arrow]
        ny = now_y + dy[arrow]
        if 0 <= nx < N and 0 <= ny < N:
            if rooms[nx][ny] == rooms[now_x][now_y]+1:
                cnt += 1
                route(nx, ny)
                cnt -= 1

for tc in range(1, int(input())+1 ):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    start = 0
    cnt = 1
    max_cnt = 0
    min_start = 987654321
    flag = False
    for i in range(N):
        for j in range(N):
            start = rooms[i][j]
            route(i, j)

    print('#{} {} {}'.format(tc, min_start, max_cnt))

