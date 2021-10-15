import sys
sys.stdin = open('input.txt')

def dijkstra():
    INF = 10000
    dist = [0] + [INF] * N
    visit = [0] * (N + 1)

    pq = [(0,0)]  # 0에서 0까지의 거리
    while pq:
        v,w = pq.pop(0)   # v: 정점 w: 정점까지의 가중치(거리)
        if dist[v] < w:
            continue
        numbers = list(range(N+1))
        numbers.sort(key=lambda x:arr[v][x])
        for e in numbers:
            if arr[v][e]:
                next_v,next_w = e, arr[v][e]
                if w+next_w < dist[next_v]:
                    dist[next_v] = w+next_w
                    pq.append((next_v,dist[next_v]))
    return dist[N]

T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(E)]
    arr = [[11]*(N+1) for _ in range(N+1)]
    for s,e,w in edges:
        arr[s][e] = w
    print('#{} {}'.format(tc,dijkstra()))