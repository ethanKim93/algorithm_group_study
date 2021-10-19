import sys
sys.stdin = open('s_input.txt')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    relationship = []
    for i in range(M):
        relationship.append(list(map(int, input().split())))
    p = list(range(N+1))

    for rel in relationship:
        if len(rel) == 2 and find_set(rel[0]) != find_set(rel[1]):
            union(find_set(rel[0]), find_set(rel[1]))

    tmp = []
    for i in range(1, N+1):
        if find_set(p[i]) not in tmp:
            tmp.append(find_set(p[i]))

    print('#{} {}'.format(tc, len(tmp)))
