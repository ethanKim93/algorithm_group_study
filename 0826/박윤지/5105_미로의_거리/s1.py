# 왜 맞는지 모르겠다. visited를 이미 온 길로도 다시 갈 수 있게 짜야하는줄 알았는데.... 노드 했던 것처럼 똑같이 해도 답이 맞는다.\
# 0, '0'이 헷갈렸다

import sys
sys.stdin = open('sample_input.txt')

# 출발지 찾기
def find_start(maze, N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


def bfs(si, sj):
    q = [[si, sj]]
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while q:
        t = q.pop(0)
        ti = t[0]
        tj = t[1]
        for k in range(4):
            if 0 <= ti + di[k] < N and 0 <= tj + dj[k] < N:  # maze 안에 있어야함
                if visited[ti + di[k]][tj + dj[k]] == 0:
                    if maze[ti + di[k]][tj + dj[k]] == '0':
                        q.append([ti + di[k], tj + dj[k]])
                        visited[ti + di[k]][tj + dj[k]] = visited[ti][tj] + 1
                    elif maze[ti + di[k]][tj + dj[k]] == '3':
                        return visited[ti][tj]-1
    return 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    si, sj = find_start(maze, N)
    print('#{} {}'.format(tc, bfs(si, sj)))

