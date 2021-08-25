
"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):

    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t)
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

#from pprint import  pprint
import sys
sys.stdin = open('input.txt')


# V(ertex), E(dge)
V, E = map(int, input().split())  # 정점, 간선
# 간선 정보 초기화
edge = list(map(int,input().split()))
# Graph 초기화
adj = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1
#pprint(adj)

# 방문 표시 초기화

visited = [0]*(V+1)

# bfs 탐색 시작
bfs(1)

