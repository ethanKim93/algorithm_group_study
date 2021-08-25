import sys
sys.stdin = open('input.txt')
"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    pass
    q = [v]

    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in range(1, V+1):
                if adj[v][w] and not visited[w]:
                    q.append(w)



import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edges = list(map(int, input().split()))

# Graph 초기화
adj = [[0] * (V+1) for _ in range(V+1)]

for i in range(0, len(edges), 2):
    adj[edges[i]][edges[i+1]] = 1
    adj[edges[i+1]][edges[i]] = 1   # 양방향

print(*adj,sep='\n')
# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)