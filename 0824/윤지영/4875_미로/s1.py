import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def maze_find(si,sj,N):
    visited[si][sj] = 1         # 첫 지점 방문 표시
    while stack:                # 돌아갈 지점 없을때까지
        s = stack.pop()
        si, sj = s[0], s[1]
        visited[si][sj] = 1
        for k in range(4):
            ni = si + di[k]             # k = 0이면 아래, 1이면 위, 2면 오른쪽, 3이면 왼쪽
            nj = sj + dj[k]
            if (0 <= ni < N) and (0 <= nj < N):      # 범위내에 속하는지
                if maze[ni][nj] == '3':
                    return 1
                elif (visited[ni][nj] == 0) and (maze[ni][nj] == '0'):
                    stack.append([ni, nj])
    return 0


for tc in range(1,T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    start_j = start_i = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_i = i
                start_j = j
    stack = [[start_i, start_j]]
    print('#{} {}'.format(tc, maze_find(start_i, start_j,N)))

# 재귀
# T = int(input())
#
#
# def maze_find(si,sj,N):
#     global ans
#     visited[si][sj] = 1         # 첫 지점 방문 표시
#     for k in range(4):
#         if ans == 0 :
#             ni, nj = si + di[k], sj + dj[k]
#             if (0 <= ni < N) and (0 <= nj < N) and (visited[ni][nj] == 0) and (maze[ni][nj] == '3'):
#                 ans = 1
#                 return
#             elif (0 <= ni < N) and (0 <= nj < N) and (visited[ni][nj] == 0) and (maze[ni][nj] == '0'):
#                 maze_find(ni, nj, N)
#
#
# for tc in range(1,T+1):
#     N = int(input())
#     maze = [input() for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     di = [1, -1, 0, 0]
#     dj = [0, 0, 1, -1]
#     start_j = start_i = ans = 0
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == '2':
#                 start_i = i
#                 start_j = j
#     stack = [[start_i, start_j]]
#     maze_find(start_i, start_j, N)
#     print('#{} {}'.format(tc, ans))


# 미로에 직접 표시
# T = int(input())
#
# def maze_find():
#     di = [1, -1, 0, 0]
#     dj = [0, 0, 1, -1]
#     while stack:                # 돌아갈 지점 없을때까지
#         now = stack.pop()
#         r, c = now[0], now[1]
#         maze[r][c] = '1'
#         for k in range(4):
#             ni, nj = r + di[k], c + dj[k]
#             if (0 <= ni < N) and (0 <= nj < N):      # 범위내에 속하는지
#                 if maze[ni][nj] == '3':
#                     return 1
#                 elif maze[ni][nj] == '0':
#                     stack.append([ni, nj])
#     return 0
#
#
# for tc in range(1,T+1):
#     N = int(input())
#     maze = [list(input()) for _ in range(N)]
#     stack = []
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == '2':
#                 stack.append([i,j])
#     print('#{} {}'.format(tc, maze_find()))