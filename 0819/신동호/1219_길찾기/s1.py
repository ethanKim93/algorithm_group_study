import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    t, N = list(map(int, input().split()))
    couples = list(map(int, input().split()))
    start = couples[::2]
    end = couples[1::2]
    S, G = 0, 99
    visited = [0] * (100)
    matrix = [[] for _ in range(100)]
    for i in range(N):
        matrix[start[i]].append(end[i])
    stack = [S]
    while stack:
        check = stack.pop()
        if not visited[check]:
            visited[check] = 1
            for v in matrix[check]:
                if not visited[v]:
                    stack.append(v)
    print('#{} {}'.format(tc, visited[G]))