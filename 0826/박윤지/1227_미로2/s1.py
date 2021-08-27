# bfs로 풀기
# 1226_미로2 랑 배열 크기만 16, 100으로 다르고 나머지는 똑같다.

import sys
sys.stdin = open('input.txt')

# 출발지 찾기
def find_start(maze):
    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                return i, j

def bfs(si, sj):
    q = [[si, sj]]
    visited = [[0] * 100 for _ in range(100)]
    visited[si][sj] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while q:
        t = q.pop(0)
        ti = t[0]
        tj = t[1]
        for k in range(4):
            if 0 <= ti + di[k] < 100 and 0 <= tj + dj[k] < 100:  # maze 안에 있어야함
                if visited[ti + di[k]][tj + dj[k]] == 0:  # 방문하지 않은 칸일 때 이동
                    if maze[ti + di[k]][tj + dj[k]] == '0':
                        q.append([ti + di[k], tj + dj[k]])
                        visited[ti + di[k]][tj + dj[k]] = 1
                    elif maze[ti + di[k]][tj + dj[k]] == '3':  # 3 찾자마자 return
                        return 1
    return 0


T = 10

for tc in range(1, T+1):
    tc = int(input())
    maze = [list(input()) for _ in range(100)]  # 내용 str임
    si, sj = find_start(maze)
    print('#{} {}'.format(tc, bfs(si, sj)))



# # dfs로 풀기
# # 2. 미로 자체에 흔적남기며 이동
#
# import sys
# sys.stdin = open('input.txt')
#
# # 출발지 찾기
# def find_start(maze):
#     for i in range(100):
#         for j in range(100):
#             if maze[i][j] == '2':
#                 return i, j
#
#
# def dfs():
#     while stack:
#         r, c = stack.pop()
#         maze[r][c] = '1'
#         for k in range(4):
#             nr = r + di[k]
#             nc = c + dj[k]
#             if 0 <= nr < 100 and 0 <= nc < 100:
#                 if maze[nr][nc] == '0':
#                     stack.append([nr, nc])
#                 elif maze[nr][nc] == '3':
#                     return 1
#     return 0
#
#
# T = 10
#
# for tc in range(1, T+1):
#     tc = int(input())
#     maze = [list(input()) for _ in range(100)]  # 내용 str임
#
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     stack = []
#     si, sj = find_start(maze)  # 출발점 찾기
#     stack.append([si, sj])
#
#     print('#{} {}'.format(tc, dfs()))



# # 1. 2차원 배열(visited) 생성 후 방문 체크하면서 이동
# # RecursionError: maximum recursion depth exceeded in comparison
# # 위에 에러 떠서 못풀었다.
#
# import sys
# sys.stdin = open('input.txt')
#
# # 출발지 찾기
# def find_start(maze):
#     for i in range(100):
#         for j in range(100):
#             if maze[i][j] == '2':
#                 return i, j
#
#
# def dfs(si, sj, visited):
#     global ans
#     visited[si][sj] = 1
#     while ans:
#         for k in range(4):
#             if 0 <= si + di[k] < 100 and 0 <= sj + dj[k] < 100:
#                 if maze[si + di[k]][sj + dj[k]] == '0' and visited[si + di[k]][sj + dj[k]] == 0:
#                     visited[si + di[k]][sj + dj[k]] = 1
#                     dfs(si + di[k], sj + dj[k], visited)
#                 elif maze[si + di[k]][sj + dj[k]] == '3' and visited[si + di[k]][sj + dj[k]] == 0:
#                     ans = False
#         return
#     return
#
#
# T = 10
#
# for tc in range(1, T+1):
#     tc = int(input())
#     maze = [list(input()) for _ in range(100)]  # 내용 str임
#
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     stack = []
#     si, sj = find_start(maze)  # 출발점 찾기
#     stack.append([si, sj])
#
#     visited = [[0] * 100 for _ in range(100)]
#     ans = True
#     print(dfs(si, sj, visited))
#
#     if ans:
#         print('#{} {}'.format(tc, 1))
#     else:
#         print('#{} {}'.format(tc, 0))
