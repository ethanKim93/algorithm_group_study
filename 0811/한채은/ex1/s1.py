import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    total = 0
    for x in range(N):
        for y in range(N):
            part = 0    # 초기화가 되어야 정확한 값을 찾을 수 있다.
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    now = arr[nx][ny] - arr[x][y]
                    if now < 0:
                        now *= -1
                    part += now
            total += part
    print(total)
