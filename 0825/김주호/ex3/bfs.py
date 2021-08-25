"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

import sys
sys.stdin = open('input.txt')


def bfs(v):
    queue = [0] * V
    queue[0] = v - 1
    front = -1
    rear = 0

    c = 1
    while front != rear:
        front += 1
        front %= V
        p = queue[front]
        if not cnt[p]:
            cnt[p] = c
            for node in Road[p]:
                rear += 1
                rear %= V
                queue[rear] = node
            c += 1

    print(cnt)


# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
route = list(map(int, input().split()))

# Graph 초기화
Road = [[] for _ in range(V)]

for i in range(E):
    Road[route[i * 2] - 1].append(route[i * 2 + 1] - 1)
# 방문 표시 초기화
cnt = [0] * V
# bfs 탐색 시작
bfs(1)