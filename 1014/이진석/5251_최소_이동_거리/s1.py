import sys
sys.stdin = open('sample_input.txt')

def dijkstara(s):       # s : 시작정점, d : 거리(list)
    used[s] = 1         # 시작점 사용 체크

    for i in range(1,N):
        if adj[s][i]:
            distance[i] = adj[s][i]

    for _ in range(N+1):
        minV = inf
        w = 0
        for i in range(N+1):
            if not used[i] and distance[i] < minV:
                minV = distance[i]
                w = i
        used[w] = 1

        for v in range(N+1):
            if adj[w][v] and adj[w][v] + distance[w] < distance[v]:
                distance[v] = adj[w][v] + distance[w]

for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    inf = 10000000
    distance = [0] + [inf] * N  # 시작점에서 노드까지의 거리, 시작점(0)은 0으로 초기화
    used = [0] * (N+1)          # 노드 사용 여부
    for _ in range(E):
        s, e, w = map(int,input().split())
        adj[s][e] = w
    dijkstara(0)
    print('#{} {}'.format(tc, distance[N])) # N번 노드에 도착했을 때의 거리 출력
