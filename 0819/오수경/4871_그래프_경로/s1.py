import sys
sys.stdin = open('sample_input.txt')

def DFS(v):
    route = []
    visited[v] = 1

    for w in range(V):
        if node[v][w] == 1 and visited[w] == 0:
            route.append(w+1)

    for r in route:
        DFS(r-1)

    if visited[test_e-1] == 1:
        return 1
    else:
        return 0



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[0] * V for _ in range(V)]

    for e in range(E):
        start, end = map(int, input().split())
        node[start-1][end-1] = 1


    test_s, test_e = map(int, input().split())
    visited = [0] * V
    print("#{} {}".format(tc, DFS(test_s-1)))