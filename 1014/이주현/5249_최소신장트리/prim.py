import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    adj = [[0] * (V + 1) for _ in range(V+1)]
    for edge in edges:
        adj[edge[0]][edge[1]] = adj[edge[1]][edge[0]] = edge[2]
    vertexs = [False] * (V + 1)
    min_weight = [11] * (V + 1)
    min_weight[0] = 0

    result = 0

    for i in range(V+1):
        min_value = 11
        min_vertex = -1
        for j in range(V+1):
            if not vertexs[j] and min_value > min_weight[j]:
                min_value = min_weight[j]
                min_vertex = j

        vertexs[min_vertex] = True
        result += min_value

        for j in range(V + 1):
            if not vertexs[j] and adj[min_vertex][j] != 0 and min_weight[j] > adj[min_vertex][j]:
                min_weight[j] = adj[min_vertex][j]

    print(min_weight)
    print(result)