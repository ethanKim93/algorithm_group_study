
def dfs(n):
    global res
    visited[n] = 1
    res += 1
    result.append(res)
    for w in arrList[n]:
        if visited[w] == 0 :
            dfs(w)
            visited[w] = 0
            res -= 1


T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arrList = [[] for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int,input().split())
        arrList[x].append(y)
        arrList[y].append(x)
    result = []
    for i in range(1,N+1):
        res = 0
        visited = [0] * (N + 1)
        dfs(i)

    print('#{} {}'.format(tc, max(result)))



# bfs로 구현할 시 오류
# def bfs(n):
#     que = []
#     que.append(n)
#     visited[n] = 1
#     while que:
#         v = que.pop(0)
#         for w in arrList[v]:
#             if visited[v] <= visited[w]:
#                 visited[w] += 1
#             elif visited[w] == 0 :
#                 que.append(w)
#                 visited[w] = visited[v] + 1
#     return max(visited)
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     arrList = [[] for _ in range(N+1)]
#     for _ in range(M):
#         x,y = map(int,input().split())
#         arrList[x].append(y)
#         arrList[y].append(x)
#     result = 0
#     for i in range(1,N+1):
#         visited = [0] * (N + 1)
#         res = bfs(i)
#         if res > result:
#             result = res
#     print('#{} {}'.format(tc, result))

# 시도해본 반례
"""
1
5 5
1 2
2 3
2 4
4 5
5 3
"""
"""
1
4 4
1 2
1 3
1 4
2 3
"""
