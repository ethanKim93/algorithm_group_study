import sys
sys.stdin = open('sample_input.txt')

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def BFS():
    while move:                       # move = [[3,3]]
        r, c = move.pop(0)            # r = 4, c = 3
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]       # nr = 5 , nc = 3
            if 0 <= nr < N and 0 <= nc < N and not dist[nr][nc]:
                if maze[nr][nc] == '0':
                    move.append([nr, nc])
                    dist[nr][nc] = dist[r][c] + 1
                elif maze[nr][nc] == '3':
                    return dist[r][c]
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    move = []          # [[4,3]]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':       # 시작 좌표 찾아서
                move.append([i,j])          # 할당
                break

    print(BFS())
