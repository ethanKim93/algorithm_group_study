import sys
sys.stdin = open('sample_input.txt')        #수업때 못풀어서 예시코드로.

T = int(input())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def BFS():
    while move:
        r, c = move.pop(0)
        for i in range(4):
            a = r + dr[i]
            b = c + dc[i]
            if 0 <= a < N and 0 <= b < N and not dist[a][b]:
                if maze[a][b] == '0':
                    move.append([a, b])
                    dist[a][b] = dist[r][c] + 1
                elif maze[a][b] == '3':
                    return dist[r][c]
    return 0

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    move = []
    dist = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                move.append([i,j])
                break
    print('#{} {}'.format(tc, BFS()))