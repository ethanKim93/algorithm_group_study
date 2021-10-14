def dijkstra():
    check = [True] * (N + 1)
    check[0] = False

    for _ in range(N):
        now = 0
        cost = 11

        for idx in range(N + 1):
            if check[idx] and cost > min_costs[idx]:
                cost = field[0][idx]
                now = idx
        check[now] = False

        for target in range(N + 1):
            if field[now][target] != 11:
                new_costs = min_costs[now] + field[now][target]
                if min_costs[target] > new_costs:
                    min_costs[target] = new_costs


for case in range(int(input())):
    N, E = map(int, input().split())
    load = [list(map(int, input().split())) for _ in range(E)]
    field = [[11] * (N + 1) for _ in range(N + 1)]

    for s, e, w in load:
        field[s][e] = w

    field[0][0] = 0

    min_costs = field[0][:]
    dijkstra()
    print("#{} {}".format(case + 1, min_costs[-1]))
