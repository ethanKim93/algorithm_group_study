import sys
sys.stdin = open('input.txt')

# prim 알고리즘

def prim(n):
    dist[n] = 0
    p = [0] * (N+1)
    visited = [0] *(N+1)
    for _ in range(N+1):
        minV = INF
        for i in range(N):
            if visited[i] == 0 and minV > dist[i]:
                w = i
                minV = dist[i]
        visited[w] = 1
        for v in range(N):
            if visited[v] == 0 and arr[w][v] :
                dist[v] = min(dist[v], arr[w][v])
                p[v] = w

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_board = list(map(int, input().split()))
    y_board = list(map(int, input().split()))
    E = float(input())
    INF = 987654321987654321
    arr = [[0] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i + 1, N):
            L = (x_board[i] - x_board[j]) ** 2 + (y_board[i] - y_board[j]) ** 2
            w = float(L * E)
            arr[i][j] = w
            arr[j][i] = w
    dist = [INF] * N
    prim(0)
    print('#{} {}'.format(tc, round(sum(dist))))




# 시도1. dfs
# def dfs(n,res,k):
#     global result
#     if res > result:
#         return
#     if k == N-1:
#         result = min(res,result)
#         return
#     visited[n] = 1
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(n,res+arr[n][i], k+1)
#             visited[i] = 0
#             dfs(n+1, res,k)
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     x_board = list(map(int,input().split()))
#     y_board = list(map(int,input().split()))
#
#     E = float(input())
#     INF = 987654321
#     arr = [[0] * N for _ in range(N)]
#     for i in range(N//2+1):
#         for j in range(i+1,N):
#             L = (x_board[i] - x_board[j])**2 + (y_board[i] - y_board[j])**2
#             w = float(L * E)
#             arr[i][j] = w
#             arr[j][i] = w
#     visited = [0] * N
#     result = INF
#     dfs(0,0,0)
#     print(arr)
#     #print('#{} {}'.format(tc, round(res)))


# 시도4 bfs
# import collections
#
# def bfs(n):
#     que = collections.deque()
#     que.append(n)
#     di = [-1,1,0,0]
#     dj = [0,0,-1,1]
#     while que:
#         x,y= que.popleft()
#         for k in range(4):
#             nx = x + di[k]
#             ny = y + dj[k]
#             if 0<= nx < N and 0<= ny < N and [nx,ny] != [0,0]:
#                 if li[nx][ny] > arr[x][y] + arr[nx][ny]:
#                     li[nx][ny] = arr[x][y] + arr[nx][ny]
#                     que.append([nx,ny])


# 시도5. 순열
# def perm(n,k,cost):
#     global res
#     if cost >= res:
#         return
#     if k == n:
#         res = min(cost,res)
#         return
#     else:
#         for i in range(k,N):
#             p[k], p[i] = p[i], p[k]
#             perm(n,k+1,cost+ arr[p[k-1]][p[k]])
#             p[k], p[i] = p[i], p[k]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     x_board = list(map(int, input().split()))
#     y_board = list(map(int, input().split()))
#
#     E = float(input())
#     INF = 987654321
#     arr = [[0] * N for _ in range(N)]
#     for i in range(N-1):
#         for j in range(i + 1, N):
#             L = (x_board[i] - x_board[j]) ** 2 + (y_board[i] - y_board[j]) ** 2
#             w = float(L * E)
#             arr[i][j] = w
#             arr[j][i] = w
#     p = [i for i in range(N)]
#     res = 987654321
#     perm(N,1,0)
#     print(res)