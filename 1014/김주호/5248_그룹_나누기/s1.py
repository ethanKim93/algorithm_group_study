def DFS(start):
    for col in range(1, N + 1):
        if pick[start][col] and check[col]:
            check[col] = False
            DFS(col)


for case in range(int(input())):
    N, M = map(int, input().split())
    pick = [[0] * (N + 1) for _ in range(N + 1)]
    st = list(map(int, input().split()))
    for i in range(M):
        pick[st[2 * i]][st[2 * i + 1]] = 1
        pick[st[2 * i + 1]][st[2 * i]] = 1

    check = [True] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if check[i]:
            check[i] = False
            cnt += 1
            DFS(i)

    print("#{} {}".format(case + 1, cnt))
