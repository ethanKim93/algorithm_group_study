# 오답
import sys
sys.stdin = open('sample_input.txt')

dr = [1, -1, 0, 0]  # 하 상 우 좌
dc = [0, 0, 1, -1]


def dfs():
    while stack:
        vertex_r, vertex_c = stack.pop()
        if not visited[vertex_r][vertex_c]:
            visited[vertex_r][vertex_c] = 1
            for k in range(4):
                mr, mc = vertex_r + dr[k], vertex_c + dc[k]
                if 0 <= mr < N and 0 <= mc < N:
                    if visited[mr][mc] == 0 and miro[mr][mc] == '0':
                        vertex_r, vertex_c = mr, mc
                        stack.append([vertex_r, vertex_c])
                    elif miro[mr][mc] == '2':
                        return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = list(list(input()) for _ in range(N))
    goal_row = 0
    goal_col = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '3':
                goal_row = i
                goal_col = j

    stack = [[goal_row, goal_col]]
    visited = [[0] * N for _ in range(N)]

    print('#{} {}'.format(tc, dfs()))
