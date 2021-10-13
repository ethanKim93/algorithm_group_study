from pprint import pprint

def bfs(n):
    q = []
    q.append(n)
    while q:
        p = q.pop(0)
        visited[p] = 1
        print(p, end=' ')
        for i in range(len(edge[p])):
            if edge[p][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
    return

arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
V = len(arr)//2
edge = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(0, len(arr), 2):
    edge[arr[i]][arr[i+1]] = 1
    edge[arr[i+1]][arr[i]] = 1
# pprint(edge)
bfs(1)