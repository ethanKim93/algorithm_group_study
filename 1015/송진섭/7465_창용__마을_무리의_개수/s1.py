"""
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
"""
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

    p = [i for i in range(N+1)]

    for i in range(M):
        x, y = map(int, input().split())
        union(x, y)

    result = []
    for i in range(1, len(p)):
        result.append(find_set(i))

    print('#{} {}'.format(tc, len(set(result))))