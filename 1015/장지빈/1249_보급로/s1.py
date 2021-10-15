import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    timetrix[x][y] = 0
    while q:
        newone = q.popleft()
        x, y = newone[0], newone[1]
        for i in range(4):
            nx, ny = newone[0]+dx[i], newone[1]+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if timetrix[nx][ny] > timetrix[x][y] + matrix[nx][ny]:
                    timetrix[nx][ny] = timetrix[x][y] + matrix[nx][ny]
                    q.append([nx, ny])
    return

for tc in range(1, int(input())+1):
    ans = 0
    INF = 987654321
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    timetrix = [[INF]*N for _ in range(N)]
    s = [0, 0]
    e = [N-1, N-1]
    bfs(0, 0)
    # print(matrix)
    ans = timetrix[e[0]][e[1]]
    # pprint(timetrix)
    print('#{} {}'.format(tc, ans))