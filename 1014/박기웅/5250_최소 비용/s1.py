import sys
sys.stdin = open('sample_input.txt')

d = [0, 0 , -1, 1]
def bfs(i, j):
    Q = [(i, j)]
    key[i][j] = 0
    for r, c in Q:
        for k in range(4):
            nr, nc = r+d[k], c+d[k-2]
            if nr < 0 or nr >= N or nc < 0 or nc >=N: continue
            if arr[nr][nc] > arr[r][c]:
                if key[nr][nc] > arr[nr][nc]-arr[r][c] + key[r][c] + 1:
                    key[nr][nc] = arr[nr][nc]-arr[r][c] + key[r][c] + 1
                    Q.append((nr, nc))
            else:
                if key[nr][nc] > key[r][c] + 1:
                    key[nr][nc] = key[r][c] + 1
                    Q.append((nr, nc))
    return key[-1][-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 1000000 # H는 최대 1000이나 격자를 지나면서 누적될 수 있으므로 더 큰 값으로 초기화 // 1000으로 했더니 6개만 맞음...
    key = [[INF]*N for _ in range(N)]
    print('#{} {}'.format(tc, bfs(0,0)))

# 모든 격자를 정점으로 본 dijkstra 시간 복잡도 N**4 ....
# def dijkstra(i, j): # 시작점
#     key[i][j] = 0
#     minV = INF
#     u = (i, j)
#     # 모든 정점 순회
#     for _ in range(N):
#         for _ in range(N):
#             # 최소 정점 찾기
#             for i in range(N):
#                 for j in range(N):
#                     if not MST[i][j]:
#                         if key[i][j] < minV:
#                             u = (i, j)
#                             minV = key[i][j]

#             # 최소 신장 트리 업데이트
#             MST[u[0]][u[1]] = 1

#             for r in range(N):
#                 for c in range(N):
#                     for k in range(4):
#                         nr, nc = r+d[k], c+d[k-2]
#                         if nr < 0 or nr >= N or nc < 0 or nc >=N: continue
#                         if not MST[nr][nc]:
#                             if arr[nr][nc] > arr[r][c]:
#                                 key[nr][nc] = min(key[nr][nc], arr[nr][nc]-arr[r][c] + key[r][c] + 1)
#                             else:
#                                 key[nr][nc] = min(key[nr][nc], key[r][c] + 1)
#     return key[-1][-1]


    