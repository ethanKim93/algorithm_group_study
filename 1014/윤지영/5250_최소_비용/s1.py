import sys
sys.stdin = open('sample_input.txt')

import collections

def bfs(n):
    que = collections.deque()
    que.append(n)
    arr[n[0]][n[1]] = 0
    while que:
        x,y = que.popleft()
        for k in range(4):
            nx = x+ di[k]
            ny = y + dj[k]
            if 0<= nx < N and 0 <= ny < N :
                plus_cost = 0
                if board[nx][ny] > board[x][y]:
                    plus_cost = board[nx][ny] - board[x][y]
                if arr[nx][ny] > arr[x][y] + plus_cost + 1:
                    arr[nx][ny] = arr[x][y]+plus_cost+1
                    que.append([nx,ny])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    INF = 987654321                 # 최대 높이가 1000인거지 최대 비용이 1000인게 아니다 ㅠㅠㅠㅠ
    arr = [[INF] * N for _ in range(N)]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    bfs([0,0])
    res = arr[N-1][N-1]
    print('#{} {}'.format(tc,res))


# 다익스트라 실패..
# def dijkstra(s):
#     global INF
#     visited = [[0] * (N+1) for _ in range(N+1)]
#     x,y = s
#     arr[x][y] = 0
#     for _ in range(N*N):
#         minV = INF
#         w = 0
#         for i in range(N):
#             for j in range(N):
#                 if visited[i][j] == 0 and minV > arr[i][j]:
#                     minV = arr[i][j]
#                     w = [i,j]
#         visited[w[0]][w[1]] = 1
#         x, y= w[0], w[1]
#         for k in range(4):
#             nx = x + di[k]
#             ny = y + dj[k]
#             if 0<= nx < N and 0<= ny < N :
#                 plus_cost = 0
#                 if board[nx][ny] > board[x][y]:
#                     plus_cost = board[nx][ny] - board[x][y]
#                 arr[nx][ny] = min(arr[nx][ny], arr[x][y]+plus_cost+1)
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     board = [list(map(int,input().split())) for _ in range(N)]
#     INF = 1000
#     arr = [[INF] * N for _ in range(N)]
#     di = [-1,1,0,0]
#     dj = [0,0,-1,1]
#     dijkstra([0,0])
#     res = arr[N-1][N-1]
#     print('#{} {}'.format(tc,res))