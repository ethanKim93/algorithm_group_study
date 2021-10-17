import sys
sys.stdin = open('input.txt')

import heapq
def prim():
    visited = [0]*N
    heap = []
    heapq.heappush(heap,(0,0))           # 거리, 번호
    ans = 0
    while heap:
        d, v = heapq.heappop(heap)
        if not visited[v]:
            ans += d
            visited[v] = 1

            for idx, dst in enumerate(dist[v]):
                if not visited[idx]:
                    heapq.heappush(heap, (dst, idx))
    return ans


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    INF = 98765432100000
    # 각 섬 간의 거리를 저장하는 리스트 정의
    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = (X[i]-X[j])**2 + (Y[i]-Y[j])**2

    print('#{} {:.0f}'.format(tc, E*prim()))