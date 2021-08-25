
def bfs(v):
    front = rear = -1
    rear += 1
    queue[rear] = v
    visited[v] = 1
    while rear != front:
        front += 1
        t = queue[front]
        print('-{}'.format(t), end='')
        for j in arr[t]:
            if not visited[j]:
                rear += 1
                queue[rear] = j
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
queue = [0] * (V+1)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)