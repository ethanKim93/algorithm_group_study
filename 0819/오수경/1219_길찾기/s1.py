import sys
sys.stdin = open('input.txt')


def DFS(v):
    route = []
    visited[v] = 1

    for w in range(100):
        if node[v][w] == 1 and visited[w] == 0:
            route.append(w+1)

    for r in route:
        DFS(r-1)

    if visited[99] == 1:
        return 1
    else:
        return 0



for tc in range(1, 11):
    tc, tc_len = map(int, input().split())
    node_link = input().split()


    node = [[0] * 100 for _ in range(100)]


    i = []
    j = []
    for a in range(tc_len*2):
        if a % 2 == 0:
            i.append(int(node_link[a]))

    for b in range(tc_len*2):
        if b % 2 != 0:
            j.append(int(node_link[b]))

    for n in range(tc_len):
        node[i[n]][j[n]] = 1

    visited = [0] * 100
    print("#{} {}".format(tc, DFS(0)))
