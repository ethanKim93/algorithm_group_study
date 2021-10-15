for case in range(int(input())):
    V, E = map(int, input().split())
    field = [[11] * (V + 1) for _ in range(V + 1)]

    st = [list(map(int, input().split())) for _ in range(E)]
    for n1, n2, w in st:
        field[n1][n2] = w
        field[n2][n1] = w

    check = [False] * (V + 1)
    check[0] = True

    total = 0
    for _ in range(V):
        idx = 0
        val = 11
        for i in range(V + 1):
            if check[i]:
                for j in range(V + 1):
                    if not check[j] and val > field[i][j]:
                        idx = j
                        val = field[i][j]
        check[idx] = True
        total += val

    print("#{} {}".format(case + 1, total))
