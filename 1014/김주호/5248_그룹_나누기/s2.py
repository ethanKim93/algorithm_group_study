def find_set(x):
    if x == pick[x]:
        return x
    else:
        return find_set(pick[x])


def union(x, y):
    pick[find_set(y)] = find_set(x)


for case in range(int(input())):
    N, M = map(int, input().split())
    pick = list(range(N + 1))
    st = list(map(int, input().split()))
    for i in range(M):
        union(st[2 * i], st[2 * i + 1])

    val = set()
    for i in range(1, N + 1):
        val.add(find_set(i))

    print("#{} {}".format(case + 1, len(val)))
