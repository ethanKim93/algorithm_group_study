# 수업 못 들은 게 크네요...주말에 보충하겠습니다. ㅠㅠ

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])

    INF = float('inf')
    dist = [INF] * (V+1)
    selected = [False] * (V+1)

    dist[0] = 0
    cnt = 0
    while cnt < (V):
        min = INF
        u = -1
        for i in range(V+1):
            if not selected[i] and dist[i] < min:
                min = dist[i]
                u = i
        # 결정
        selected[u] = True
        cnt += 1
        # 간선완화
        for w, cost in adj[u]:  # 도착정점, 가중치
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
    print("#{} {}".format(tc, dist[V]))