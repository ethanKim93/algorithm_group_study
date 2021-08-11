import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0] #합쳐 좌우상하 탐색
    res = 0

    for x in range(N):
        total = 0
        for y in range(N):
            for k in range(4): #좌표 하나 당 네방향에 접근
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N: #범위 안에 있을때만
                    tot = abs(arr[nx][ny]) - abs(arr[x][y])
                    if tot >= 0:
                        res += tot
                    elif tot < 0:
                        res -= tot
    print('#{} {}'.format(tc+1, res))