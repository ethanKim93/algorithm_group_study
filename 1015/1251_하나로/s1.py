import sys
sys.stdin = open('input.txt')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    graph = []
    p = list(range(N))

    # 간선 정보 만들기
    for i in range(N):
        for j in range(i+1, N):
            w = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
            graph.append((w, i, j))
    graph.sort()

    ans = 0
    cnt = 0
    for w, u, v in graph:
        if find_set(u) != find_set(v):
            cnt += 1
            ans += w
            union(u, v)
            if cnt == N-1:
                break
    print('#{} {}'.format(tc, round(ans * E)))