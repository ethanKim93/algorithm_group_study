import sys
sys.stdin = open("input.txt")

A = 0
B = 99

for _ in range(1, 11):
    tc, E = map(int, input().split())
    points = list(map(int,input().split()))

    matrix = [[] for _ in range(B+1)]
    for i in range(0, len(points), 2):
        matrix[points[i]].append(points[i+1])

    visited = [0] * (B+1)

    stack = [A]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = 1
            if vertex == B:
                break
            for v in matrix[vertex]:
                if not visited[v]:
                    stack.append(v)

    print('#{} {}'.format(tc, visited[B]))
