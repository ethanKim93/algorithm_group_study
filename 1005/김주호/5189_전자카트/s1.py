def goto(now=0, score=0, step=0):
    global minimum
    if score >= minimum:
        return

    if step == N - 1:
        if score + field[now][0] < minimum:
            minimum = score + field[now][0]
        return

    for i in range(1, N):
        if check[i]:
            check[i] = False
            goto(i, score + field[now][i], step + 1)
            check[i] = True


for case in range(int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    check = [True] * N
    check[0] = False
    minimum = 100 * N * N

    goto()

    print("#{} {}".format(case + 1, minimum))
