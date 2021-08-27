import sys
sys.stdin = open('sample_input.txt', 'r')

def BPS(s, g):
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        for i in range(len(edges[t])):
            if visited[edges[t][i]] == 0:
                queue.append(edges[t][i])
                visited[edges[t][i]] = visited[t] + 1

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V + 1)]
    for i in range(1, E + 1):
        s, d = map(int, input().split())
        edges[s] += [d]
        edges[d] += [s]
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    queue = []

    BPS(S, G)
    if visited[G]:
        print("#{} {}".format(tc, visited[G]-1))
    else:
        print("#{} {}".format(tc, 0))
