import sys
sys.stdin = open('sample_input.txt')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = []
    for i in range(E):
        u, v, w = map(int, input().split())
        graph.append((w, u, v))
    graph.sort()
    p = [i for i in range(V+1)]

    N = V+1
    cnt = 0
    total = 0
    for w, u, v in graph:
        if find_set(u) != find_set(v):
            cnt += 1
            total += w
            union(u, v)
            if cnt == N-1:
                break

    print('#{} {}'.format(tc, total))
