import sys

sys.stdin = open("sample_input.txt")


def dfs(V):
    visited[V] = 1
    for i in empty[V]:
        if visited[i] == 0:
            dfs(i)


T = int(input())
for tc in range(0, T):
    V, E = map(int, input().split())
    empty = [[] * V for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        empty[a].append(b)
    S, G = map(int, input().split())

    dfs(S)

    if visited[G] == 1:
        print("#" + str(tc + 1), 1)
    else:
        print("#" + str(tc + 1), 0)