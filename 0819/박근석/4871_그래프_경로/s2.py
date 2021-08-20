import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    #인풋값 먼저 만들어 보기
    V, E = map(int, input().split())
    matrix = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        matrix[start].append(end)
    S, G = map(int, input().split())

    visited = [0] * (V+1)

    stack = [S]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = 1
            for v in matrix[vertex]:
                if not visited[v]:
                    stack.append(v)

    result = 1 if visited[G] else 0
    print('#{} {}'.format(tc, result))