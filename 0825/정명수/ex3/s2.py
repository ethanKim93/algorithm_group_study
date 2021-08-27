import sys
sys.stdin = open('input.txt')
#인접행렬
V, E = map(int,input().split())
way = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]
def bfs(s,V):
    q = []
    visited = [0]*(V+1)
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        print(t)
        for i in range(1,V+1):
            if adj[t][i] ==1 and visited[i]==0:
                q.append(i)
                visited[i] = 1

for i in range(E):
    n1,n2 = way[2*i],way[2*i+1]
    adj[n1][n2] = 1
bfs(1,V)

