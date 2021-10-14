import sys
sys.stdin = open('sample_input.txt')
import time
start = time.time()
from collections import deque


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    distance = [[10000] * N for _ in range(N)]
    distance[0][0] = 0
    queue = deque([(0, 0)])
    d = [0, 0, -1, 1]
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + d[k], j + d[k-2]
            plus = 0
            if 0 <= ni < N and 0 <= nj < N:
                if maps[ni][nj] > maps[i][j]:
                    plus = maps[ni][nj]-maps[i][j]
                if distance[ni][nj] > distance[i][j]+1+plus:
                    distance[ni][nj] = distance[i][j]+1+plus
                    queue.append((ni, nj))
    print('#{} {}'.format(tc, distance[N-1][N-1]))

# 시간초과
# def dfs(i, j, cnt):
#     global min_cnt
#     visited[i][j] = 1
#     if cnt > min_cnt:
#         return
#     if i == j == N-1:
#         min_cnt = min(cnt, min_cnt)
#         return
#     for k in range(4):
#         ni, nj = i + d[k], j + d[k-2]
#         if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
#             if maps[ni][nj] > maps[i][j]:
#                 dfs(ni, nj, cnt+(maps[ni][nj]-maps[i][j])+1)
#             else:
#                 dfs(ni, nj, cnt+1)
#             visited[ni][nj] = 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maps = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     min_cnt = 10000
#     d = [0, 0, -1, 1]
#     dfs(0, 0, 0)
#     print('#{} {}'.format(tc, min_cnt))
print("time :", time.time() - start)
