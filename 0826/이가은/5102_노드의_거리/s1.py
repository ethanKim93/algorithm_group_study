import sys
sys.stdin = open('sample_input.txt')

def BFS(S, G):
    queue = [S]
    visited = [0] * (V+1)
    distance = [0] * (V+1)

    while queue:
        t = queue.pop(0)

        if not visited[t]:
            visited[t] = 1

            for i in range(1, V+1):
                if graph[t][i] and not visited[i]:
                    queue.append(i)
                    visited[i] =1
                    distance[i] = distance[t] + 1

                    if i == G:
                        return distance[i]

    return 0

T = int(input())

for tc in range(T):
    V, E = map(int, input().split())

    graph = [[0] * (V+1) for _ in range(V+1)]

    for e in range(E):
        e1, e2 = map(int, input().split())
        graph[e1][e2] = 1
        graph[e2][e1] = 1

    S, G = map(int, input().split())
    print('#{} {}'.format(tc+1, BFS(S, G)))