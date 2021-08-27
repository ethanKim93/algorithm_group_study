import sys
sys.stdin = open('input.txt')
from pprint import pprint

def BFS(u, v):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = []
    stack.append([u, v])
    visited[u][v] = 1
    while stack:
        now = stack.pop(0)
        for x in range(4):
            ddx = now[0] + dx[x]
            ddy = now[1] + dy[x]
            if 0 <= ddx < N and 0 <= ddy < N and not visited[ddx][ddy]:
                if maze[ddx][ddy] == 0 or maze[ddx][ddy] == 3:
                    stack.append([ddx, ddy])
                    visited[ddx][ddy] = visited[now[0]][now[1]] + 1
                    if [ddx, ddy] == [goal[0], goal[1]]:
                        return visited[now[0]][now[1]] -1
    return 0

for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
            if maze[i][j] == 3:
                goal = [i, j]

    print('#{} {}'.format(tc,BFS(start[0], start[1])))