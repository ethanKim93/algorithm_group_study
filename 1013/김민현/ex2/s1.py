#재귀
import sys
sys.stdin = open('input.txt')

T = int(input())


def bfs(graph, v, visited):
  visited[v]=True
  ans_list.append(v)

  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

for tc in range(1,T+1):
    data = list(map(int,input().split()))
    nodes = [list() for _ in range(len(data)//2)]
    for i in range(0,len(data),2):
        nodes[data[i]].append(data[i+1])
    visited = [False] * 9
    ans_list = []

    dfs(nodes, 1, visited)
    print(*ans_list)