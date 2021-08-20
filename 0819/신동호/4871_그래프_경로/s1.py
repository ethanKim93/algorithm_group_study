import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    visited = [0] * (V+1)
    matrix = [[] for _ in range(V+1)]
    for _ in range(E):
        st, en = map(int, input().split())
        matrix[st].append(en)
    S, G = list(map(int, input().split()))
    stack = [S]
    while stack:
        check = stack.pop()
        if not visited[check]:
            visited[check] = 1
            for v in matrix[check]:
                if not visited[v]:
                    stack.append(v)
    print('#{} {}'.format(tc, visited[G]))