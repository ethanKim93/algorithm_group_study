import heapq


def Prim():
    visited = [0] * (V+1)
    heap = []
    heapq.heappush(heap, (0, 0))
    ans = 0

    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = 1

            for idx, weight in adj[v]:
                if not visited[idx]:
                    heapq.heappush(heap, (weight, idx))
    return ans


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append((n2, w))
        adj[n2].append((n1, w))

    print('#{} {}'.format(tc, Prim()))