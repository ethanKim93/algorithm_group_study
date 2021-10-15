"""
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
"""

def make_set(x):
    p[x] = x


def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


def union(x, y):
    if x < y:
        p[find_set(y)] = find_set(x)
    else:
        p[find_set(x)] = find_set(y)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edge = list(map(int, input().split()))
    p = [0 for _ in range(N + 1)]
    for j in range(1, N+1):
        make_set(j)

    for i in range(0, len(edge), 2):
        union(edge[i], edge[i+1])
    print(p)
    result = []
    for i in range(1, len(p)):
        result.append(find_set(i))
    print(result)
    print('#{} {}'.format(tc, len(set(result))))