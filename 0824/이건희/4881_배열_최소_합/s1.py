import sys

sys.stdin = open("input.txt")


def DFS(idx):
    global mn, sm

    if sm >= mn:
        return

    if idx == n:
        if sm < mn:
            mn = sm
        return

    for i in range(n):
        if not already_c[i]:
            already_c[i] = True
            sm += maps[idx][i]
            DFS(idx + 1)
            sm -= maps[idx][i]
            already_c[i] = False


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    already_c = [False] * n
    mn = 10000
    sm = 0

    DFS(0)

    print("#{} {}".format(tc, mn))
