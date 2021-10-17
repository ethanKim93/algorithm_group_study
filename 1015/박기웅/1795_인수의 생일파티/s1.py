import sys
sys.stdin = open('input.txt')

def bfs(st, adj):
    Q = [st]
    time = [INF]*(N+1)
    time[st] = 0
    for s in Q:
        for v in range(1, N+1):
            if adj[s][v] and time[v] > time[s] + adj[s][v]:
                time[v] = time[s] + adj[s][v]
                Q.append(v)
    return time

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]       
    adj_rev = [[0]*(N+1) for _ in range(N+1)]       # 역방향 연산용 
    INF = 10000000

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x][y] = c
        adj_rev[y][x] = c
    
    forward, backward = bfs(X,adj_rev), bfs(X, adj)
    max_time = max([x+y for x, y in zip(forward[1:], backward[1:])])
    print('#{} {}'.format(tc, max_time))

### dijkstra 시간초과 ...
# def dijkstra(st, end):
#     MST = [0]*(N+1)
#     time = [INF]*(N+1)
#     time[st] = 0

#     for _ in range(N):
#         u = 0
#         minV = INF
#         # 최소 가중치 정점 선택
#         for i in range(N+1):
#             if not MST[i]:
#                 if time[i] < minV:
#                     u = i
#                     minV = time[i]
#         # 최소 신장 트리 추가
#         MST[u] = 1

#         for v in range(N+1):
#             if not MST[v] and adj[u][v]:
#                 time[v] = min(time[v], time[u]+adj[u][v])

#     return time

# T = int(input())

# for tc in range(1, T+1):
#     N, M, X = map(int, input().split())
#     adj = [[0]*(N+1) for _ in range(N+1)]
#     INF = 10000000

#     for _ in range(M):
#         x, y, c = map(int, input().split())
#         adj[x][y] = c
    
#     max_time = 0
#     for i in range(1, N+1):
#         if i != X:
#             back = dijkstra(X, i)
#             break
#     for i in range(1, N+1):
#         if i != X:
#             forward = dijkstra(i, X)
#             max_time = max(max_time, forward[X] + back[i])
    
#     print('#{} {}'.format(tc, max_time))