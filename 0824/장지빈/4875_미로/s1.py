import sys
sys.stdin = open('input.txt')
# from pprint import pprint

# 망함
# def Spoint():
#     startingpoint = []
#     for x in range(N):
#         for y in range(N):
#             if maze[x][y] == '2':
#                 startingpoint.append(x)
#                 startingpoint.append(y)
#                 return startingpoint
#
# def mazerun(i, j):
#     global visited
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#
#     visited.append([i, j])
#     for a in range(4):
#         ddx = i + dx[a]
#         ddy = i + dy[a]
#         if ddx >= 0 and ddx < N and ddy >= 0 and ddy < N and [i, j] not in visited and maze[ddx][ddy] == '3':
#             return 1
#         elif ddx >= 0 and ddx < N and ddy >= 0 and ddy < N and [i, j] not in visited and maze[ddx][ddy] == '0':
#             mazerun(ddx, ddy)
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     maze = [list(input()) for _ in range(N)]
#     # print(tc,'##############')
#     # pprint(maze)
#     # print('spoint:',Spoint())
#     # print('##############')
#     visited = []
#     # print(mazerun(Spoint()[0], Spoint()[1], visited))
#     # print(Spoint())
#     print(mazerun(Spoint()[0], Spoint()[1]))
#
#
#
#     # print('#{} {}'.format(tc,tc))

T = int(input())
def DFS():

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while stack:
        now = stack.pop()           # r, c = stack.pop 도 가능
        r, c =now[0], now[1]        # 4, 3 담긴 상태로
        maze[r][c] = '1'            # 벽으로 만들면서..
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == '0':
                    stack.append([nr, nc])
                elif maze[nr][nc] == '3':
                    return 1
    return 0        # while의 포인트를 다 돌아도 도착 못하면 0

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    stack = []                                  # tc1 기준 [4, 3]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                stack.append([i, j])

    print('#{} {}'.format(tc, DFS()))       # 인자를 넣지 않고도 가능
