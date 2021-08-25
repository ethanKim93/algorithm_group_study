"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        print('-{}'.format(t), end='')
        for j in arr[t]:
            if not visited[j]:
                queue.append(j)
                visited[j] = visited[t] + 1
    print()

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int,input().split())

# 간선 정보 초기화
node_list = list(map(int, input().split()))
arr = [[] for _ in range(E+1)]

for i in range(E):
    n1, n2 = node_list[i*2], node_list[i*2+1]
    arr[n1].append(n2)
# Graph 초기화
queue = [1]

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)