"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

import sys
sys.stdin = open('input.txt')


def bfs(v):
    place = v - 1
    queue = [place]
    c = 1
    while queue:
        p = queue.pop(0)
        if not cnt[p]:
            cnt[p] = c
            while Road[p]:
                node = Road[p].pop(0)
                queue.append(node)
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