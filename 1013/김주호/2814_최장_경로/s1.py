import pprint


def DFS(root, now, step=1):
    for target in range(1, N + 1):
        if field[now][target] == 1 and not mine[target]:
            maps[root][target] = max(step, maps[root][target])
            mine[target] = True
            DFS(root, target, step + 1)
            mine[target] = False


for case in range(int(input())):
    N, M = map(int, input().split())
    field = [[0] * (N + 1) for _ in range(N + 1)]
    maps = [[0] * (N + 1) for _ in range(N + 1)]
    route = [0] * (N + 1)

    for _ in range(M):
        A, B = map(int, input().split())
        field[A][B] = 1
        field[B][A] = 1

    mine = [False] * (N + 1)
    for r in range(1, N + 1):
        mine[r] = True
        DFS(r, r)
        mine[r] = False

    total = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if total < maps[i][j]:
                total = maps[i][j]

    print("#{} {}".format(case + 1, total + 1))
    pprint.pprint(maps)
