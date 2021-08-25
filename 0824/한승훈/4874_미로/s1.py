import sys
sys.stdin = open('sample_input.txt')

T = int(input())
# 목적지 도착가능 : 1, 불가능 : 0 출력
# 출발지점 : 2, 도착 지점 : 3, 통로 : 0


def move(u, v):
    global ans
    if maze[u][v] == 3:
        ans = 1
        return

    visited.append((u, v))
    for idx in range(4):
        if 0 <= u+dx[idx] < N and 0 <= v+dy[idx] < N and maze[u+dx[idx]][v+dy[idx]] in [0, 3]:
            if (u+dx[idx], v+dy[idx]) not in visited:
                move(u+dx[idx], v+dy[idx])


for tc in range(1, T+1):
    N = int(input())
    maze = [[] for _ in range(N)]
    for i in range(N):
        maze[i].extend(map(int, input()))
    ans = 0
    dx = [0, 0, -1, 1]  # 우 좌 상 하
    dy = [1, -1, 0, 0]
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                start = [x, y]  # 시작지점의 인덱스값
                break
    visited = []
    move(start[0], start[1])
    print('#{} {}'.format(tc, ans))


