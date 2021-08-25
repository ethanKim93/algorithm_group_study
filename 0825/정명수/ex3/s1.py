# BFS 구현 (인접리스트)
import sys
sys.stdin = open('input.txt')

def bfs(s,V):
    q = [s]
    visited = [0]*(V+1)
    while q:
        t = q.pop(0)
        visited[t] = 1
        print(t)
        for i in adj[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

V, E = map(int,input().split())
way = list(map(int,input().split()))
adj = [[] for _ in range(E)]
for i in range(E):
    adj[way[2*i]].append(way[2*i+1])
bfs(1,V)
