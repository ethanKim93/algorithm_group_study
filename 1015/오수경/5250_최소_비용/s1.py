# 처음에 갑자기 재귀랑 착각해서 중간에 마지막 위치에 도달하면 return되는 중단조건을 넣어버렸다!! -> 완전탐색이 안되어버림
# 아무생각 없이 만들지 말자...

import sys
sys.stdin = open('sample_input.txt')
from collections import deque

def bfs(i, j):
    visited[i][j] = 0
    way = deque()
    way.append([i, j])

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while way:
        now = way.popleft()
        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if board[now[0]][now[1]] < board[ni][nj]:
                    if visited[ni][nj] > visited[now[0]][now[1]] + 1 + (board[ni][nj] - board[now[0]][now[1]]):
                        visited[ni][nj] = visited[now[0]][now[1]] + 1 + (board[ni][nj] - board[now[0]][now[1]])
                        way.append([ni, nj])
                    continue

                else:
                    if visited[ni][nj] > visited[now[0]][now[1]] + 1:
                        visited[ni][nj] = visited[now[0]][now[1]] + 1
                        way.append([ni, nj])
                    continue



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[987654321]*N for _ in range(N)]

    bfs(0, 0)
    print('#{} {}'.format(tc, visited[N-1][N-1]))
