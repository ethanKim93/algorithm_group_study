for case in range(int(input())):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    for i in range(N, -1, -1):
        if tree[i] == 0:
            try:
                tree[i] += tree[i * 2]
                tree[i] += tree[i * 2 + 1]
            except:
                pass

    print("#{} {}".format(case + 1, tree[L]))