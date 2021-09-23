import sys
sys.stdin = open('input.txt')


def in_order(v):
    global route
    if v:
        in_order(left[v])
        route.append(v)
        in_order(right[v])


for tc in range(1, 11):
    N = int(input())
    info = [list(input().split()) for _ in range(N)]

    alp_dict = dict()
    edge = []

    # 정점을 key로 하고 알파벳을 value로 하는 dict로 가공
    for i in info:
        alp_dict[int(i[0])] = i[1]
        i.pop(1)
        edge.append(list(map(int, i)))

    # tree 구조 가공
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for e in edge:
        if len(e) == 3:
            left[e[0]] = e[1]
            right[e[0]] = e[2]
        elif len(e) == 2:
            left[e[0]] = e[1]

    route = []
    in_order(1)

    print('#{}'.format(tc), end=' ')
    for r in route:
        print(alp_dict[r], end='')
    print()