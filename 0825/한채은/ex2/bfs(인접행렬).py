"""
bfs - 인접 행렬 or 인접 리스트 구현
"""
# 인접행렬
def bfs(v):
    q = [v] # 빈 q 만들고 append 해도 상관 없다

    while q: # q가 뭐가 있을 동안에
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1 #방문 하면 1
            print(v, end = '')
            for w in range(1, V+1):
                if Graph[v][w] and not visited[w]:
                    q.append(w)
import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)  # 활용하기 위해 숫자로 변환
V, E = map(int,input().split())
# 간선 정보 초기화
edge = list(map(int, input().split()))
# Graph 초기화
Graph = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    Graph[edge[i*2]][edge[i*2+1]] = 1
    Graph[edge[i*2+1]][edge[i*2]] = 1
print(Graph)
# 방문 표시 초기화
visited = [0] * (V+1)
# bfs 탐색 시작
bfs(1)